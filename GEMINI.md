# GEMINI.md

## Project Overview

**zlab** is a personal blog and knowledge base built with **MkDocs Material**, hosted on GitHub Pages at [zihan.us](https://zihan.us). It features a category-based structure for posts (Reflections, Books), supports bilingual content (Chinese/English), and utilizes modern documentation features like MathJax, Mermaid diagrams, and Admonitions.

The repository also includes a `mkdocs-blog-template` directory, which is a Cookiecutter template for scaffolding similar blog projects.

## Technology Stack

*   **Static Site Generator:** [MkDocs](https://www.mkdocs.org/) with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.
*   **Language:** Python 3.13.1+
*   **Package Manager:** [Poetry](https://python-poetry.org/)
*   **Deployment:** GitHub Actions (CI/CD) -> GitHub Pages
*   **Search:** Built-in client-side search (lunr.js)
*   **Analytics:** Google Analytics (configured in `mkdocs.yml`)

## Directory Structure

```
/
├── docs/                 # Source documentation & content
│   ├── index.md          # Homepage (manually curated index)
│   ├── posts/            # Blog posts categorized by folders
│   │   ├── books/        # Book reviews
│   │   └── reflections/  # Life reflections
│   ├── assets/           # Static assets (images, etc.)
│   └── javascripts/      # Custom JS (e.g., MathJax config)
├── mkdocs-blog-template/ # Cookiecutter template for new blogs
├── mkdocs.yml            # Main MkDocs configuration
├── pyproject.toml        # Python dependencies (Poetry)
├── Makefile              # Build shortcuts
└── .github/workflows/    # CI/CD pipelines
```

## Development Workflow

### Prerequisites

*   Python 3.13+
*   Poetry (`pip install poetry`)

### Setup & Installation

1.  **Install dependencies:**
    ```bash
    poetry install
    ```
2.  **Activate virtual environment:**
    ```bash
    poetry shell
    ```

### Running Locally

*   **Start the dev server:**
    ```bash
    make serve
    # OR directly: poetry run mkdocs serve
    ```
    Access the site at `http://127.0.0.1:8000/`.

### Adding Content

1.  **Create a new post** in `docs/posts/<category>/<filename>.md`.
2.  **Add Frontmatter** (Recommended):
    ```yaml
    ---
    draft: false
    date: 2025-12-09
    categories:
        - reflections
    ---
    ```
3.  **Update Homepage:** Manually add a link to the new post in `docs/index.md`.
    ```markdown
    - **2025-12-09 :coffee: [Post Title](posts/reflections/filename.md)**
    ```

## Configuration & Customization

*   **`mkdocs.yml`**: Controls site metadata, theme settings, plugins (blog, search, redirects), and markdown extensions.
*   **`FONT.md`**: Guide for customizing fonts (currently uses Ma Shan Zheng and Lora).
*   **Extensions**:
    *   **Math**: `$E=mc^2$`
    *   **Mermaid**: ` ```mermaid `
    *   **Emojis**: `:smile:`
    *   **Admonitions**: `!!! note "Title"`

## Deployment

Deployment is automated via GitHub Actions. Pushing changes to the `main` branch triggers the `cicd.yml` workflow, which builds the site and deploys it to the `gh-pages` branch.

## Commit Conventions

Use conventional commit messages: `type: description`
*   `post: New article on Life`
*   `fix: typo in about page`
*   `chore: update dependencies`
