import os
import sys
import datetime
import math
import textwrap

def parse_issue_body(body):
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

def generate_svg_radar(acidity, body, sweetness, aftertaste, rating):
    """
    Generates a 5-axis SVG Radar Chart.
    Values are 1-10. Rating (1-5) will be doubled to map to 1-10.
    """
    size = 300
    center = size / 2
    # Reduced radius to prevent label cutoff
    radius = 80 
    
    # 5 Metrics
    metrics = [
        ('Acidity', acidity),
        ('Body', body),
        ('Sweetness', sweetness),
        ('Aftertaste', aftertaste),
        ('Overall', rating * 2) # Normalize 5-star to 10-point
    ]
    
    # Calculate Points
    points = []
    axis_lines = ""
    label_text = ""
    
    angle_step = (2 * math.pi) / 5
    # Start at top (negative PI/2)
    start_angle = -math.pi / 2
    
    for i, (name, value) in enumerate(metrics):
        angle = start_angle + (i * angle_step)
        
        # Point for the value polygon
        val_radius = (value / 10.0) * radius
        x = center + val_radius * math.cos(angle)
        y = center + val_radius * math.sin(angle)
        points.append(f"{x:.1f},{y:.1f}")
        
        # Axis Line (Background)
        ax_x = center + radius * math.cos(angle)
        ax_y = center + radius * math.sin(angle)
        axis_lines += f'<line x1="{center}" y1="{center}" x2="{ax_x}" y2="{ax_y}" stroke="#444" stroke-width="1" />'
        
        # Axis Labels
        # Push label out a bit (radius + 20)
        lbl_x = center + (radius + 20) * math.cos(angle)
        lbl_y = center + (radius + 20) * math.sin(angle)
        
        # Adjust text anchor based on position
        anchor = "middle"
        if lbl_x < center - 10: anchor = "end"
        if lbl_x > center + 10: anchor = "start"
        
        # Adjust baseline
        baseline = "middle"
        if lbl_y < center - 10: baseline = "auto" # Top
        if lbl_y > center + 10: baseline = "hanging" # Bottom
        
        label_text += f'<text x="{lbl_x:.1f}" y="{lbl_y:.1f}" text-anchor="{anchor}" dominant-baseline="{baseline}" fill="#888" font-size="12" font-family="sans-serif">{name}</text>'

    # Polygon String
    poly_points = " ".join(points)
    
    # Background Grid (Pentagons at 2, 4, 6, 8, 10)
    grid_polys = ""
    for r in [0.2, 0.4, 0.6, 0.8, 1.0]:
        gp = []
        for i in range(5):
            angle = start_angle + (i * angle_step)
            gx = center + (radius * r) * math.cos(angle)
            gy = center + (radius * r) * math.sin(angle)
            gp.append(f"{gx:.1f},{gy:.1f}")
        grid_polys += f'<polygon points="{" ".join(gp)}" fill="none" stroke="#333" stroke-width="1" />'

    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="100%" height="auto" style="max-width:400px; display:block; margin: 0 auto; background-color: transparent;">
        <!-- Background Grid -->
        {grid_polys}
        <!-- Axis Lines -->
        {axis_lines}
        <!-- Data Polygon -->
        <polygon points="{poly_points}" fill="rgba(0, 188, 212, 0.2)" stroke="#00BCD4" stroke-width="2" />
        <circle cx="{center}" cy="{center}" r="2" fill="#00BCD4" />
        <!-- Labels -->
        {label_text}
    </svg>
    "
    return textwrap.dedent(svg).strip()

def generate_svg_step_chart(pours):
    """
    Generates a step chart for the pour profile.
    Pours is a list of dicts: [{'amount': 60, 'time': 45}, ...] 
    """
    width = 600
    height = 200
    margin_left = 40
    margin_bottom = 30
    margin_top = 20
    margin_right = 20
    
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_bottom - margin_top
    
    # Calculate Max Values for Scaling
    total_water = sum(p['amount'] for p in pours)
    max_time = len(pours) * 45 + 15 # Add buffer
    
    def get_x(sec):
        return margin_left + (sec / max_time) * plot_w
        
    def get_y(vol):
        # Y is inverted in SVG (0 is top)
        # vol 0 -> plot_h + margin_top
        # vol max -> margin_top
        pct = vol / (total_water * 1.1) # 10% headroom
        return margin_top + plot_h - (pct * plot_h)

    path_d = f"M {get_x(0)} {get_y(0)}"
    
    current_time = 0
    current_vol = 0
    
    pour_labels = ""
    
    # 45s interval standard
    # Simulate pour: take 10s to pour
    pour_duration = 10
    interval = 45
    
    for i, pour in enumerate(pours):
        amt = pour['amount']
        
        # Start Pour
        path_d += f" L {get_x(current_time)} {get_y(current_vol)}"
        
        # End Pour (Volume up)
        current_vol += amt
        path_d += f" L {get_x(current_time + pour_duration)} {get_y(current_vol)}"
        
        # Drawdown (Flat volume until next interval)
        next_time = (i + 1) * interval
        current_time = next_time
        path_d += f" L {get_x(current_time)} {get_y(current_vol)}"
        
        # Label (P1, P2...)
        # Center label in the flat part
        label_x = get_x((i * interval) + interval/2 + 5)
        label_y = get_y(current_vol) - 10
        pour_labels += f'<text x="{label_x}" y="{label_y}" font-size="10" fill="#888" text-anchor="middle">P{i+1}</text>'
        
        # Volume Label underneath
        pour_labels += f'<text x="{label_x}" y="{get_y(current_vol) + 15}" font-size="9" fill="#555" text-anchor="middle">{int(amt)}g</text>'

    # Axis Lines
    axes = f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#555" stroke-width="1"/>'
    axes += f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#555" stroke-width="1"/>'

    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="display:block; background-color: transparent;">
        <!-- Axes -->
        {axes}
        <!-- Graph Line -->
        <path d="{path_d}" fill="none" stroke="#E91E63" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Labels -->
        {pour_labels}
    </svg>
    ""
    return textwrap.dedent(svg).strip()

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
        # Fallback defaults
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


    # --- SVG Visuals ---
    
    # 1. Step Chart Data
    pours = [{'amount': first_pour}, {'amount': second_pour}]
    for _ in range(strength_pours_count):
        pours.append({'amount': strength_pour_amount})
    
    step_svg = generate_svg_step_chart(pours)

    # 2. Radar Chart Data
    # Parse fields, defaulting to 5 if missing/error
    def parse_score(key):
        try:
            return int(data.get(key, '5').split()[0])
        except:
            return 5
            
    acidity = parse_score('Acidity / Brightness')
    body = parse_score('Body / Texture')
    sweetness = parse_score('Sweetness')
    aftertaste = parse_score('Aftertaste')
    
    # Rating is usually "⭐⭐⭐" (len 3)
    rating_raw = data.get('Overall Rating', '⭐⭐⭐').strip()
    rating_val = rating_raw.count('⭐')
    if rating_val == 0: rating_val = 3
    
    radar_svg = generate_svg_radar(acidity, body, sweetness, aftertaste, rating_val)

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

## ⏱️ The Pour

{step_svg}

## 🧪 Sensory Analysis

> "{data.get('Tasting Notes', 'No notes provided.')}"

<div style="width: 100%; display: flex; justify-content: center;">
{radar_svg}
</div>

**Overall Rating:** {rating_raw}
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
