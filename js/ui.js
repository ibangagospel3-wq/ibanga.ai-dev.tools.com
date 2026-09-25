const page = document.documentElement.dataset.page || '';

const rootPrefix =
  location.pathname.includes('/pages/') ||
  location.pathname.includes('/dashboard/')
    ? '../'
    : '';

window.IBANGA_API_BASE_URL ||=
  window.IBANGA_API_URL || 'http://127.0.0.1:8000/api';

if (!document.querySelector('link[rel="icon"]')) {
  const favicon = document.createElement('link');
  favicon.rel = 'icon';
  favicon.type = 'image/svg+xml';
  favicon.href = `${rootPrefix}favicon.svg`;
  document.head.appendChild(favicon);
}

/* =========================
   GLOBAL DOM HELPERS
   ========================= */

window.$ = (selector, root = document) =>
  root.querySelector(selector);

window.$$ = (selector, root = document) =>
  [...root.querySelectorAll(selector)];


/* =========================
   API
========================= */

const tokenKey = 'token';


/* =========================
   ROUTES
========================= */

const routes = {
  home: `${rootPrefix}index.html`,
  login: `${rootPrefix}pages/login.html`,
  register: `${rootPrefix}pages/register.html`,
  learn: `${rootPrefix}pages/learn.html`,
  playground: `${rootPrefix}pages/playground.html`,
  challenges: `${rootPrefix}pages/challenges.html`,
  projects: `${rootPrefix}pages/projects.html`,
  ai: `${rootPrefix}pages/ai-assistant.html`,
  docs: `${rootPrefix}pages/documentation.html`,
  about: `${rootPrefix}pages/about.html`,
  dashboard: `${rootPrefix}dashboard/dashboard.html`
};


/* =========================
   HEADER
========================= */

const header = $('#site-header');

if (header) {
  header.innerHTML = `
    <header class="site-header">
      <div class="container nav-wrap">

        <a class="brand" href="${routes.home}">
          <span class="brand-mark">I</span>

          <span>
            IBANGA AI
            <small>DEVELOPERS TOOL</small>
          </span>
        </a>

        <button
          class="menu-toggle"
          aria-label="Open navigation"
          aria-expanded="false">
          ☰
        </button>

        <nav class="main-nav" aria-label="Primary navigation">

          <a href="${routes.home}">
            Home
          </a>

          <a
            class="protected-link"
            href="${routes.learn}">
            Learn
          </a>

          <a
            class="protected-link"
            href="${routes.playground}">
            Code Playground
          </a>

          <a
            class="protected-link"
            href="${routes.challenges}">
            Challenges
          </a>

          <a
            class="protected-link"
            href="${routes.projects}">
            Projects
          </a>

          <a
            class="protected-link"
            href="${routes.ai}">
            AI Assistant
          </a>

          <a href="${routes.docs}">
            Docs
          </a>

          <a
            class="auth-login"
            href="${routes.login}">
            Login
          </a>

          <a
            class="auth-register btn btn-primary btn-small"
            href="${routes.register}">
            Get started
          </a>

          <span class="auth-user" hidden>

            <a href="${routes.dashboard}">
              Dashboard
            </a>

            <button
              class="logout-button theme-toggle"
              type="button">
              Logout
            </button>

          </span>

          <button
            class="theme-toggle theme-button"
            type="button"
            aria-label="Toggle theme">
            ◐
          </button>

        </nav>

      </div>
    </header>
  `;
}


/* =========================
   FOOTER
========================= */

const footer = $('#site-footer');

if (footer) {
  footer.innerHTML = `
    <footer class="site-footer">

      <div class="container">

        <div class="footer-grid">

          <div class="footer-brand">

            <a class="brand" href="${routes.home}">

              <span class="brand-mark">
                I
              </span>

              <span>
                IBANGA AI<br>
                <small>DEVELOPERS TOOL</small>
              </span>

            </a>

            <p>
              Modern HTML • CSS • JavaScript Companion
            </p>

            <p>
              Learn. Code. Build. Get AI Assistance.
            </p>

          </div>


          <div class="footer-links">

            <h4>PLATFORM</h4>

            <a href="${routes.learn}">
              Learn
            </a>

            <a href="${routes.playground}">
              Playground
            </a>

            <a href="${routes.challenges}">
              Challenges
            </a>

            <a href="${routes.projects}">
              Projects
            </a>

          </div>


          <div class="footer-links">

            <h4>RESOURCES</h4>

            <a href="${routes.ai}">
              IBANGA AI
            </a>

            <a href="${routes.docs}">
              Documentation
            </a>

            <a href="${routes.about}">
              About
            </a>

          </div>


          <div class="footer-links">

            <h4>ACCOUNT</h4>

            <a href="${routes.login}">
              Login
            </a>

            <a href="${routes.register}">
              Create account
            </a>

            <a href="${routes.dashboard}">
              Dashboard
            </a>

          </div>

        </div>


        <div class="footer-bottom">

          <span>
            © 2026 IBANGA AI Developers Tool.
            All rights reserved.
          </span>

          <span>
            Frontend + FastAPI + Gemini
          </span>

        </div>

      </div>

    </footer>
  `;
}


/* =========================
   EXTRA STYLES
========================= */

const style = document.createElement('style');

style.textContent = `
  .brand small {
    display: block;
    font: 600 .5rem Inter;
    letter-spacing: .09em;
    color: var(--muted);
  }

  .site-footer .brand small {
    color: #9aa8bd;
  }

  .auth-user {
    display: inline-flex;
    align-items: center;
    gap: 12px;
  }

  .auth-user a {
    color: var(--brand) !important;
    font-weight: 700;
  }

  .logout-button {
    border: 0;
    background: transparent;
    color: var(--muted);
    padding: 0;
    cursor: pointer;
  }

  .ai-fab {
    position: fixed;
    right: 24px;
    bottom: 24px;
    z-index: 70;
    width: 58px;
    height: 58px;
    border: 0;
    border-radius: 50%;
    background: linear-gradient(
      135deg,
      var(--brand),
      var(--brand-2)
    );
    color: #fff;
    font-size: 1.35rem;
    box-shadow: 0 12px 30px rgba(108, 92, 231, .4);
    animation: aiPulse 3s infinite;
    cursor: pointer;
  }

  .ai-fab:hover {
    transform: scale(1.08);
  }

  .ai-fab:after {
    content: "Ask IBANGA AI";
    position: absolute;
    right: 68px;
    top: 18px;
    background: var(--dark);
    color: #fff;
    border-radius: 7px;
    padding: 5px 8px;
    font-size: .7rem;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: .2s;
  }

  .ai-fab:hover:after {
    opacity: 1;
  }

  @keyframes aiPulse {
    0%, 100% {
      box-shadow:
        0 12px 30px rgba(108, 92, 231, .4);
    }

    50% {
      box-shadow:
        0 12px 30px rgba(0, 194, 255, .65);
    }
  }

  @media(max-width:760px) {

    .ai-fab {
      right: 18px;
      bottom: 18px;
    }

    .ai-fab:after {
      display: none;
    }

  }
`;

document.head.appendChild(style);


/* =========================
   BACKEND CHECK
========================= */

/*
   IMPORTANT:
   We use /health instead of /auth/me.

   /auth/me requires a login token,
   so using it as a backend availability
   check creates unnecessary 401 errors.
*/

async function backendIsReachable() {

  try {

    const controller =
      new AbortController();

    const timeout =
      setTimeout(
        () => controller.abort(),
        1200
      );

    const response =
      await fetch(
        `${window.IBANGA_API_BASE_URL}/health`,
        {
          headers: {
            Accept: 'application/json'
          },
          cache: 'no-store',
          signal: controller.signal
        }
      );

    clearTimeout(timeout);

    return response.ok;

  } catch {

    return false;

  }
}


/* =========================
   AUTH REDIRECT
========================= */

function authRedirect() {

  return `${location.pathname}${location.search}`;

}


/* =========================
   PROTECTED PAGES
========================= */

async function requireAuth() {

  const protectedPages = [
    'learn',
    'lesson',
    'playground',
    'projects',
    'challenges',
    'ai',
    'dashboard'
  ];


  if (!protectedPages.includes(page)) {
    return true;
  }


  const token =
    localStorage.getItem(tokenKey);


  if (!token) {

    location.href =
      `${routes.login}?redirect=${encodeURIComponent(
        authRedirect()
      )}`;

    return false;

  }

  if (!await backendIsReachable()) {
    location.href =
      `${routes.login}?redirect=${encodeURIComponent(
        authRedirect()
      )}`;

    return false;
  }


  try {

    const response =
      await fetch(
        `${window.IBANGA_API_BASE_URL}/auth/me`,
        {
          headers: {
            Authorization:
              `Bearer ${token}`,
            Accept:
              'application/json'
          }
        }
      );


    if (!response.ok) {
      throw new Error('expired');
    }


    window.currentUser =
      await response.json();


    return true;

  } catch {

    localStorage.removeItem(tokenKey);

    location.href =
      `${routes.login}?redirect=${encodeURIComponent(
        authRedirect()
      )}`;

    return false;

  }
}


/* =========================
   UPDATE AUTH UI
========================= */

async function updateAuthUI() {

  const token =
    localStorage.getItem(tokenKey);

  const login =
    $('.auth-login');

  const register =
    $('.auth-register');

  const user =
    $('.auth-user');


  if (!user) {
    return;
  }


  if (!token) {

    if (login) {
      login.hidden = false;
    }

    if (register) {
      register.hidden = false;
    }

    user.hidden = true;

    return;

  }


  const backendAvailable =
    await backendIsReachable();


  if (!backendAvailable) {

    window.IBANGA_DEMO_MODE = true;

    return;

  }


  if (login) {
    login.hidden = true;
  }

  if (register) {
    register.hidden = true;
  }

  user.hidden = false;


  try {

    const response =
      await fetch(
        `${window.IBANGA_API_BASE_URL}/auth/me`,
        {
          headers: {
            Authorization:
              `Bearer ${token}`,
            Accept:
              'application/json'
          }
        }
      );


    if (!response.ok) {
      throw new Error('invalid');
    }


    window.currentUser =
      await response.json();


  } catch {

    localStorage.removeItem(tokenKey);


    if (login) {
      login.hidden = false;
    }

    if (register) {
      register.hidden = false;
    }

    user.hidden = true;

  }
}


/* =========================
   THEME
========================= */

const storedTheme =
  localStorage.getItem('ibanga-theme');


if (storedTheme === 'dark') {
  document.body.classList.add('dark');
}


const theme =
  $('.theme-button');


theme?.addEventListener(
  'click',
  () => {

    document.body.classList.toggle('dark');


    localStorage.setItem(
      'ibanga-theme',
      document.body.classList.contains('dark')
        ? 'dark'
        : 'light'
    );


    theme.textContent =
      document.body.classList.contains('dark')
        ? '☀'
        : '◐';

  }
);


if (
  theme &&
  document.body.classList.contains('dark')
) {

  theme.textContent = '☀';

}


/* =========================
   MOBILE MENU
========================= */

const menu =
  $('.menu-toggle');

const nav =
  $('.main-nav');


menu?.addEventListener(
  'click',
  () => {

    const open =
      nav.classList.toggle('open');


    menu.setAttribute(
      'aria-expanded',
      String(open)
    );

  }
);


document.addEventListener(
  'click',
  event => {

    if (
      nav?.classList.contains('open') &&
      !nav.contains(event.target) &&
      !menu.contains(event.target)
    ) {

      nav.classList.remove('open');

      menu.setAttribute(
        'aria-expanded',
        'false'
      );

    }

  }
);


document.addEventListener(
  'keydown',
  event => {

    if (event.key === 'Escape') {

      nav?.classList.remove('open');

      menu?.setAttribute(
        'aria-expanded',
        'false'
      );

    }

  }
);


/* =========================
   LOGOUT
========================= */

$('.logout-button')?.addEventListener(
  'click',
  async () => {

    try {

      if (typeof logoutUser === 'function') {
        await logoutUser();
      }

    } catch {

      // Even if the API logout request fails,
      // remove the local token.

    } finally {

      localStorage.removeItem(tokenKey);

      location.href =
        routes.home;

    }

  }
);


/* =========================
   AI FLOATING BUTTON
========================= */

if (!$('#ai-assistant-page')) {

  const fab =
    document.createElement('button');

  fab.className =
    'ai-fab';

  fab.type =
    'button';

  fab.setAttribute(
    'aria-label',
    'Ask IBANGA AI'
  );

  fab.textContent =
    '✦';


  fab.addEventListener(
    'click',
    () => {

      location.href =
        `${routes.ai}?return=${encodeURIComponent(
          location.pathname
        )}`;

    }
  );


  document.body.append(fab);

}


/* =========================
   START AUTH CHECKS
========================= */

updateAuthUI();

requireAuth();


/* =========================
   REVEAL ANIMATIONS
========================= */

$$('.reveal').forEach(
  element => {

    const observer =
      new IntersectionObserver(
        entries => {

          if (
            entries[0].isIntersecting
          ) {

            element.classList.add(
              'visible'
            );

            observer.disconnect();

          }

        }
      );


    observer.observe(element);

  }
);
