# Focus Skill

Creates a new monthly focus post with proper structure and updates the focus index.

## Steps

1. **Determine month**: Use current month or ask user for specific month
2. **Check if exists**: See if focus post already exists
3. **Create post file**: Generate `docs/posts/focus/YYYY-MM.md` with template
4. **Update index**: Add entry to `docs/focus.md` under the appropriate year
5. **Verify**: Confirm file created and index updated

## Post Template

```markdown
---
draft: false
date: YYYY-MM-01
categories:
  - focus
---

# YYYY/MM

## 🎯 Key Areas

- **Area 1**: Description
- **Area 2**: Description
- **Area 3**: Description

## 📊 Progress

Update this throughout the month...

<!-- more -->

## Notes

Additional thoughts and reflections.
```

## Index Entry Format

Add to `docs/focus.md` under the appropriate year heading:

```markdown
- **YYYY-MM [Month YYYY Focus](posts/focus/YYYY-MM.md)**
```

Month names: January, February, March, April, May, June, July, August, September, October, November, December

## Instructions

1. Ask user if they want to create focus for current month or specify a different month
2. Extract year-month in YYYY-MM format
3. Check if `docs/posts/focus/YYYY-MM.md` exists
   - If exists, ask if they want to open it or overwrite
   - If not, proceed to create
4. Create the focus post file with proper frontmatter and template
5. Read `docs/focus.md` to understand current structure
6. Determine the year section (e.g., "### 2025")
   - If year section doesn't exist, create it
7. Add the new entry as the FIRST item under that year section
8. Report success and provide link to the created file

## Important Notes

- Always use current month by default for convenience
- Keep year sections in reverse chronological order (newest first)
- Entries within each year should also be newest first (December before January)
- Use interactive prompts to confirm actions
- The title in the markdown file should use forward slashes (YYYY/MM)
- The frontmatter date should always be the first day of the month (YYYY-MM-01)
- Extract proper month name for the index entry
