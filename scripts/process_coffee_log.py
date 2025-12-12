import os
import sys
import datetime
from datetime import timezone, timedelta
import plotly.graph_objects as go

# Constants
TIMEZONE_OFFSET = -5  # EST (UTC-5), change to -4 for EDT or your timezone
POUR_INTERVAL_SECONDS = 45
PHASE1_RATIO = 0.4
PHASE2_RATIO = 0.6
DEFAULT_DOSE = 20
DEFAULT_WATER = 300
DEFAULT_RATIO = 15.0
MAX_SLIDER_VALUE = 10
MAX_SCORE = 90  # 9 SCA criteria × 10 points each

# Field names (must match GitHub Issue template labels exactly)
FIELD_BEAN_NAME = 'Bean Name'
FIELD_ROASTER = 'Roaster'
FIELD_ROAST_LEVEL = 'Roast Level'
FIELD_DOSE = 'Dose (g)'
FIELD_WATER = 'Total Water (g)'
FIELD_TEMP = 'Water Temp (°C)'
FIELD_GRINDER = 'Grinder & Setting'
FIELD_FIRST_POUR = 'First Pour Amount (g)'
FIELD_STRENGTH_POURS = 'Strength Pours'
FIELD_POUR_INTERVAL = 'Pour Interval (seconds)'
# SCA Sensory Evaluation (1-10 scale)
FIELD_AROMA = 'Aroma (香气)'
FIELD_FLAVOR = 'Flavor (风味)'
FIELD_AFTERTASTE = 'Aftertaste (余韵)'
FIELD_ACIDITY = 'Acidity (酸质)'
FIELD_BODY = 'Body (醇厚度)'
FIELD_BALANCE = 'Balance (平衡度)'
FIELD_CLEAN_CUP = 'Clean Cup (干净度)'
FIELD_SWEETNESS = 'Sweetness (甜度)'
FIELD_OVERALL = 'Overall (总体评价)'
FIELD_NOTES = 'Tasting Notes'

# SCA Sensory attributes configuration: (display_label, field_name, min_descriptor, max_descriptor)
# Scale: 1-10 for each attribute, max total score = 90
SENSORY_ATTRIBUTES = [
    ('AROMA', FIELD_AROMA, 'Weak', 'Complex'),
    ('FLAVOR', FIELD_FLAVOR, 'Simple', 'Excellent'),
    ('AFTERTASTE', FIELD_AFTERTASTE, 'Short', 'Lingering'),
    ('ACIDITY', FIELD_ACIDITY, 'Flat', 'Bright'),
    ('BODY', FIELD_BODY, 'Light', 'Syrupy'),
    ('BALANCE', FIELD_BALANCE, 'Uneven', 'Harmonious'),
    ('CLEAN CUP', FIELD_CLEAN_CUP, 'Defects', 'Clean'),
    ('SWEETNESS', FIELD_SWEETNESS, 'Dry', 'Sweet'),
    ('OVERALL', FIELD_OVERALL, 'Poor', 'Outstanding'),
]

def parse_numeric_field(data, key, default='0'):
    """Extract first number from field like '10 (Label)' or '93'."""
    try:
        value_str = data.get(key, default)
        return float(value_str.split()[0])
    except (ValueError, IndexError, AttributeError):
        return float(default)


def parse_issue_body(body):
    """Parse GitHub Issue form body into a dictionary of field values."""
    data = {}
    lines = body.split('\n')
    current_key = None
    current_value = []

    for line in lines:
        line = line.strip()
        # 1. New Field Key (### Label)
        if line.startswith('### '):
            if current_key:
                data[current_key] = '\n'.join(current_value).strip()
            current_key = line[4:].strip()
            current_value = []
        # 2. Ignore Section Headers (## Header) inserted by Template
        elif line.startswith('## '):
            continue
        # 3. Capture Value
        else:
            if line:
                current_value.append(line)

    if current_key:
        data[current_key] = '\n'.join(current_value).strip()
    return data


def calculate_balance_profile(first_pour, second_pour):
    """
    Determine balance profile from Phase 1 pour distribution.

    In 4:6 method, Phase 1 controls acidity vs. sweetness:
    - More water in first pour → More acidic
    - More water in second pour → Sweeter
    """
    phase1_midpoint = (first_pour + second_pour) / 2

    if first_pour < phase1_midpoint:
        return "SWEETER"
    elif first_pour > phase1_midpoint:
        return "ACIDIC"
    else:
        return "BALANCED"


def calculate_strength_profile(pour_count):
    """
    Determine strength profile from Phase 2 pour count.

    Fewer pours = lighter body (water flows through faster)
    More pours = stronger body (longer contact time)
    """
    strength_map = {1: "LIGHT", 2: "MEDIUM"}
    return strength_map.get(pour_count, "STRONG")


def generate_radar_plot(scores, labels, output_path):
    """
    Generate a radar/spider plot for SCA sensory evaluation using Plotly.

    Args:
        scores: List of scores (1-10) for each attribute
        labels: List of attribute labels
        output_path: Path to save the plot image
    """
    # Create the radar chart
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=labels,
        fill='toself',
        fillcolor='rgba(99, 110, 250, 0.3)',  # Semi-transparent fill
        line=dict(color='rgb(99, 110, 250)', width=3),
        marker=dict(size=8, color='rgb(99, 110, 250)'),
        name='Score',
        hovertemplate='<b>%{theta}</b><br>Score: %{r}/10<extra></extra>'
    ))

    # Update layout for better appearance
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickvals=[2, 4, 6, 8, 10],
                tickfont=dict(size=12, color='white', family='Garamond, serif'),
                gridcolor='rgba(255, 255, 255, 0.3)',
            ),
            angularaxis=dict(
                tickfont=dict(size=13, color='white', family='Garamond, serif'),
                rotation=90,
                direction='clockwise',
                gridcolor='rgba(255, 255, 255, 0.3)',
            ),
            bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        ),
        showlegend=False,
        title=dict(
            text='SCA Sensory Evaluation',
            font=dict(size=18, color='white', family='Garamond, serif'),
            x=0.5,
            xanchor='center',
            y=0.95,
        ),
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
        plot_bgcolor='rgba(0, 0, 0, 0)',   # Transparent plot background
        margin=dict(l=80, r=80, t=100, b=80),
        width=800,
        height=800,
    )

    # Save as static image
    fig.write_image(output_path, format='png', scale=2)


def generate_sensory_block(data, image_path):
    """Generate sensory analysis radar plot from issue data and calculate total score."""
    scores = []
    labels = []

    for label, field_name, left_desc, right_desc in SENSORY_ATTRIBUTES:
        value = int(parse_numeric_field(data, field_name, '5'))
        scores.append(value)
        labels.append(label)

    total_score = sum(scores)

    # Generate radar plot
    generate_radar_plot(scores, labels, image_path)

    return total_score


def generate_terminal_slider(label, value, left_label, right_label):
    """
    Generates a high-density unicode slider with inline labels.
    Input is 1-10 (matches GitHub Issue template dropdowns).
    Output bar has 10 segments.
    Example: AROMA (Weak vs. Complex) ▕▓▓▓▓▓▓▓░░░▏
    """
    # Normalize value to 1-10 range
    value = max(1, min(MAX_SLIDER_VALUE, value))

    filled = '▓' * value
    empty = '░' * (MAX_SLIDER_VALUE - value)

    # Combine label with descriptive text
    full_label = f"{label} ({left_label} vs. {right_label})"

    # Max label width - should be >= longest label (AFTERTASTE = 32 chars)
    max_label_display_width = 36

    # Ensure consistent padding for alignment
    padding_needed = max_label_display_width - len(full_label)

    return f"{full_label}{' ' * padding_needed} ▕{filled}{empty}▏"

def generate_terminal_timeline(first, second, strength_count, strength_amt, interval_seconds=POUR_INTERVAL_SECONDS):
    """
    Generates a timeline using box drawing characters, with aligned times.
    Each pour interval defaults to POUR_INTERVAL_SECONDS (45s for the 4:6 method).
    """
    pours = [first, second] + [strength_amt] * strength_count

    # Calculate times for header
    times = []
    for i in range(len(pours) + 1):
        total_sec = i * interval_seconds
        m, s = divmod(total_sec, 60)
        times.append(f"{m}:{s:02d}")
    
    # Generate time row: Left align to match start of segments
    # Each segment is 6 chars + 1 separator = 7 chars total width per block
    # We want the time string to start at the tick.
    time_row_parts = []
    for i, t in enumerate(times):
        if i < len(times) - 1:
            # Left align in 7-char field for all but last time
            time_row_parts.append(f"{t:<7}")
        else:
            # Last time: no padding to avoid excessive overhang
            time_row_parts.append(t)
    time_row = "".join(time_row_parts)

    segment = "──────" # 6 chars
    bar_row = "├" + "┼".join([segment] * len(pours)) + "┤"
    
    label_row = ""
    for i, amt in enumerate(pours):
        label_row += f"│  P{i+1:<2} "
    label_row += "│"

    vol_row = ""
    for p in pours:
        # Format as "Xg" then center in 6-char cell
        vol_str = f"{int(p)}g"
        vol_row += f"│{vol_str:^6}"
    vol_row += "│"
    
    bottom_row = "└" + "┴".join([segment] * len(pours)) + "┘"
    
    return f"```text\n{time_row}\n{bar_row}\n{label_row}\n{vol_row}\n{bottom_row}\n```"

def generate_markdown(data, bean_name_for_filename):
    """Generate MkDocs-compatible markdown from parsed issue data."""
    # Get current time in specified timezone
    tz = timezone(timedelta(hours=TIMEZONE_OFFSET))
    today = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    bean = data.get(FIELD_BEAN_NAME, 'Unknown Bean')
    roaster = data.get(FIELD_ROASTER, 'Unknown Roaster')

    # Create image filename and path
    safe_bean_name = "".join([c for c in bean_name_for_filename if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    safe_bean_name = safe_bean_name.replace(' ', '-').lower()
    image_filename = f"{today}-{safe_bean_name}-radar.png"
    image_path = f"docs/assets/coffee/{image_filename}"
    image_rel_path = f"../../assets/coffee/{image_filename}"  # Relative path for markdown

    # Ensure assets directory exists
    os.makedirs('docs/assets/coffee', exist_ok=True)

    # --- Numeric Parsing ---
    try:
        dose = parse_numeric_field(data, FIELD_DOSE, str(DEFAULT_DOSE))
        water = parse_numeric_field(data, FIELD_WATER, str(DEFAULT_WATER))
        ratio = round(water / dose, 1)

        # 4:6 Logic: Phase 1 (Balance) = 40%, Phase 2 (Strength) = 60%
        first_pour = parse_numeric_field(data, FIELD_FIRST_POUR, '60')
        phase1_total = water * PHASE1_RATIO
        second_pour = phase1_total - first_pour

        phase2_total = water * PHASE2_RATIO
        strength_pours_str = data.get(FIELD_STRENGTH_POURS, '2 Pours').split()[0]
        strength_pours_count = int(strength_pours_str)
        strength_pour_amount = round(phase2_total / strength_pours_count)

    except Exception as e:
        print(f"Warning: Error parsing recipe values: {e}", file=sys.stderr)
        print(f"Using default values...", file=sys.stderr)
        dose, water, ratio = DEFAULT_DOSE, DEFAULT_WATER, DEFAULT_RATIO
        first_pour, second_pour = 60, 60
        strength_pours_count = 2
        strength_pour_amount = 90

    # --- Analysis Text ---
    balance_text = calculate_balance_profile(first_pour, second_pour)
    strength_text = calculate_strength_profile(strength_pours_count)

    # --- Visuals (Terminal Pro) ---
    pour_interval = int(parse_numeric_field(data, FIELD_POUR_INTERVAL, str(POUR_INTERVAL_SECONDS)))
    timeline_block = generate_terminal_timeline(first_pour, second_pour, strength_pours_count, strength_pour_amount, pour_interval)

    # Sensory Radar Plot (1-10 scale) and Score Calculation
    total_score = generate_sensory_block(data, image_path)

    md_content = f"""# {today}

!!! abstract "The 4:6 Recipe"
    **Bean:** {bean}
    **Roast:** {data.get(FIELD_ROAST_LEVEL, 'N/A')}
    **Target:** {balance_text} & {strength_text}

    *   **Ratio:** 1:{ratio} ({dose}g In / {water}g Out)
    *   **Grinder:** {data.get(FIELD_GRINDER, 'N/A')}
    *   **Temp:** {data.get(FIELD_TEMP, 'N/A')}°C

    **Phase 1 (Balance):** {int(first_pour)}g ➔ {int(second_pour)}g
    **Phase 2 (Strength):** {strength_pours_count} x {int(strength_pour_amount)}g

## Timeline

{timeline_block}

## Evaluation

![SCA Sensory Evaluation]({image_rel_path})

**Total Score:** {total_score}/{MAX_SCORE}

> "{data.get(FIELD_NOTES, 'No notes provided.')}"
"""
    return md_content, bean

def main():
    if len(sys.argv) < 2:
        print("Usage: python process_coffee_log.py <issue_body>", file=sys.stderr)
        sys.exit(1)

    issue_body = sys.argv[1]
    data = parse_issue_body(issue_body)

    # Validate required fields
    required_fields = [FIELD_BEAN_NAME, FIELD_DOSE, FIELD_WATER]
    missing = [f for f in required_fields if not data.get(f)]
    if missing:
        print(f"Error: Missing required fields: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    # Get bean name for filename generation
    bean_name = data.get(FIELD_BEAN_NAME, 'Unknown Bean')
    content, _ = generate_markdown(data, bean_name)

    # Use same timezone as in generate_markdown for consistency
    tz = timezone(timedelta(hours=TIMEZONE_OFFSET))
    today = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    safe_name = "".join([c for c in bean_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    safe_name = safe_name.replace(' ', '-').lower()
    filename = f"docs/posts/咖啡/{today}-{safe_name}.md"

    os.makedirs('docs/posts/咖啡', exist_ok=True)

    # Warn if overwriting existing file
    if os.path.exists(filename):
        print(f"Warning: {filename} already exists, overwriting...", file=sys.stderr)

    with open(filename, 'w') as f:
        f.write(content)

    print(f"Created journal entry: {filename}")

if __name__ == "__main__":
    main()
