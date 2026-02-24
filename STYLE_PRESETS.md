# Frontend Slides — Style Presets

Each preset is a self-contained CSS variables block. Copy the block for the chosen preset and paste it inside the `<style>` tag of `slides.html`, replacing the `/* === PASTE PRESET CSS VARIABLES HERE === */` comment.

---

## `dark-tech` (Default)

Dark background, electric-blue accent. Great for developer talks, technical demos, and engineering presentations.

```css
/* === PRESET: dark-tech === */
:root {
  --bg:           #0d1117;
  --surface:      #161b22;
  --fg:           #e6edf3;
  --fg-muted:     #8b949e;
  --accent:       #58a6ff;
  --font-heading: 'JetBrains Mono', 'Fira Code', monospace;
  --font-body:    'Inter', 'Segoe UI', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  --code-bg:      #1e2430;
  --code-fg:      #a9b7c6;
}
/* Google Fonts for dark-tech */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap');
```

---

## `light-clean`

White background, indigo accent. Ideal for product demos, design reviews, and general business presentations.

```css
/* === PRESET: light-clean === */
:root {
  --bg:           #ffffff;
  --surface:      #f3f4f6;
  --fg:           #111827;
  --fg-muted:     #6b7280;
  --accent:       #4f46e5;
  --font-heading: 'Plus Jakarta Sans', 'Nunito', sans-serif;
  --font-body:    'Inter', 'Segoe UI', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  --code-bg:      #f9fafb;
  --code-fg:      #374151;
}
/* Google Fonts for light-clean */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Plus+Jakarta+Sans:wght@600;700&display=swap');
```

---

## `corporate-blue`

Navy background, gold accent. Professional and polished — suits executive briefings, finance, and strategy decks.

```css
/* === PRESET: corporate-blue === */
:root {
  --bg:           #0a1628;
  --surface:      #112040;
  --fg:           #e8eef7;
  --fg-muted:     #94a3b8;
  --accent:       #f59e0b;
  --font-heading: 'Merriweather', Georgia, serif;
  --font-body:    'Source Sans 3', 'Segoe UI', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;
  --code-bg:      #0d1f3c;
  --code-fg:      #cbd5e1;
}
/* Google Fonts for corporate-blue */
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@700&family=Source+Sans+3:wght@400;600&display=swap');
```

---

## `pastel-minimal`

Soft cream background, rose accent. Friendly and approachable — good for education, onboarding, and community talks.

```css
/* === PRESET: pastel-minimal === */
:root {
  --bg:           #fdf6f0;
  --surface:      #fce8d8;
  --fg:           #2d2013;
  --fg-muted:     #7a6652;
  --accent:       #e05a6e;
  --font-heading: 'Playfair Display', Georgia, serif;
  --font-body:    'Lato', 'Helvetica Neue', sans-serif;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;
  --code-bg:      #fff0e8;
  --code-fg:      #4a3728;
}
/* Google Fonts for pastel-minimal */
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Playfair+Display:wght@700&display=swap');
```

---

## `hacker-green`

Black background, terminal-green accent. Perfect for security research, CTF write-ups, and hacker-culture talks.

```css
/* === PRESET: hacker-green === */
:root {
  --bg:           #050a05;
  --surface:      #0b150b;
  --fg:           #b6f5b6;
  --fg-muted:     #4e9e4e;
  --accent:       #39ff14;
  --font-heading: 'Share Tech Mono', 'Fira Code', monospace;
  --font-body:    'Share Tech Mono', 'Fira Code', monospace;
  --font-mono:    'Share Tech Mono', 'Fira Code', 'Courier New', monospace;
  --code-bg:      #0a170a;
  --code-fg:      #7fff7f;
}
/* Google Fonts for hacker-green */
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
```

---

## `sunset-warm`

Deep plum background, orange accent. Eye-catching and energetic — great for marketing, creative, and keynote-style talks.

```css
/* === PRESET: sunset-warm === */
:root {
  --bg:           #1a0a2e;
  --surface:      #2d1147;
  --fg:           #f5e6d3;
  --fg-muted:     #b89ec7;
  --accent:       #ff7b35;
  --font-heading: 'Raleway', 'Trebuchet MS', sans-serif;
  --font-body:    'Open Sans', 'Segoe UI', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;
  --code-bg:      #250e3d;
  --code-fg:      #f0d5b8;
}
/* Google Fonts for sunset-warm */
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Raleway:wght@700;800&display=swap');
```

---

## `monochrome`

Pure black-and-white with a gray accent. Timeless and distraction-free — ideal for academic papers, research, or printing.

```css
/* === PRESET: monochrome === */
:root {
  --bg:           #121212;
  --surface:      #1e1e1e;
  --fg:           #f0f0f0;
  --fg-muted:     #9e9e9e;
  --accent:       #bdbdbd;
  --font-heading: 'IBM Plex Sans', Arial, sans-serif;
  --font-body:    'IBM Plex Sans', Arial, sans-serif;
  --font-mono:    'IBM Plex Mono', 'Courier New', monospace;
  --code-bg:      #1a1a1a;
  --code-fg:      #d4d4d4;
}
/* Google Fonts for monochrome */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&family=IBM+Plex+Sans:wght@400;600&display=swap');
```

---

## `ocean-breeze`

Teal-navy gradient feel, cyan accent. Clean and modern — works well for data, science, and analytics presentations.

```css
/* === PRESET: ocean-breeze === */
:root {
  --bg:           #0c1e2e;
  --surface:      #102840;
  --fg:           #d6f0f7;
  --fg-muted:     #7fb8cc;
  --accent:       #00e5cc;
  --font-heading: 'DM Sans', 'Helvetica Neue', sans-serif;
  --font-body:    'DM Sans', 'Helvetica Neue', sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  --code-bg:      #091825;
  --code-fg:      #a8d8e8;
}
/* Google Fonts for ocean-breeze */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&display=swap');
```

---

## Offline / No-Internet Fallback

If the presentation must work without internet access, use this system-font-only variant. Replace `@import` with this block and pick any variable set above (or customize freely).

```css
/* === PRESET: system-fonts (offline safe) === */
:root {
  --bg:           #1a1a2e;
  --surface:      #16213e;
  --fg:           #e0e0e0;
  --fg-muted:     #9090a0;
  --accent:       #e94560;
  --font-heading: system-ui, -apple-system, 'Segoe UI', Arial, sans-serif;
  --font-body:    system-ui, -apple-system, 'Segoe UI', Arial, sans-serif;
  --font-mono:    ui-monospace, 'Cascadia Code', 'Fira Code', 'Courier New', monospace;
  --code-bg:      #0f111a;
  --code-fg:      #c8c8d0;
}
/* No @import needed — uses system fonts only */
```

---

## Preset Quick-Reference

| Preset | Background | Accent | Best for |
|--------|-----------|--------|----------|
| `dark-tech` | Dark gray | Electric blue | Dev / engineering talks |
| `light-clean` | White | Indigo | Product / design reviews |
| `corporate-blue` | Navy | Gold | Executive / finance decks |
| `pastel-minimal` | Cream | Rose | Education / onboarding |
| `hacker-green` | Black | Neon green | Security / CTF |
| `sunset-warm` | Deep plum | Orange | Marketing / keynote |
| `monochrome` | Near-black | Light gray | Academic / research |
| `ocean-breeze` | Teal-navy | Cyan | Data / science / analytics |
| `system-fonts` | Dark navy | Red | Offline / no internet |
