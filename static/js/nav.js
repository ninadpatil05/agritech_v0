// Navigation Component
const NavComponent = {
  init: function(rootId) {
    const root = document.getElementById(rootId);
    if (!root) return;

    const currentPath = window.location.pathname;
    const cachedUser = sessionStorage.getItem('agritech_user');

    // Try cached user first, then fetch
    if (cachedUser) {
      this.render(root, JSON.parse(cachedUser), currentPath);
    } else {
      fetch('/api/me', { credentials: 'include' })
        .then(response => {
          if (response.status === 401) {
            this.render(root, null, currentPath);
            return null;
          }
          return response.json();
        })
        .then(data => {
          if (data) {
            sessionStorage.setItem('agritech_user', JSON.stringify(data.user || data));
            this.render(root, data.user || data, currentPath);
          }
        })
        .catch(() => {
          this.render(root, null, currentPath);
        });
    }
  },

  setLang: function(lang) {
    const root = document.getElementById('nav-root');
    if (!root) return;
    const cached = sessionStorage.getItem('agritech_user');
    this.render(root, cached ? JSON.parse(cached) : null, window.location.pathname);
  },

  render: function(root, user, currentPath) {
    const isLoggedIn = !!user;
    const initial = user ? (user.first_name || user.email || 'U')[0].toUpperCase() : '';
    const themeIcon = (document.documentElement.getAttribute('data-theme') || 'light') === 'dark' ? '☀️' : '🌙';
    const t = (key, fb) => (window.Lang ? Lang.t(key) : fb);

    const publicLinks = [
      { href: '/index.html',   label: t('nav_home',    'Home') },
      { href: '/about.html',   label: t('nav_about',   'About') },
      { href: '/library.html', label: t('nav_library', 'Library') },
      { href: '/contact.html', label: t('nav_contact', 'Contact') }
    ];

    const protectedLinks = [
      { href: '/dashboard.html', label: t('nav_dashboard', 'Dashboard'), icon: '🏠' },
      { href: '/detect.html',    label: t('nav_detect',    'Detect'),    icon: '🔬' },
      { href: '/weather.html',   label: t('nav_weather',   'Weather'),   icon: '🌤' },
      { href: '/library.html',   label: t('nav_library',   'Library'),   icon: '📚' },
      { href: '/reports.html',   label: t('nav_reports',   'Reports'),   icon: '📋' }
    ];

    const links = isLoggedIn ? protectedLinks : publicLinks;

    const linksHTML = links.map(link => {
      const isActive = currentPath === link.href || 
                       (link.href === '/index.html' && currentPath === '/');
      return `
        <a href="${link.href}" class="navbar-link ${isActive ? 'active' : ''}">
          ${link.icon ? link.icon + ' ' : ''}${link.label}
        </a>
      `;
    }).join('');

    const actionsHTML = `
      <button class="theme-toggle-btn" data-theme-toggle
              onclick="ThemeManager && ThemeManager.toggle()"
              title="${t('nav_toggle_theme', 'Toggle Theme')}" aria-label="${t('nav_toggle_theme', 'Toggle Theme')}">
        <span class="tt-icon">${themeIcon}</span>
      </button>
    ` + (isLoggedIn ? `
      <div class="navbar-avatar" onclick="this.querySelector('.navbar-dropdown').classList.toggle('show')">
        ${initial}
        <div class="navbar-dropdown">
          <a href="/profile.html" class="navbar-dropdown-item">👤 ${t('nav_profile', 'Profile')}</a>
          <div class="navbar-dropdown-divider"></div>
          <a href="#" class="navbar-dropdown-item" onclick="NavComponent.logout(event)">🚪 ${t('nav_logout', 'Logout')}</a>
        </div>
      </div>
    ` : `
      <a href="/auth.html" class="btn btn-ghost btn-sm">${t('nav_login', 'Login')}</a>
      <a href="/auth.html#signup" class="btn btn-primary btn-sm">${t('nav_signup', 'Sign Up')}</a>
    `);

    const mobileLinksHTML = links.map(link => {
      const isActive = currentPath === link.href || 
                       (link.href === '/index.html' && currentPath === '/');
      return `
        <a href="${link.href}" class="navbar-mobile-link ${isActive ? 'active' : ''}">
          ${link.icon ? link.icon + ' ' : ''}${link.label}
        </a>
      `;
    }).join('');

    const mobileActionsHTML = `
      <button class="navbar-mobile-link" style="background:none;border:none;text-align:left;cursor:pointer;font-family:inherit;font-size:16px;color:inherit;"
              data-theme-toggle onclick="ThemeManager && ThemeManager.toggle()">
        <span class="tt-icon">${themeIcon}</span> ${t('nav_toggle_theme', 'Toggle Theme')}
      </button>
    ` + (isLoggedIn ? `
      <a href="/profile.html" class="navbar-mobile-link">👤 ${t('nav_profile', 'Profile')}</a>
      <a href="#" class="navbar-mobile-link" onclick="NavComponent.logout(event)">🚪 ${t('nav_logout', 'Logout')}</a>
    ` : `
      <a href="/auth.html" class="btn btn-ghost btn-full">${t('nav_login', 'Login')}</a>
      <a href="/auth.html#signup" class="btn btn-primary btn-full">${t('nav_signup', 'Sign Up')}</a>
    `);

    root.innerHTML = `
      <nav class="navbar">
        <div class="navbar-inner">
          <a href="${isLoggedIn ? '/dashboard.html' : '/index.html'}" class="navbar-logo">
            🌿 Smart Crop Detective
          </a>
          
          <div class="navbar-links">
            ${linksHTML}
          </div>
          
          <div class="navbar-actions">
            ${actionsHTML}
          </div>
          
          <button class="navbar-hamburger" onclick="NavComponent.toggleMobile()">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
        
        <div class="navbar-mobile-menu" id="navbar-mobile-menu">
          ${mobileLinksHTML}
          <div class="navbar-mobile-actions">
            ${mobileActionsHTML}
          </div>
        </div>
      </nav>
    `;

    // Sync theme button icon after render
    if (window.ThemeManager) ThemeManager.syncBtns();

    // Close dropdown when clicking outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.navbar-avatar')) {
        const dropdown = document.querySelector('.navbar-dropdown');
        if (dropdown) dropdown.classList.remove('show');
      }
    });
    NavComponent._injectLangSwitcher();
  },

  toggleMobile: function() {
    const menu = document.getElementById('navbar-mobile-menu');
    const hamburger = document.querySelector('.navbar-hamburger');
    
    if (menu && hamburger) {
      menu.classList.toggle('show');
      hamburger.classList.toggle('active');
    }
  },

  logout: function(e) {
    e.preventDefault();
    
    fetch('/api/logout', {
      method: 'POST',
      credentials: 'include'
    })
    .then(() => {
      sessionStorage.removeItem('agritech_user');
      window.location.href = '/index.html';
    })
    .catch(() => {
      sessionStorage.removeItem('agritech_user');
      window.location.href = '/index.html';
    });
  }
,

  _injectLangSwitcher: function() {
    const currentLang = window.Lang ? Lang.get() : (localStorage.getItem('lang') || 'en');
    const labels = { en: 'EN', hi: 'हि', mr: 'म' };
    const fullNames = {
      en: { flag: '🇬🇧', name: 'English' },
      hi: { flag: '🇮🇳', name: 'हिंदी' },
      mr: { flag: '🇮🇳', name: 'मराठी' }
    };

    const existing = document.getElementById('global-lang-switcher');
    if (existing) {
      const lbl = existing.querySelector('.gls-label');
      if (lbl) lbl.textContent = labels[currentLang] || 'EN';
      existing.querySelectorAll('.gls-option').forEach(btn => {
        btn.classList.toggle('gls-active', btn.dataset.lang === currentLang);
      });
      return;
    }

    if (!document.getElementById('gls-styles')) {
      const style = document.createElement('style');
      style.id = 'gls-styles';
      style.textContent = `
        #global-lang-switcher {
          position: fixed;
          bottom: 28px;
          right: 24px;
          z-index: 9999;
          font-family: 'Inter', 'Noto Sans Devanagari', sans-serif;
        }
        .gls-btn {
          display: flex;
          align-items: center;
          gap: 6px;
          padding: 9px 15px;
          background: var(--surface, #fff);
          border: 1.5px solid var(--border, #e2e8f0);
          border-radius: 999px;
          cursor: pointer;
          font-size: 13px;
          font-weight: 600;
          color: var(--text, #1a202c);
          box-shadow: 0 4px 20px rgba(0,0,0,0.12);
          transition: box-shadow 0.2s, transform 0.15s;
          white-space: nowrap;
          user-select: none;
        }
        @media (max-width: 768px) {
          #global-lang-switcher {
            bottom: 84px; /* Move above mobile-nav (64px) + 20px padding */
          }
        }
        .gls-btn:hover {
          box-shadow: 0 6px 28px rgba(0,0,0,0.18);
          transform: translateY(-1px);
        }
        .gls-btn:active { transform: translateY(0); }
        .gls-globe { font-size: 15px; line-height: 1; }
        .gls-label { letter-spacing: 0.03em; }
        .gls-chevron {
          font-size: 10px;
          opacity: 0.5;
          transition: transform 0.2s;
          display: inline-block;
        }
        #global-lang-switcher.open .gls-chevron { transform: rotate(180deg); }
        .gls-popup {
          display: none;
          position: absolute;
          bottom: calc(100% + 10px);
          right: 0;
          background: var(--surface, #fff);
          border: 1.5px solid var(--border, #e2e8f0);
          border-radius: 16px;
          box-shadow: 0 8px 32px rgba(0,0,0,0.15);
          overflow: hidden;
          min-width: 160px;
          animation: glsPopIn 0.18s ease;
        }
        @keyframes glsPopIn {
          from { opacity: 0; transform: translateY(6px) scale(0.97); }
          to   { opacity: 1; transform: translateY(0) scale(1); }
        }
        #global-lang-switcher.open .gls-popup { display: block; }
        .gls-popup-header {
          padding: 10px 14px 8px;
          font-size: 11px;
          font-weight: 700;
          letter-spacing: 0.08em;
          text-transform: uppercase;
          color: var(--text-muted, #718096);
          border-bottom: 1px solid var(--border, #e2e8f0);
        }
        .gls-option {
          display: flex;
          align-items: center;
          gap: 10px;
          width: 100%;
          padding: 11px 14px;
          background: none;
          border: none;
          cursor: pointer;
          font-size: 14px;
          font-weight: 500;
          color: var(--text, #1a202c);
          text-align: left;
          transition: background 0.15s;
          font-family: inherit;
        }
        .gls-option:hover { background: var(--green-tint, rgba(45,106,79,0.07)); }
        .gls-option.gls-active {
          background: var(--green-tint, rgba(45,106,79,0.1));
          color: var(--green-700, #2d6a4f);
          font-weight: 700;
        }
        .gls-option .gls-check {
          margin-left: auto;
          opacity: 0;
          color: var(--green-700, #2d6a4f);
          font-size: 13px;
        }
        .gls-option.gls-active .gls-check { opacity: 1; }
        .gls-flag { font-size: 16px; line-height: 1; }
      `;
      document.head.appendChild(style);
    }

    const widget = document.createElement('div');
    widget.id = 'global-lang-switcher';

    const optionsHTML = Object.entries(fullNames).map(([code, info]) => `
      <button class="gls-option ${code === currentLang ? 'gls-active' : ''}" data-lang="${code}" tabindex="0"
              onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();this.click();}"
              onclick="event.stopPropagation(); if(window.Lang){Lang.set('${code}');} else{localStorage.setItem('lang','${code}');location.reload();} document.getElementById('global-lang-switcher').classList.remove('open');">
        <span class="gls-flag">${info.flag}</span>
        <span>${info.name}</span>
        <span class="gls-check">✓</span>
      </button>
    `).join('');

    widget.innerHTML = `
      <div class="gls-popup" role="dialog" aria-label="Language selection">
        <div class="gls-popup-header">🌐 Language / भाषा</div>
        ${optionsHTML}
      </div>
      <button class="gls-btn" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();document.getElementById('global-lang-switcher').classList.toggle('open');}" onclick="document.getElementById('global-lang-switcher').classList.toggle('open');" aria-label="Switch language" aria-haspopup="true" aria-expanded="false">
        <span class="gls-globe">🌐</span>
        <span class="gls-label">${labels[currentLang] || 'EN'}</span>
        <span class="gls-chevron">▲</span>
      </button>
    `;

    document.body.appendChild(widget);

    document.addEventListener('click', function(e) {
      if (!e.target.closest('#global-lang-switcher')) {
        widget.classList.remove('open');
      }
    });

    // Keep aria-expanded in sync with the open class
    const glsBtn = widget.querySelector('.gls-btn');
    const observer = new MutationObserver(() => {
      glsBtn.setAttribute('aria-expanded', widget.classList.contains('open').toString());
    });
    observer.observe(widget, { attributes: true, attributeFilter: ['class'] });

    window.addEventListener('langchange', function(e) {
      NavComponent._injectLangSwitcher();
    });
  }
};

// Auto-initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
  NavComponent.init('nav-root');
  NavComponent._injectLangSwitcher();
});

window.NavComponent = NavComponent;
