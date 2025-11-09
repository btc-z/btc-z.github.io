# MkDocs Material Blog Template

A cookiecutter template for creating a beautiful personal blog with MkDocs Material.

## Features

- **Modern Material Design** theme with light/dark mode
- **Blog plugin** with date-based URLs
- **Rich markdown** support (emoji, math, diagrams, admonitions)
- **Automatic deployment** to GitHub Pages via GitHub Actions
- **Git-based timestamps** showing post creation/modification dates
- **Google Analytics** integration (optional)
- **Custom domain** support
- **Bilingual** content support
- Sample posts included for reference

## Prerequisites

- Python 3.13 or higher
- [Cookiecutter](https://cookiecutter.readthedocs.io/)
- [Poetry](https://python-poetry.org/) (will be installed in the generated project)
- Git

## Quick Start

### 1. Install Cookiecutter

```bash
pip install cookiecutter
# or
pipx install cookiecutter
```

### 2. Generate Your Blog

```bash
cookiecutter /path/to/mkdocs-blog-template
```

You'll be prompted to enter:
- **full_name**: Your full name (e.g., "Jane Doe")
- **email**: Your email address
- **github_username**: Your GitHub username
- **project_name**: Name of your blog (e.g., "My Blog")
- **site_name**: Display name for your site
- **site_description**: Brief description of your blog
- **domain_name**: Your custom domain (if you have one)
- **use_custom_domain**: Whether to use a custom domain (yes/no)
- **use_analytics**: Whether to set up Google Analytics (yes/no)
- **google_analytics_id**: Your Google Analytics tracking ID (if enabled)
- **primary_color**: Theme color (lime, indigo, purple, etc.)
- **python_version**: Python version to use (default: 3.13)

### 3. Navigate to Your New Blog

```bash
cd <project_slug>  # The name will be based on your project_name
```

### 4. Install Dependencies

```bash
poetry install
```

### 5. Start Local Development Server

```bash
poetry shell
make serve
```

Visit `http://127.0.0.1:8000/` to see your blog!

## What's Included

### Directory Structure

```
your-blog/
├── .github/
│   └── workflows/
│       └── cicd.yml          # Auto-deployment to GitHub Pages
├── docs/
│   ├── assets/               # Images and media
│   ├── javascripts/
│   │   └── mathjax.js        # Math rendering configuration
│   ├── posts/
│   │   ├── reflections/
│   │   │   └── welcome.md    # Sample reflection post
│   │   └── books/
│   │       └── sample-book-review.md  # Sample book review
│   ├── index.md              # Homepage
│   └── CNAME                 # Custom domain (if enabled)
├── mkdocs.yml                # Site configuration
├── pyproject.toml            # Python dependencies
├── Makefile                  # Helpful commands
├── .gitignore               # Git ignore rules
└── README.md                 # Your blog's README
```

### Sample Content

The template includes two sample posts to help you get started:
1. **Welcome post** - Demonstrates various markdown features
2. **Sample book review** - Template for book reviews

Feel free to delete or modify these!

## Deployment to GitHub Pages

GitHub Pages is free web hosting for your blog!

### Quick Setup

1. **Create repository:** `yourusername.github.io` on GitHub (must be public)
2. **Push code:** `git init && git add . && git commit -m "Initial commit" && git push`
3. **Configure Pages:** Settings → Pages → Deploy from `gh-pages` branch
4. **Done!** Your blog is live at `https://yourusername.github.io/`

### Detailed Instructions

See **[GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)** for a complete visual walkthrough including:
- Repository naming requirements
- Step-by-step GitHub Pages configuration
- Troubleshooting common issues
- Understanding automatic deployments

**Important:** The repository MUST be named `yourusername.github.io` (replace with your actual GitHub username) for the URL to work correctly

## Customization

Everything is customizable! The generated README.md in your blog includes detailed instructions for:

- Adding new posts
- Changing theme colors
- Updating the logo
- Adding custom CSS/JavaScript
- Setting up Google Analytics
- Configuring a custom domain
- And much more!

## Available Features

### Markdown Extensions
- **Emojis**: `:smile:` → 😊
- **Math**: `$E=mc^2$` → Mathematical notation
- **Mermaid diagrams**: For flowcharts and diagrams
- **Admonitions**: Callout boxes for notes, tips, warnings
- **Footnotes**: Add references and citations
- **Code highlighting**: Syntax highlighting for 200+ languages

### Blog Features
- Date-based URLs (`/posts/2024/01/15/post-title`)
- Automatic post listing
- Git-based timestamps ("2 days ago" format)
- Draft posts (set `draft: true` in frontmatter)
- Categories/tags

### Theme Features
- Light/dark mode toggle
- Responsive design
- Search functionality
- Table of contents
- Smooth scrolling
- Syntax highlighting

## Tips

1. **Start with the samples**: Modify the sample posts to understand the structure
2. **Use frontmatter**: Always include date and categories in your posts
3. **Preview locally**: Always run `make serve` to preview before pushing
4. **Commit regularly**: Push small changes frequently
5. **Check the docs**: MkDocs Material has excellent [documentation](https://squidfunk.github.io/mkdocs-material/)

## Troubleshooting

### Cookiecutter not found
```bash
pip install --user cookiecutter
# or
pipx install cookiecutter
```

### Poetry not installed
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Python version issues
Make sure you have Python 3.13+ installed:
```bash
python --version
```

## Contributing

Found a bug or have a suggestion? Contributions are welcome!

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## License

This template is open source and free to use for your personal or commercial projects.

---

Happy blogging! ✨
