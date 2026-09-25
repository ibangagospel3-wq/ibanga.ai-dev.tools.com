# IBANGA AI Developers Tool

**Modern HTML • CSS • JavaScript Companion**

A complete, original frontend learning and coding platform built with HTML5, CSS3, and vanilla JavaScript. It supports the core journey:

**Learn → Practice → Write code → Run code → See the result → Get AI help → Save projects**

## Run locally

1. Open `C:\Users\ACER\Desktop\UNKNOWN WORK` in VS Code.
2. Install the **Live Server** extension by Ritwick Dey.
3. Right-click `index.html` and select **Open with Live Server**.
4. Use the navigation to open the learning center, playground, challenges, projects, AI assistant, documentation, and dashboard.

No npm install or build step is required. The application is static and uses browser APIs.

## Main structure

- `index.html` — product landing page and learning journey.
- `pages/learn.html` — HTML, CSS, and JavaScript learning paths with progress tracking and lesson modals.
- `pages/playground.html` — three-editor browser playground with live iframe preview.
- `pages/challenges.html` — beginner coding challenges with basic automated checks.
- `pages/projects.html` — project templates plus locally saved projects.
- `pages/ai-assistant.html` — IBANGA AI Demo Mode chat with quick actions and code context.
- `pages/documentation.html` — searchable web development reference cards.
- `pages/about.html` — product explanation and contact link.
- `dashboard/dashboard.html` — learning progress dashboard.
- `css/style.css` — shared design system and landing styles.
- `css/responsive.css` — mobile, tablet, and desktop breakpoints.
- `css/editor.css` — playground editor and preview styles.
- `css/dashboard.css` — dashboard layout styles.
- `js/storage.js` — LocalStorage helpers and shared project/progress utilities.
- `js/ui.js` — path-aware navigation, footer, theme toggle, mobile menu, and reveal animations.
- `js/editor.js` — editor tabs, iframe rendering, run/reset/clear/copy/download/save, keyboard shortcuts, and error reporting.
- `js/playground.js` — playground-to-AI context handoff and preview fullscreen.
- `js/learning.js` — lesson catalog, completion tracking, and lesson modal content.
- `js/challenges.js` — challenge catalog and basic answer checks.
- `js/projects.js` — starter templates and saved-project load/delete actions.
- `js/ai-assistant.js` — Demo AI Mode responses and assistant UI.
- `js/dashboard.js` — dashboard sidebar and progress summaries.

## Playground

The playground has separate HTML, CSS, and JavaScript editors. Press **Run code** or `Ctrl/Cmd + Enter` to inject the combined code into a sandboxed iframe. Use `Ctrl/Cmd + S` to save the current project locally. You can copy code, download `index.html`, `style.css`, and `script.js`, reset, clear, refresh, fullscreen the preview, or send project context to IBANGA AI.

JavaScript errors are reported above the preview when the browser frame sends an error message to the parent application.

## LocalStorage

The demo stores only frontend learning data in the browser:

- `ibanga-theme` — light/dark preference.
- `ibanga-progress` — completed lesson IDs.
- `ibanga-projects` — saved project code.
- `ibanga-pending-project` — temporary handoff from a project template to the playground.
- `ibanga-ai-context` — temporary playground code context for the AI page.

Clear the site’s browser storage to reset the demo.

## AI integration and security

The current assistant is explicitly labeled **Demo AI Mode** and uses local mock responses. It has no API key and does not contact an AI provider.

For production, use this flow:

`Frontend → Backend API → AI provider`

The browser should call a backend endpoint such as:

- `POST /api/ai/chat`
- `POST /api/ai/explain-code`
- `POST /api/ai/debug-code`
- `POST /api/ai/generate-code`

Keep provider keys in server environment variables. Never put OpenAI, Gemini, Claude, or other provider secrets in HTML, CSS, or frontend JavaScript.

## Future backend

The frontend is ready for FastAPI or Express integration. Replace LocalStorage calls with `fetch()` service functions for endpoints such as:

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/user`
- `PUT /api/user`
- `GET /api/lessons`
- `GET /api/projects`
- `POST /api/projects`
- `PUT /api/projects/:id`
- `DELETE /api/projects/:id`
- `GET /api/progress`
- `PUT /api/progress`
- `POST /api/ai/chat`

A real backend should use secure sessions or short-lived tokens, validate all input server-side, and never trust frontend checks for authorization.

## Future database

A backend can persist users, lessons, projects, progress, challenges, submissions, AI conversations, and notifications in PostgreSQL or MongoDB.

## Images and deployment

The current UI uses CSS and code mockups, so no image files are required. If you add assets, put optimized files in `images/`, use meaningful `alt` text, and lazy-load below-the-fold images.

For deployment, upload the folder to any static host such as GitHub Pages, Netlify, Vercel static hosting, or Cloudflare Pages. Set the published directory to the project root and keep the relative folder structure unchanged.
