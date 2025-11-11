# CLAUDE.md

## Project Overview

This is a personal blog built with MkDocs Material, deployed to GitHub Pages at **zihan.us**. The repository serves two purposes:
1. The main blog content (root level)
2. A cookiecutter template for creating similar blogs (`mkdocs-blog-template/`)

## Development Commands

### Local Development
```bash
poetry install             # Install dependencies (first time setup)
poetry env activate        # Activate virtual environment
make serve                 # Start development server at http://127.0.0.1:8000/
```

### Deployment
Deployment is fully automated via GitHub Actions. Pushing to `main` branch triggers `.github/workflows/cicd.yml` which:
- Installs dependencies (mkdocs-material, mkdocs-git-revision-date-localized-plugin, mkdocs-redirects)
- Runs `mkdocs gh-deploy --force` to deploy to GitHub Pages

## Architecture

### Blog Structure
The blog uses MkDocs Material with the blog plugin. Posts are organized in a **category-based structure** under `docs/posts/`:

```
docs/
├── index.md              # Homepage with curated post index
├── CNAME                 # Custom domain: zihan.us
├── assets/               # Images and media
│   └── vipassana/
├── javascripts/          # Custom JavaScript
│   └── mathjax.js       # Math rendering configuration
└── posts/                # Blog posts
    ├── reflections/     # 生活感悟
    └── books/           # 读书笔记
```

### Post Workflow
1. **Create post**: Add markdown file to `docs/posts/reflections/` or `docs/posts/books/`
2. **Frontmatter**: Include YAML frontmatter with `draft`, `date`, and `categories`
3. **Update homepage**: Manually add entry to `docs/index.md` with emoji, date, and link
4. **Preview**: Run `make serve` to test locally
5. **Deploy**: Commit and push to `main` - GitHub Actions handles deployment

### Post File Structure vs URL Format
- **File structure**: Posts stored in category folders: `docs/posts/reflections/post-name.md` or `docs/posts/books/post-name.md`
- **Generated URLs**: Blog plugin generates date-based URLs like `/posts/2024/11/01/post-title` based on the `date` field in frontmatter (configured via `post_url_date_format: yyyy/MM/dd` in mkdocs.yml)

**Blog plugin documentation**: https://squidfunk.github.io/mkdocs-material/plugins/blog/

### Homepage vs Blog Index
- `docs/index.md`: Manual homepage with curated post listings using emojis and dates
- `docs/posts/index.md`: Auto-redirects to homepage (via redirects plugin)

## Key Configuration

### mkdocs.yml
- **Blog plugin**: Date-based URLs (`post_url_date_format: yyyy/MM/dd`), `blog_dir: posts`, archive disabled
- **Redirects plugin**: Routes `posts/index.md` → `index.md`
- **Git revision date plugin**: Shows "timeago" format timestamps (e.g., "2 days ago")
- **Theme**: Material with Roboto Mono font, lime primary color, light/dark mode toggle
- **Analytics**: Google Analytics enabled (G-X956BD08NG)
- **Markdown extensions**: emoji, math (MathJax), mermaid diagrams, admonitions, footnotes

### pyproject.toml
- Python version: `^3.13.1`
- Package manager: Poetry
- Dependencies: mkdocs-material, mkdocs-git-revision-date-localized-plugin, mkdocs-redirects, cookiecutter

### MathJax Configuration
Math rendering is configured via `docs/javascripts/mathjax.js` and loaded from CDN (unpkg.com)

## Cookiecutter Template

The `mkdocs-blog-template/` directory contains a cookiecutter template for generating new blogs with similar structure. Key files:
- `cookiecutter.json`: Template variables
- `{{cookiecutter.project_slug}}/`: Template directory structure
- Multiple documentation files (QUICKSTART.md, USAGE_GUIDE.md, etc.) explaining template usage

## Language Support

The blog is primarily in Chinese with bilingual support for post content:
- Posts can be written in Chinese, English, or a mix of both languages
- No special configuration needed - UTF-8 natively supports both languages
- Example: `docs/posts/reflections/理想的生活.md` (Chinese) and `docs/posts/books/alchemist.md` (mixed content)

## Custom Domain

The `docs/CNAME` file contains `zihan.us` for GitHub Pages custom domain routing.

## Commit Convention

Based on git history, commits follow pattern: `type: description`
- Examples: `post: 理想的生活`, `chore: update note to readers`, `cookiecutter`
