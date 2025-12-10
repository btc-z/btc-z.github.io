import os
import sys
import datetime
import math

def parse_issue_body(body):
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

def generate_terminal_slider(label, value_1_to_10, left_label, right_label):
    """
    Generates a high-density unicode slider with inline labels.
    ACIDITY (Muted vs. Vibrant) ▕▓▓▓▓▓▓░░░░▏
    """
    # Normalize value
    if value_1_to_10 < 1: value_1_to_10 = 1
    if value_1_to_10 > 10: value_1_to_10 = 10
    
    # Bar representation (10 segments)
    filled = '▓' * value_1_to_10
    empty = '░' * (10 - value_1_to_10)
    
    # Combine label with descriptive text
    full_label = f"{label} ({left_label} vs. {right_label})"
    
    # Max label width for padding purposes
    max_label_display_width = 32 
    
    # Ensure a minimum space after label before the bar
    padding_needed = max_label_display_width - len(full_label)
    if padding_needed < 1: padding_needed = 1 # Ensure at least one space
    
    return f"{full_label}{' ' * padding_needed} ▕{filled}{empty}▏"

def generate_terminal_timeline(first, second, strength_count, strength_amt):
    """
    Generates a timeline using box drawing characters, with aligned times.
    """
    pours = [first, second] + [strength_amt] * strength_count
    
    # Calculate times for header
    times = []
    for i in range(len(pours) + 1):
        total_sec = i * 45
        m, s = divmod(total_sec, 60)
        times.append(f"{m}:{s:02d}")
    
    # Generate time row: each time string is centered over a 7-char width
    time_row_parts = []
    for i, t in enumerate(times):
        time_row_parts.append(f"{t:^7}") # Center over 7 chars
    time_row = "".join(time_row_parts)

    segment = "──────" # 6 chars
    bar_row = "├" + "┼".join([segment] * len(pours)) + "┤"
    
    label_row = ""
    for i, amt in enumerate(pours):
        label_row += f"│  P{i+1:<2} "
    label_row += "│"

    vol_row = ""
    for p in pours:
        vol_row += f"│ {int(p):^4}g "
    vol_row += "│"
    
    bottom_row = "└" + "┴".join([segment] * len(pours)) + "┘"
    
    return f"```text\n{time_row}\n{bar_row}\n{label_row}\n{vol_row}\n{bottom_row}\n```"

def generate_markdown(data):
    today = datetime.date.today().strftime('%Y-%m-%d')
    bean = data.get('Bean Name', 'Unknown Bean')
    roaster = data.get('Roaster', 'Unknown Roaster')
    
    # --- Numeric Parsing ---
    try:
        dose = float(data.get('Dose (g)', '20').split()[0])
        water = float(data.get('Total Water (g)', '300').split()[0])
        ratio = round(water / dose, 1)
        
        # 4:6 Logic
        first_pour = float(data.get('First Pour Amount (g)', '60').split()[0])
        phase1_total = water * 0.4
        second_pour = phase1_total - first_pour
        
        phase2_total = water * 0.6
        strength_pours_str = data.get('Strength Pours', '2 Pours').split()[0]
        strength_pours_count = int(strength_pours_str)
        strength_pour_amount = round(phase2_total / strength_pours_count)
        
    except Exception as e:
        dose, water, ratio = 20, 300, 15.0
        first_pour, second_pour = 60, 60
        strength_pours_count = 2
        strength_pour_amount = 90

    # --- Analysis Text ---
    half_p1 = (first_pour + second_pour) / 2
    if first_pour < half_p1:
        balance_text = "SWEETER"
    elif first_pour > half_p1:
        balance_text = "ACIDIC"
    else:
        balance_text = "BALANCED"
        
    if strength_pours_count == 1: strength_text = "LIGHT"
    elif strength_pours_count == 2: strength_text = "MEDIUM"
    else: strength_text = "STRONG"


    # --- Visuals (Terminal Pro) ---
    timeline_block = generate_terminal_timeline(first_pour, second_pour, strength_pours_count, strength_pour_amount)

    # Sensory Sliders
    def parse_score(key):
        try: return int(data.get(key, '5').split()[0])
        except: return 5

    acidity = parse_score('Acidity / Brightness')
    body = parse_score('Body / Texture')
    sweetness = parse_score('Sweetness')
    aftertaste = parse_score('Aftertaste')

    sensory_block = "```text\n"
    sensory_block += generate_terminal_slider("ACIDITY", acidity, "Muted", "Vibrant") + "\n"
    sensory_block += generate_terminal_slider("BODY", body, "Watery", "Syrupy") + "\n"
    sensory_block += generate_terminal_slider("SWEETNESS", sweetness, "Dry", "Candy-like") + "\n"
    sensory_block += generate_terminal_slider("AFTERTASTE", aftertaste, "Short", "Lingering") + "\n"
    sensory_block += "```"
    
    # Convert star rating to numerical
    rating_raw = data.get('Overall Rating', '⭐⭐⭐').strip()
    numerical_rating = f"{rating_raw.count('⭐')}/5"

    md_content = f"""
---
date: {today}
categories:
  - coffee
tags:
  - {roaster}
  - 4-6-method
---

# {today}

!!! abstract "The 4:6 Recipe" 
    **Bean:** {bean}
    **Target:** {balance_text} & {strength_text}

    *   **Ratio:** 1:{ratio} ({dose}g In / {water}g Out)
    *   **Grinder:** {data.get('Grinder & Setting', 'N/A')}
    *   **Temp:** {data.get('Water Temp (°C)', 'N/A')}°C

    **Phase 1 (Balance):** {int(first_pour)}g ➔ {int(second_pour)}g
    **Phase 2 (Strength):** {strength_pours_count} x {int(strength_pour_amount)}g

## Timeline

{timeline_block}

## Analysis

{sensory_block}

**Overall Rating:** {numerical_rating}
"""
    return md_content, bean

def main():
    if len(sys.argv) < 2:
        print("Usage: python process_coffee_log.py <issue_body>")
        sys.exit(1)
        
    issue_body = sys.argv[1]
    data = parse_issue_body(issue_body)
    
    content, bean_name = generate_markdown(data)
    
    today = datetime.date.today().strftime('%Y-%m-%d')
    safe_name = "".join([c for c in bean_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    safe_name = safe_name.replace(' ', '-').lower()
    filename = f"docs/posts/coffee/{today}-{safe_name}.md"
    
    os.makedirs('docs/posts/coffee', exist_ok=True)
    
    with open(filename, 'w') as f:
        f.write(content)
        
    print(f"Created journal entry: {filename}")

if __name__ == "__main__":
    main()
