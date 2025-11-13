# CLAUDE.md

## Project Overview

Personal blog built with MkDocs Material, deployed to GitHub Pages at **zihan.us**. The repository contains:
1. Main blog content (root level)
2. Cookiecutter template for creating similar blogs (`mkdocs-blog-template/`)

## Working Together

**Interaction Style:**
- Keep answers concise and direct - break responses >25 lines into chunks
- Use interactive prompts (AskUserQuestion tool) for natural dialog and follow-ups
- Challenge big assumptions - push back if something doesn't seem right
- Proactively ask questions when information is incomplete rather than making assumptions
- Build collaboratively, not just execute orders

## Development Commands

```bash
poetry install          # Install dependencies (first time)
poetry env activate     # Activate virtual environment
make serve             # Start dev server at http://127.0.0.1:8000/
```

**Deployment**: Automated via GitHub Actions. Push to `main` triggers deployment to GitHub Pages.

## Blog Structure

Posts are organized in **category-based folders** under `docs/posts/`:

```
docs/
├── index.md              # Homepage with curated post index
├── CNAME                 # Custom domain: zihan.us
├── assets/               # Images and media
├── javascripts/mathjax.js
└── posts/
    ├── reflections/     # 生活感悟
    └── books/           # 读书笔记
```

## Post Workflow

1. **Create post**: Add markdown file to `docs/posts/reflections/` or `docs/posts/books/`
2. **Frontmatter**: Include YAML with `draft`, `date`, and `categories`
3. **Update homepage**: Manually add entry to `docs/index.md` with emoji, date, and link
4. **Preview**: Run `make serve` to test locally
5. **Deploy**: Commit and push to `main` - GitHub Actions handles the rest

### URL Format
- **File location**: `docs/posts/reflections/post-name.md`
- **Generated URL**: `/posts/2024/11/01/post-title` (based on `date` in frontmatter)
- Configured via `post_url_date_format: yyyy/MM/dd` in mkdocs.yml

**Blog plugin docs**: https://squidfunk.github.io/mkdocs-material/plugins/blog/

## Key Configuration

### mkdocs.yml
- Date-based URLs, redirects plugin (`posts/index.md` → `index.md`)
- Markdown extensions: emoji, MathJax, mermaid, admonitions
- Custom fonts disabled to use CSS-configured fonts (see FONT.md)

### pyproject.toml
- Python ^3.13.1, Poetry package manager
- Dependencies: mkdocs-material, git-revision-date plugin, redirects, cookiecutter

### Fonts & Typography
See **[FONT.md](FONT.md)** for complete font configuration guide including:
- Current font choices (Ma Shan Zheng for Chinese, Lora for English)
- How to change fonts
- Popular alternatives
- Troubleshooting tips

### Language Support
Blog supports both Chinese and English content natively (UTF-8). No special configuration needed.

## Commit Convention

Follow pattern: `type: description`
- Examples: `post: 理想的生活`, `chore: update note`, `feat: add feature`
- **NEVER include Claude Code credit/disclaimer** in commit messages
