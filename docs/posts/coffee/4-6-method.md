---
date: 2025-12-09
categories:
  - coffee
tags:
  - guide
  - 4-6-method
---

# The 4:6 Method Guide

> **"First 40% determines Balance. Last 60% determines Strength."** — Tetsu Kasuya

The method divides total water into two distinct phases. All pours are spaced 45s apart.

## Phase 1: Balance (First 40%)

The relationship between the first two pours determines the flavor profile.

*   **Sweeter:** Pour smaller amount first (e.g., 50g -> 70g).
*   **Acidic:** Pour larger amount first (e.g., 70g -> 50g).
*   **Balanced:** Pour equal amounts (e.g., 60g -> 60g).

## Phase 2: Strength (Last 60%)

The number of pours in the second phase determines the concentration/strength.

*   **Light:** 1 Pour.
*   **Medium:** 2 Pours.
*   **Strong:** 3 Pours.

## Workflow

This lab uses an **IssueOps** workflow to automate journaling.

1.  **Input:** Create a **Coffee Journal Entry** in GitHub Issues.
2.  **Process:** GitHub Actions calculates the brew physics (Sweet vs Acidic, Strength level).
3.  **Output:** A new post is automatically committed to this site with visual charts.

## Data Fields

| Field | Default | Description |
| :--- | :--- | :--- |
| **Dose** | 20g | Coffee bean amount. |
| **Water** | 300g | Total water amount (1:15 ratio). |
| **Temp** | 93°C | Water temperature. |
| **Acidity** | 3/5 | 1=Muted, 3=Balanced, 5=Vibrant. |
| **Body** | 3/5 | 1=Watery, 3=Medium, 5=Syrupy. |
| **Sweetness** | 3/5 | 1=Dry, 3=Medium, 5=Candy-like. |
| **Aftertaste** | 3/5 | 1=Short, 3=Medium, 5=Lingering. |

## Visualization

The system generates "Terminal Pro" block graphics to visualize the data.

**Timeline:**
A left-aligned axis showing the exact timing of each pour.

```text
0:00   0:45   1:30
├──────┼──────┼───
```

**Analysis:**
5-block sliders representing the sensory intensity.

```text
ACIDITY (Muted vs. Vibrant)    ▕▓▓▓░░▏
```