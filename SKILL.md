---
name: frontend-slides
description: Creating beautiful frontend HTML/CSS/JS presentation slides. Use when the user wants to create a slide deck, presentation, or slideshow using web technologies.
---

# Frontend Slides Skill

Create beautiful, self-contained HTML presentation slides with smooth transitions, responsive layouts, and polished styling — all in a single file.

## Overview

This skill produces single-file HTML presentations that work offline in any modern browser. No build tools, no dependencies, no server required.

**Output:** One `slides.html` file (or a name the user specifies) that contains all HTML, CSS, and JS inline.

## Workflow

Make a todo list for all the tasks in this workflow and work through them one at a time.

### 1. Gather Requirements

Ask the user (or infer from context):
- **Topic / title** of the presentation
- **Audience** (technical, executive, general public, etc.)
- **Number of slides** (approximate, or list of slide titles/topics)
- **Style preset** — see `STYLE_PRESETS.md` for options (default: `dark-tech`)
- **Special needs** — code blocks, diagrams, images, speaker notes, progress bar, etc.

If the user already provided all of this, skip ahead.

### 2. Plan the Slide Deck

Draft a quick outline:
```
Slide 1: Title slide (title, subtitle, author)
Slide 2: Agenda / overview
Slide 3-N: Content slides
Slide N+1: Closing / Q&A / Thank you
```

Confirm the outline with the user if there is any ambiguity.

### 3. Choose a Style Preset

Pick (or let the user pick) a preset from `STYLE_PRESETS.md`. Each preset defines:
- Background and foreground colors
- Font families (loaded from Google Fonts or system fonts)
- Accent color used for headings, highlights, and bullets
- Code block theme

### 4. Build the HTML File

Create a single self-contained HTML file using the structure below.

#### Base HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title><!-- Presentation Title --></title>
  <style>
    /* === PASTE PRESET CSS VARIABLES HERE === */
    /* === CORE SLIDE ENGINE CSS BELOW === */

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-body);
      background: var(--bg);
      color: var(--fg);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* Progress bar */
    #progress {
      position: fixed;
      top: 0; left: 0;
      height: 3px;
      background: var(--accent);
      transition: width 0.3s ease;
      z-index: 100;
    }

    /* Slide container */
    #deck {
      flex: 1;
      position: relative;
      overflow: hidden;
    }

    .slide {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 4rem 6rem;
      opacity: 0;
      transform: translateX(60px);
      transition: opacity 0.4s ease, transform 0.4s ease;
      pointer-events: none;
    }

    .slide.active {
      opacity: 1;
      transform: translateX(0);
      pointer-events: auto;
    }

    .slide.exit {
      opacity: 0;
      transform: translateX(-60px);
    }

    /* Typography */
    h1 { font-family: var(--font-heading); font-size: clamp(2rem, 5vw, 3.5rem); color: var(--accent); line-height: 1.1; }
    h2 { font-family: var(--font-heading); font-size: clamp(1.5rem, 3.5vw, 2.5rem); color: var(--accent); margin-bottom: 1.5rem; }
    h3 { font-size: clamp(1rem, 2vw, 1.4rem); color: var(--fg-muted); margin-bottom: 0.75rem; }
    p, li { font-size: clamp(0.95rem, 1.8vw, 1.25rem); line-height: 1.7; max-width: 70ch; }
    ul, ol { padding-left: 1.5rem; }
    li { margin-bottom: 0.5rem; }
    li::marker { color: var(--accent); }

    /* Subtitle on title slide */
    .subtitle { font-size: clamp(1rem, 2vw, 1.4rem); color: var(--fg-muted); margin-top: 1rem; }
    .author   { font-size: 1rem; color: var(--fg-muted); margin-top: 2rem; }

    /* Two-column layout */
    .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; width: 100%; }

    /* Highlight / callout box */
    .callout {
      background: var(--surface);
      border-left: 4px solid var(--accent);
      border-radius: 0 8px 8px 0;
      padding: 1rem 1.5rem;
      margin: 1rem 0;
      width: 100%;
    }

    /* Code blocks */
    pre {
      background: var(--code-bg);
      color: var(--code-fg);
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: clamp(0.75rem, 1.4vw, 1rem);
      overflow-x: auto;
      width: 100%;
      line-height: 1.6;
    }
    code { font-family: var(--font-mono); font-size: 0.9em; }

    /* Image helper */
    .slide img { max-width: 100%; max-height: 55vh; object-fit: contain; border-radius: 8px; }

    /* Speaker notes (hidden by default, shown with ?notes=1) */
    .notes {
      display: none;
      position: fixed;
      bottom: 0; left: 0; right: 0;
      background: rgba(0,0,0,0.85);
      color: #eee;
      padding: 1rem 2rem;
      font-size: 0.9rem;
      line-height: 1.5;
      max-height: 25vh;
      overflow-y: auto;
    }
    body.show-notes .notes { display: block; }

    /* Nav controls */
    #nav {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      padding: 0.75rem;
      background: var(--surface);
      font-size: 0.85rem;
      color: var(--fg-muted);
    }
    #nav button {
      background: var(--accent);
      color: #fff;
      border: none;
      border-radius: 6px;
      padding: 0.4rem 1rem;
      cursor: pointer;
      font-size: 0.85rem;
      font-family: inherit;
      transition: opacity 0.2s;
    }
    #nav button:disabled { opacity: 0.35; cursor: default; }
    #nav button:not(:disabled):hover { opacity: 0.85; }
  </style>
</head>
<body>
  <div id="progress"></div>

  <div id="deck">

    <!-- ═══════════════════════════════════════════
         SLIDE 1 — Title
    ════════════════════════════════════════════ -->
    <section class="slide active" id="s1">
      <h1>Presentation Title</h1>
      <p class="subtitle">A concise, compelling subtitle</p>
      <p class="author">Author Name · Date</p>
      <aside class="notes">Welcome everyone. Today I'll be covering…</aside>
    </section>

    <!-- ═══════════════════════════════════════════
         SLIDE 2 — Agenda
    ════════════════════════════════════════════ -->
    <section class="slide" id="s2">
      <h2>Agenda</h2>
      <ul>
        <li>Topic One</li>
        <li>Topic Two</li>
        <li>Topic Three</li>
        <li>Q &amp; A</li>
      </ul>
      <aside class="notes">Here is what we'll cover today…</aside>
    </section>

    <!-- Add more slides here following the same pattern -->

  </div>

  <nav id="nav">
    <button id="btn-prev" disabled>← Prev</button>
    <span id="counter">1 / 1</span>
    <button id="btn-next">Next →</button>
  </nav>

  <script>
    (function () {
      const slides = Array.from(document.querySelectorAll('.slide'));
      const progress = document.getElementById('progress');
      const counter  = document.getElementById('counter');
      const btnPrev  = document.getElementById('btn-prev');
      const btnNext  = document.getElementById('btn-next');
      let current = 0;

      // Show notes when URL contains ?notes=1
      if (new URLSearchParams(location.search).get('notes') === '1') {
        document.body.classList.add('show-notes');
      }

      function goTo(idx) {
        if (idx < 0 || idx >= slides.length) return;
        slides[current].classList.remove('active');
        slides[current].classList.add('exit');
        setTimeout(() => slides[current < idx ? current : idx + (current - idx)]
          ?.classList.remove('exit'), 450);
        current = idx;
        slides[current].classList.add('active');
        slides[current].classList.remove('exit');
        counter.textContent = `${current + 1} / ${slides.length}`;
        btnPrev.disabled = current === 0;
        btnNext.disabled = current === slides.length - 1;
        const pct = slides.length > 1
          ? ((current / (slides.length - 1)) * 100).toFixed(1)
          : 100;
        progress.style.width = pct + '%';
      }

      btnPrev.addEventListener('click', () => goTo(current - 1));
      btnNext.addEventListener('click', () => goTo(current + 1));

      document.addEventListener('keydown', e => {
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') goTo(current + 1);
        if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')                    goTo(current - 1);
        if (e.key === 'Home') goTo(0);
        if (e.key === 'End')  goTo(slides.length - 1);
      });

      // Touch / swipe support
      let touchX = null;
      document.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; });
      document.addEventListener('touchend',   e => {
        if (touchX === null) return;
        const dx = e.changedTouches[0].clientX - touchX;
        if (Math.abs(dx) > 50) goTo(current + (dx < 0 ? 1 : -1));
        touchX = null;
      });

      goTo(0);
    })();
  </script>
</body>
</html>
```

### 5. Populate Content

Fill in each slide with the actual content:
- Use `<h2>` for slide titles, `<h1>` only on the title slide
- Use `<ul>` / `<ol>` for bullet points (keep to 5 items max per slide)
- Use `<pre><code>` for code — include the language as a comment or class when relevant
- Use `.cols` div for two-column layouts
- Use `.callout` for important quotes or key takeaways
- Add `<aside class="notes">…</aside>` inside each slide for speaker notes
- Keep each slide focused on **one idea**

### 6. Apply the Style Preset

Copy the CSS variables block from the chosen preset in `STYLE_PRESETS.md` and paste it at the top of the `<style>` section, replacing the placeholder comment.

### 7. Validate

Open the file in a browser (or use a local server) and check:
- [ ] All slides are reachable via arrow keys and buttons
- [ ] Progress bar advances correctly
- [ ] Code blocks are readable
- [ ] Text doesn't overflow on any slide
- [ ] Responsive at common viewport sizes (1280×720, 1920×1080)

### 8. Deliver

Save the final file and inform the user:
- Filename and location
- Keyboard shortcuts: `→`/`Space` next, `←` prev, `Home`/`End` first/last
- Speaker notes: add `?notes=1` to the URL
- How to change the preset (point to `STYLE_PRESETS.md`)

## Slide Types Reference

| Type | When to use |
|------|-------------|
| **Title** | First slide only — `<h1>` + `.subtitle` + `.author` |
| **Bullet list** | Key points, agenda, features |
| **Two-column** | Compare/contrast, text + image |
| **Code** | Technical demos — wrap in `<pre><code>` |
| **Callout** | Single important quote or stat |
| **Image** | Full-bleed or centered visual |
| **Closing** | Thank you, links, Q&A prompt |

## Best Practices

- **Less is more** — aim for 6–8 words per bullet, 5 bullets max per slide
- **One idea per slide** — split complex topics across multiple slides
- **Consistent layout** — don't mix too many different slide layouts
- **Contrast** — ensure text is legible; rely on preset color variables
- **No external dependencies** — embed images as base64 if needed, use system/Google fonts with a fallback stack
- **Accessibility** — use semantic HTML, `alt` text on images, sufficient color contrast

## Wrap Up

In your final message to the user, provide:

* **File location** of the generated slide deck
* **Slide count** and brief outline
* **Keyboard shortcuts** summary
* **Style preset used** and how to switch presets
* **Speaker notes** instructions (`?notes=1`)
