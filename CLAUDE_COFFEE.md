# Coffee Journal System (IssueOps)

## Overview

An automated coffee brewing journal system built on GitHub Issues. Uses structured forms to capture 4:6 method pour-over data, then generates beautiful markdown posts with Terminal Pro-style visualizations.

**Flow:** GitHub Issue Form → Python Parser → Markdown Post → MkDocs Blog

## System Components

### 1. Issue Template
**File:** `.github/ISSUE_TEMPLATE/coffee_log.yml`

Structured form capturing:
- **Bean Info**: Name, roaster, roast level
- **Recipe**: Dose, water, temperature, grinder setting, pour interval
- **4:6 Method**: Phase 1 (balance), Phase 2 (strength) pour details
- **Sensory**: 1-5 scale ratings for acidity, body, sweetness, aftertaste
- **Notes**: Free-form tasting notes

### 2. GitHub Action Workflow
**File:** `.github/workflows/coffee_journal.yml`

**Trigger:** Issue opened/edited with title starting with `"Brew Log"`

**Process:**
1. Checkout repo
2. Set up Python 3.13.1
3. Run `process_coffee_log.py` with issue body (exits on error)
4. Commit generated markdown to `docs/posts/coffee/` (skips if no changes)
5. Close issue with success message

**Note:** Template auto-sets title to "Brew Log" + adds `coffee-log` label for organization

### 3. Python Parser
**File:** `scripts/process_coffee_log.py`

**Key Functions:**

```python
parse_issue_body()           # Parses ### Field format from GitHub
parse_numeric_field()        # Extracts numbers from "20 (g)" format
generate_terminal_slider()   # Creates ▕▓▓▓░░▏ visualizations
generate_terminal_timeline() # Pour schedule with box-drawing chars
generate_markdown()          # Full post generation
```

**Output:** `docs/posts/coffee/{date}-{bean-name}.md`

## The 4:6 Method

A pour-over technique by Tetsu Kasuya:

- **Phase 1 (40% of water):** Controls **balance**
  - First pour < second pour = SWEETER
  - First pour > second pour = ACIDIC

- **Phase 2 (60% of water):** Controls **strength**
  - 1 pour = LIGHT body
  - 2 pours = MEDIUM body
  - 3 pours = STRONG body

**Example (300g water):**
- Phase 1: 50g + 70g = 120g (40%)
- Phase 2: 60g + 60g + 60g = 180g (60%)

## Generated Post Structure

```markdown
---
date: 2025-12-09
categories:
  - coffee
tags:
  - {roaster}
  - 4-6-method
---

# {date}

!!! abstract "The 4:6 Recipe"
    Bean, roast, grinder, temp details
    Phase 1 & Phase 2 breakdown

## Timeline
```text
0:00   0:45   1:30   2:15   3:00
├──────┼──────┼──────┼──────┼──────┤
│  P1  │  P2  │  P3  │  P4  │  P5  │
│  50g │  70g │  60g │  60g │  60g │
└──────┴──────┴──────┴──────┴──────┘
```

## Analysis
```text
ACIDITY (Muted vs. Vibrant)     ▕▓▓▓░░▏
BODY (Watery vs. Syrupy)        ▕▓▓▓▓░▏
...
```

> "Tasting notes here"

**Overall Rating:** 4/5
```

## Configuration

### Constants (scripts/process_coffee_log.py)

```python
POUR_INTERVAL_SECONDS = 45   # Time between pours
PHASE1_RATIO = 0.4           # 40% for balance
PHASE2_RATIO = 0.6           # 60% for strength
MAX_SLIDER_VALUE = 5         # 1-5 scale for sensory
```

### Required Fields

The script validates these fields on every run:
- `Bean Name`
- `Dose (g)`
- `Total Water (g)`

Missing fields will cause the workflow to fail with an error message.

## Maintenance

### Adding New Sensory Attributes

1. Add dropdown to `.github/ISSUE_TEMPLATE/coffee_log.yml`
2. Parse in `generate_markdown()` using `parse_numeric_field()`
3. Add slider to `sensory_block` with `generate_terminal_slider()`

### Changing Pour Timing

**Per-brew:** Set "Pour Interval (seconds)" in the issue form (defaults to 45s)

**Global default:** Modify `POUR_INTERVAL_SECONDS` constant in script (currently 45s)

### Adjusting Slider Scale

Change `MAX_SLIDER_VALUE` and update template dropdowns to match

## Known Issues

None currently! All previous issues have been resolved:
- ✅ Python version updated to 3.13.1 (matches project requirements)
- ✅ Error handling added (workflow exits on script failure)
- ✅ Empty commit prevention (checks for changes before committing)
- ✅ Bot email uses verified github-actions[bot] identity
- ✅ Roast level is displayed in recipe abstract

## Future Enhancements

- [ ] Add brew time tracking (actual vs. expected)
- [ ] Generate radar charts for sensory profile
- [ ] Support for other brew methods (V60, Aeropress)
- [ ] Historical comparison ("vs. last brew of this bean")
- [ ] Auto-suggest grind adjustment based on taste

## Related Files

- `docs/posts/coffee/4-6-method.md` - Method explainer
- `docs/posts/coffee/` - All generated journal entries
- `.github/workflows/coffee_journal.yml` - Automation workflow
- `.github/ISSUE_TEMPLATE/coffee_log.yml` - Data entry form

---

**Last Updated:** 2025-12-09
**System Version:** 1.0
