---
description: Quick daily post for 短期 or 长期
---

Create dated post and update index. Usage: `/write` or `/write s` (短期) or `/write l` (长期).

**Steps:**
1. Parse argument: `s` = 短期 (default), `l` = 长期
2. Use today's date (YYYY-MM-DD)
3. Create an empty  file `docs/posts/{category}/YYYY-MM-DD.md` with a single line:
   - `# MM月DD日`
4. Update `docs/{category}.md` - add to top of month section:
   - Format: `- **[YYYY-MM-DD](posts/{category}/YYYY-MM-DD.md)**`
   - Under: `### YYYY年MM月`
   - Create month heading if needed
5. Done

**No prompts** - just create and link.
