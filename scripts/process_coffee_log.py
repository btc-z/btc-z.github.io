import os
import sys
import datetime
import re

def parse_issue_body(body):
    """
    Parses the Markdown body of the issue form.
    """
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
        else:
            if line:
                current_value.append(line)
            
    if current_key:
        data[current_key] = '\n'.join(current_value).strip()
        
    return data

def generate_ascii_timeline(first, second, strength_count, strength_amt):
    """
    Generates an ASCII timeline for the 5 pours.
    Assumes standard 45s intervals.
    """
    # 5 steps total
    pours = [first, second] + [strength_amt] * strength_count
    
    # Header Time
    # 0:00   0:45   1:30   2:15   3:00   3:45 (if 5 pours)
    timeline =  "0:00   0:45   1:30   2:15   3:00   3:45\n"
    timeline += "|------|------|------|------|------|\n"
    
    # Boxes
    # [  P1  ][  P2  ][  P3  ][  P4  ][  P5  ]
    row_boxes = ""
    row_vals = ""
    
    for i, amt in enumerate(pours):
        pour_num = i + 1
        row_boxes += f"[  P{pour_num}  ]"
        
        # Center the gram amount: "( 60g  )"
        val_str = f" {int(amt)}g "
        row_vals += f"({val_str:^6})"
        
    return f"```text\n{timeline}{row_boxes}\n{row_vals}\n```"

def generate_ascii_slider(label, value_1_to_10, left_label, right_label):
    """
    Generates: LABEL: [Left......X.......Right]
    """
    bar_length = 20
    # Map 1-10 to 0-19 index
    if value_1_to_10 < 1: value_1_to_10 = 1
    if value_1_to_10 > 10: value_1_to_10 = 10
    
    pos = int((value_1_to_10 - 1) * (bar_length - 1) / 9)
    
    chars = ['.'] * bar_length
    chars[pos] = 'X'
    bar = "".join(chars)
    
    # Format: LABEL   [.....X.....]
    #         Left                Right
    
    return f"{label:<10} [{bar}]\n{'':<11}{left_label:<10}{right_label:>11}"

def generate_markdown(data):
    today = datetime.date.today().strftime('%Y-%m-%d')
    bean = data.get('Bean Name', 'Unknown Bean')
    roaster = data.get('Roaster', 'Unknown Roaster')
    brewer = 'V60'
    
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


    # --- ASCII Visuals ---
    timeline_ascii = generate_ascii_timeline(first_pour, second_pour, strength_pours_count, strength_pour_amount)

    # Sliders
    acidity_raw = data.get('Acidity / Brightness', '5').split()[0]
    body_raw = data.get('Body / Texture', '5').split()[0]
    
    try:
        acidity_val = int(acidity_raw)
        body_val = int(body_raw)
    except:
        acidity_val, body_val = 5, 5
        
    slider_block = "```text\n"
    slider_block += generate_ascii_slider("ACIDITY", acidity_val, "Muted", "Vibrant") + "\n\n"
    slider_block += generate_ascii_slider("BODY", body_val, "Tea-like", "Syrupy") + "\n"
    slider_block += "```"

    md_content = f"""
---
date: {today}
categories:
  - coffee
tags:
  - {roaster}
  - 4-6-method
---

# ☕ {bean}

!!! abstract "The 4:6 Recipe" 
    **Target:** {balance_text} & {strength_text}

    *   **Ratio:** 1:{ratio} ({dose}g In / {water}g Out)
    *   **Grinder:** {data.get('Grinder & Setting', 'N/A')}
    *   **Temp:** {data.get('Water Temp (°C)', 'N/A')}°C

    **Phase 1 (Balance):** {int(first_pour)}g ➔ {int(second_pour)}g
    **Phase 2 (Strength):** {strength_pours_count} x {int(strength_pour_amount)}g

## ⏱️ The Method

{timeline_ascii}

## 🧪 Sensory Analysis

> "{data.get('Tasting Notes', 'No notes provided.')}"

{slider_block}

**Overall Rating:** {data.get('Overall Rating', '⭐⭐⭐')}
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
