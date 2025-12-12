import os
import sys
import datetime
from datetime import timezone, timedelta
from pathlib import Path
import plotly.graph_objects as go
from jinja2 import Template

# Constants
TIMEZONE_OFFSET, POUR_INTERVAL_SECONDS = -5, 45
PHASE1_RATIO, PHASE2_RATIO = 0.4, 0.6
DEFAULT_DOSE, DEFAULT_WATER, DEFAULT_RATIO = 20, 300, 15.0
MAX_SCORE = 90

# Field names (must match GitHub Issue template labels exactly)
FIELD_BEAN_NAME = 'Bean Name'
FIELD_DOSE = 'Dose (g)'
FIELD_WATER = 'Total Water (g)'

# SCA Sensory attributes: (display_label, field_name, min_descriptor, max_descriptor)
SENSORY_ATTRIBUTES = [
    ('AROMA', 'Aroma (香气)', 'Weak', 'Complex'),
    ('FLAVOR', 'Flavor (风味)', 'Simple', 'Excellent'),
    ('AFTERTASTE', 'Aftertaste (余韵)', 'Short', 'Lingering'),
    ('ACIDITY', 'Acidity (酸质)', 'Flat', 'Bright'),
    ('BODY', 'Body (醇厚度)', 'Light', 'Syrupy'),
    ('BALANCE', 'Balance (平衡度)', 'Uneven', 'Harmonious'),
    ('CLEAN CUP', 'Clean Cup (干净度)', 'Defects', 'Clean'),
    ('SWEETNESS', 'Sweetness (甜度)', 'Dry', 'Sweet'),
    ('OVERALL', 'Overall (总体评价)', 'Poor', 'Outstanding'),
]

def parse_numeric_field(data, key, default='0'):
    """Extract first number from field like '10 (Label)' or '93'."""
    try:
        value_str = data.get(key, default)
        return float(value_str.split()[0])
    except (ValueError, IndexError, AttributeError):
        return float(default)


def parse_issue_body(body):
    """Parse GitHub Issue form body into field dictionary."""
    data = {}
    lines = body.split('\n')
    current_key = None
    current_value = []

    for line in lines:
        line = line.strip()
        if line.startswith('### '):
            if current_key:
                data[current_key] = '\n'.join(current_value).strip()
            current_key = line[4:].strip()
            current_value = []
        elif line.startswith('## '):
            continue
        else:
            if line:
                current_value.append(line)

    if current_key:
        data[current_key] = '\n'.join(current_value).strip()
    return data


def generate_radar_plot(scores, labels, output_path):
    """Generate SCA sensory radar plot using Plotly."""
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=labels,
        fill='toself',
        fillcolor='rgba(99, 110, 250, 0.3)',
        line=dict(color='rgb(99, 110, 250)', width=3),
        marker=dict(size=8, color='rgb(99, 110, 250)'),
        name='Score',
        hovertemplate='<b>%{theta}</b><br>Score: %{r}/10<extra></extra>'
    ))

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
            bgcolor='rgba(0, 0, 0, 0)',
        ),
        showlegend=False,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=80, r=80, t=100, b=80),
        width=800,
        height=800,
    )

    fig.write_image(output_path, format='png', scale=2)


def generate_sensory_block(data, image_path):
    """Generate sensory radar plot and return total score."""
    scores = [int(parse_numeric_field(data, field, '5')) for _, field, _, _ in SENSORY_ATTRIBUTES]
    labels = [label for label, _, _, _ in SENSORY_ATTRIBUTES]
    generate_radar_plot(scores, labels, image_path)
    return sum(scores)


def generate_terminal_timeline(first, second, strength_count, strength_amt, interval_seconds=POUR_INTERVAL_SECONDS):
    """Generate pour timeline using box-drawing characters."""
    pours = [first, second] + [strength_amt] * strength_count
    times = [f"{(i * interval_seconds) // 60}:{(i * interval_seconds) % 60:02d}"
             for i in range(len(pours) + 1)]

    time_row = "".join(f"{t:<7}" if i < len(times)-1 else t for i, t in enumerate(times))
    segment = "──────"
    bar_row = "├" + "┼".join([segment] * len(pours)) + "┤"
    label_row = "".join(f"│  P{i+1:<2} " for i in range(len(pours))) + "│"
    vol_row = "".join(f"│{f'{int(p)}g':^6}" for p in pours) + "│"
    bottom_row = "└" + "┴".join([segment] * len(pours)) + "┘"

    return f"```text\n{time_row}\n{bar_row}\n{label_row}\n{vol_row}\n{bottom_row}\n```"


def generate_markdown(data, bean_name_for_filename):
    """Generate MkDocs-compatible markdown from parsed issue data."""
    tz = timezone(timedelta(hours=TIMEZONE_OFFSET))
    today = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    bean = data.get(FIELD_BEAN_NAME, 'Unknown Bean')

    # Create image filename and path
    safe_bean_name = "".join([c for c in bean_name_for_filename if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    safe_bean_name = safe_bean_name.replace(' ', '-').lower()
    image_filename = f"{today}-{safe_bean_name}-radar.png"
    image_path = f"docs/assets/coffee/{image_filename}"
    image_rel_path = f"../../assets/coffee/{image_filename}"

    os.makedirs('docs/assets/coffee', exist_ok=True)

    # Parse recipe values
    try:
        dose = parse_numeric_field(data, FIELD_DOSE, str(DEFAULT_DOSE))
        water = parse_numeric_field(data, FIELD_WATER, str(DEFAULT_WATER))
        ratio = round(water / dose, 1)

        first_pour = parse_numeric_field(data, 'First Pour Amount (g)', '60')
        phase1_total = water * PHASE1_RATIO
        second_pour = phase1_total - first_pour

        phase2_total = water * PHASE2_RATIO
        strength_pours_str = data.get('Strength Pours', '2 Pours').split()[0]
        strength_pours_count = int(strength_pours_str)
        strength_pour_amount = round(phase2_total / strength_pours_count)

    except Exception as e:
        print(f"Warning: Error parsing recipe values: {e}", file=sys.stderr)
        print(f"Using default values...", file=sys.stderr)
        dose, water, ratio = DEFAULT_DOSE, DEFAULT_WATER, DEFAULT_RATIO
        first_pour, second_pour = 60, 60
        strength_pours_count = 2
        strength_pour_amount = 90

    # Generate timeline and sensory analysis
    pour_interval = int(parse_numeric_field(data, 'Pour Interval (seconds)', str(POUR_INTERVAL_SECONDS)))
    timeline_block = generate_terminal_timeline(first_pour, second_pour, strength_pours_count, strength_pour_amount, pour_interval)
    total_score = generate_sensory_block(data, image_path)

    # Load and render template
    template_path = Path(__file__).parent / 'templates' / 'coffee_journal.jinja2'
    with open(template_path) as f:
        template = Template(f.read())

    md_content = template.render(
        date=today,
        bean=bean,
        roast_level=data.get('Roast Level', 'N/A'),
        ratio=ratio,
        dose=int(dose),
        water=int(water),
        grinder=data.get('Grinder & Setting', 'N/A'),
        temp=data.get('Water Temp (°C)', 'N/A'),
        first_pour=int(first_pour),
        second_pour=int(second_pour),
        strength_count=strength_pours_count,
        strength_amt=int(strength_pour_amount),
        timeline_block=timeline_block,
        image_path=image_rel_path,
        total_score=total_score,
        max_score=MAX_SCORE,
        notes=data.get('Tasting Notes', 'No notes provided.')
    )

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

    # Generate markdown content
    bean_name = data.get(FIELD_BEAN_NAME, 'Unknown Bean')
    content, _ = generate_markdown(data, bean_name)

    # Create output file
    tz = timezone(timedelta(hours=TIMEZONE_OFFSET))
    today = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    safe_name = "".join([c for c in bean_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    safe_name = safe_name.replace(' ', '-').lower()
    filename = f"docs/posts/咖啡/{today}-{safe_name}.md"

    os.makedirs('docs/posts/咖啡', exist_ok=True)

    if os.path.exists(filename):
        print(f"Warning: {filename} already exists, overwriting...", file=sys.stderr)

    with open(filename, 'w') as f:
        f.write(content)

    print(f"Created journal entry: {filename}")


if __name__ == "__main__":
    main()
