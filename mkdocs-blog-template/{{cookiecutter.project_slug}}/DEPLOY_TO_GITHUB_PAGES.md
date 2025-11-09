# 🚀 Deploy Your Blog to GitHub Pages

Follow these steps **exactly** to make your blog live at `https://{{ cookiecutter.github_username }}.github.io/`

## ⚠️ CRITICAL REQUIREMENT

Your GitHub repository **MUST** be named: `{{ cookiecutter.github_username }}.github.io`

If you use a different name, your URL will be different!

---

## Step 1: Create GitHub Repository (2 minutes)

1. **Go to:** https://github.com/new

2. **Fill in:**
   - **Repository name:** `{{ cookiecutter.github_username }}.github.io` ← Copy this exactly!
   - **Description:** (optional) "{{ cookiecutter.site_description }}"
   - **Public** ← MUST be checked (required for free GitHub Pages)

3. **DO NOT check these boxes:**
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license

4. **Click** "Create repository"

---

## Step 2: Push Your Blog to GitHub (1 minute)

Open your terminal in this directory and run these commands **one by one**:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create your first commit
git commit -m "Initial commit: {{ cookiecutter.site_name }}"

# Set main as the default branch
git branch -M main

# Connect to your GitHub repository
git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_username }}.github.io.git

# Push to GitHub
git push -u origin main
```

✅ You should see the upload complete successfully!

---

## Step 3: Wait for Automatic Build (2 minutes)

1. **Go to your repository on GitHub:**
   https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_username }}.github.io

2. **Click the "Actions" tab** (top menu)

3. **Watch the workflow run**
   - You'll see: "Deploy MkDocs to GitHub Pages"
   - Wait for the **green checkmark ✅** (about 1-2 minutes)
   - If you see a **red X ❌**, click it to see what went wrong

**What's happening:** GitHub is automatically building your blog and creating a `gh-pages` branch.

---

## Step 4: Enable GitHub Pages (1 minute)

1. **Go to Settings:**
   Click "Settings" tab → Click "Pages" in left sidebar

2. **Configure deployment:**
   - **Source:** Select "Deploy from a branch"
   - **Branch:** Select **`gh-pages`** (NOT main!)
   - **Folder:** Select **`/ (root)`**

3. **Click "Save"**

4. **Look for this message:**
   ```
   ✓ Your site is live at https://{{ cookiecutter.github_username }}.github.io/
   ```

---

## Step 5: Visit Your Live Blog! (1 minute)

**Open your browser and go to:**

🌐 **https://{{ cookiecutter.github_username }}.github.io/**

🎉 **Your blog is now live on the internet!**

**Note:** First deployment can take up to 10 minutes. If you see a 404 error, wait a few minutes and refresh.

---

## 🎯 Quick Checklist

- [ ] Created repository: `{{ cookiecutter.github_username }}.github.io`
- [ ] Repository is **Public**
- [ ] Ran all git commands successfully
- [ ] GitHub Actions workflow completed with green ✅
- [ ] Configured Pages to use **`gh-pages`** branch (not main!)
- [ ] Saw "Your site is live" message
- [ ] Can access blog at https://{{ cookiecutter.github_username }}.github.io/

---

## 📝 Future Updates (After Initial Setup)

Every time you want to publish new posts:

```bash
# 1. Create/edit posts in docs/posts/

# 2. Test locally
make serve

# 3. Commit and push
git add .
git commit -m "post: My new post title"
git push

# 4. Wait 2-3 minutes - your site updates automatically!
```

No need to repeat the setup steps above!

---

## ❌ Common Problems

### "gh-pages branch not showing in dropdown"
**Solution:** Wait for GitHub Actions to complete (check Actions tab), then refresh the Pages settings.

### "404 Page not found"
**Solutions:**
- Wait up to 10 minutes for first deployment
- Verify you selected `gh-pages` branch (not `main`)
- Make sure repository is Public
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

### "Workflow failed (red X)"
**Solution:**
- Click on the failed workflow in Actions tab
- Read the error message
- Most common: Check `mkdocs.yml` for syntax errors

### "Site has no styling/looks broken"
**Solution:**
- Make sure repository name is exactly `{{ cookiecutter.github_username }}.github.io`
- If using different name, add to `mkdocs.yml`:
  ```yaml
  site_url: https://{{ cookiecutter.github_username }}.github.io/repo-name/
  ```

---

## 🆘 Need More Help?

- **Detailed guide:** See `GITHUB_PAGES_SETUP.md` in the template
- **GitHub Pages docs:** https://docs.github.com/en/pages
- **MkDocs Material:** https://squidfunk.github.io/mkdocs-material/

---

## 🎊 Congratulations!

Your blog is now:
- ✅ Live on the internet
- ✅ Automatically deployed when you push changes
- ✅ Hosted for free on GitHub Pages
- ✅ Using HTTPS by default

**Share your blog:** https://{{ cookiecutter.github_username }}.github.io/

Happy blogging! 📝
