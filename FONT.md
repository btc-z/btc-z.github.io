# Font Configuration

## Current Setup

The blog uses custom fonts configured through CSS and MkDocs Material theme:

- **Chinese**: Ma Shan Zheng (马善政) - artistic handwritten style
- **English**: Lora - elegant serif font
- **Code blocks**: Fira Code - modern monospace with ligatures

## How It Works

### 1. Font Loading (CSS)
Fonts are loaded via Google Fonts CDN in `docs/stylesheets/extra.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap');
```

### 2. Font Application
Font stack is applied using CSS variables and selectors:

```css
:root {
  --md-text-font: "Lora", "Ma Shan Zheng", cursive;
  --md-code-font: "Fira Code", monospace;
}
```

The font order matters: English text uses Lora first, then falls back to Ma Shan Zheng for Chinese characters.

### 3. MkDocs Configuration
In `mkdocs.yml`, default Material fonts are disabled:

```yaml
theme:
  font: false  # Disable default fonts to use custom fonts
```

And custom CSS is loaded:

```yaml
extra_css:
  - stylesheets/extra.css
```

## Changing Fonts

### Option 1: Use Google Fonts

**Steps:**
1. Find your font at [Google Fonts](https://fonts.google.com/)
2. Update the `@import` URL in `docs/stylesheets/extra.css`
3. Update font family names in CSS variables and selectors

**Example - Changing Chinese font to LXGW WenKai:**

```css
/* Replace the import */
@import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.1.0/style.css');

/* Update font stack */
:root {
  --md-text-font: "Lora", "LXGW WenKai", serif;
}

body,
.md-typeset {
  font-family: "Lora", "LXGW WenKai", serif;
}
```

### Option 2: Use Local Fonts

If you have font files (.woff2, .ttf):

1. Create `docs/fonts/` directory
2. Add font files there
3. Update `docs/stylesheets/extra.css`:

```css
@font-face {
  font-family: 'CustomFont';
  src: url('../fonts/customfont.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
}
```

## Popular Font Alternatives

### Chinese Fonts
- **LXGW WenKai** (霞鹜文楷) - Elegant handwritten, great readability
- **Noto Sans CJK SC** - Modern sans-serif, professional
- **Noto Serif CJK SC** - Traditional serif, formal
- **Zhi Mang Xing** (志满星) - Casual handwritten
- **Liu Jian Mao Cao** (刘建毛草) - Artistic cursive

### English Fonts
- **Inter** - Modern sans-serif, excellent for screens
- **Merriweather** - Warm serif, great readability
- **Georgia** - Classic web serif
- **Roboto** - Clean sans-serif

### Code Fonts
- **JetBrains Mono** - Developer favorite
- **Cascadia Code** - Microsoft's modern choice
- **Source Code Pro** - Adobe's classic monospace

## Testing Changes

After making font changes:

1. Run local dev server:
   ```bash
   make serve
   ```

2. Open http://127.0.0.1:8000/

3. Check:
   - Chinese and English text rendering
   - Headings vs body text
   - Code blocks
   - Different font weights (bold, italic)

## Troubleshooting

**Fonts not loading:**
- Check browser console for network errors
- Verify font URLs are accessible
- Clear browser cache

**Chinese characters show wrong font:**
- Check font order in CSS (English font should come first)
- Verify the Chinese font supports Simplified/Traditional characters

**Performance issues:**
- Consider using fewer font weights
- Use `font-display: swap` in @import URLs
- Self-host fonts instead of CDN for faster loading

## File Reference

- **Font CSS**: `docs/stylesheets/extra.css`
- **MkDocs config**: `mkdocs.yml` (lines 21, 71-72)
- **This doc**: `FONT.md`
