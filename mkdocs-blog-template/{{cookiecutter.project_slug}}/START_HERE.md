# ⭐ START HERE - Your New Blog!

Congratulations! You've generated your blog. Here's what to do next:

## 🎯 Your Mission

Get your blog running locally, then deploy it to the internet!

---

## ✅ Step 1: Local Setup (5 minutes)

### Install Dependencies

```bash
# Make sure you're in this directory
pwd  # Should show: .../{{ cookiecutter.project_slug }}

# Install dependencies
poetry install
```

**First time using Poetry?** Install it:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Run Your Blog Locally

```bash
# Start the poetry environment
poetry shell

# Start local server
make serve
```

**Open browser:** http://127.0.0.1:8000/

🎉 **Your blog is running!** Press `Ctrl+C` to stop.

---

## 🌐 Step 2: Deploy to GitHub Pages (5 minutes)

**Your blog will be live at:** https://{{ cookiecutter.github_username }}.github.io/

### Quick Steps:

1. Create GitHub repo named: `{{ cookiecutter.github_username }}.github.io` (must be **Public**)
2. Push your code
3. Configure GitHub Pages to use `gh-pages` branch
4. Wait 2-3 minutes
5. Visit your live blog!

### Detailed Instructions:

**👉 See `DEPLOY_TO_GITHUB_PAGES.md` for complete step-by-step guide!**

---

## 📝 Step 3: Write Your First Post

### Delete Sample Posts

```bash
rm docs/posts/reflections/welcome.md
rm docs/posts/books/sample-book-review.md
```

### Create Your First Post

Create file: `docs/posts/reflections/my-first-post.md`

```yaml
---
draft: false
date: 2024-01-15
categories:
    - reflections
---

# My First Post

This is my first blog post!

## What I'll Write About

- My thoughts and reflections
- Books I'm reading
- Things I'm learning

Stay tuned!
```

### Update Homepage

Edit `docs/index.md` and add:

```markdown
### :ocean: Reflections

- **2024-01-15 :sparkles: [My First Post](posts/reflections/my-first-post.md)**
```

### Preview & Publish

```bash
# Preview locally
make serve

# Commit and push
git add .
git commit -m "post: My first post"
git push

# Wait 2-3 minutes - live on your site!
```

---

## 📚 Important Files

- **`docs/index.md`** - Your homepage (edit this!)
- **`docs/posts/`** - Put all blog posts here
- **`mkdocs.yml`** - Site configuration
- **`README.md`** - Complete documentation
- **`DEPLOY_TO_GITHUB_PAGES.md`** - Deployment guide

---

## 🎨 Customization

### Change Site Name/Logo

Edit `mkdocs.yml`:
```yaml
site_name: {{ cookiecutter.site_name }}  # Change this
theme:
  logo: assets/your-logo.png  # Add your logo
```

### Change Theme Color

Edit `mkdocs.yml`:
```yaml
palette:
  primary: {{ cookiecutter.primary_color }}  # Try: indigo, purple, pink, blue, etc.
```

### Add Google Analytics

Edit `mkdocs.yml` and uncomment the analytics section (if not already enabled).

---

## 🆘 Need Help?

### For Deployment Issues
📖 Read: `DEPLOY_TO_GITHUB_PAGES.md`

### For General Questions
📖 Read: `README.md`

### For Markdown Features
📖 Look at the sample posts you deleted (check git history)

### External Resources
- [MkDocs Material Docs](https://squidfunk.github.io/mkdocs-material/)
- [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet)
- [Markdown Guide](https://www.markdownguide.org/)

---

## ✨ Quick Commands Reference

```bash
# Start local server
poetry shell
make serve

# Build site
make build

# Add & commit changes
git add .
git commit -m "your message"
git push

# Exit poetry shell
exit
```

---

## 🎊 Next Steps

1. ✅ Run blog locally (Step 1)
2. ✅ Deploy to GitHub Pages (Step 2)
3. ✅ Write your first post (Step 3)
4. 🎨 Customize your blog
5. 📝 Keep writing!

**Your blog URL:** https://{{ cookiecutter.github_username }}.github.io/

---

## 🚀 You're All Set!

Everything you need is in this directory. Follow the steps above and you'll have a live blog in 10 minutes!

**Questions?** Check the documentation files or the resources listed above.

Happy blogging! 📚✨
