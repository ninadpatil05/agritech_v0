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

  render: function(root, user, currentPath) {
    const isLoggedIn = !!user;
    const initial = user ? (user.first_name || user.email || 'U')[0].toUpperCase() : '';
    const themeIcon = (document.documentElement.getAttribute('data-theme') || 'light') === 'dark' ? '☀️' : '🌙';

    const publicLinks = [
      { href: '/index.html', label: 'Home' },
      { href: '/about.html', label: 'About' },
      { href: '/library.html', label: 'Library' },
      { href: '/contact.html', label: 'Contact' }
    ];

    const protectedLinks = [
      { href: '/dashboard.html', label: 'Dashboard', icon: '🏠' },
      { href: '/detect.html', label: 'Detect', icon: '🔬' },
      { href: '/weather.html', label: 'Weather', icon: '🌤' },
      { href: '/library.html', label: 'Library', icon: '📚' },
      { href: '/reports.html', label: 'Reports', icon: '📋' }
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
              title="Toggle dark mode" aria-label="Toggle dark mode">
        <span class="tt-icon">${themeIcon}</span>
      </button>
    ` + (isLoggedIn ? `
      <div class="navbar-avatar" onclick="this.querySelector('.navbar-dropdown').classList.toggle('show')">
        ${initial}
        <div class="navbar-dropdown">
          <a href="/profile.html" class="navbar-dropdown-item">👤 Profile</a>
          <div class="navbar-dropdown-divider"></div>
          <a href="#" class="navbar-dropdown-item" onclick="NavComponent.logout(event)">🚪 Logout</a>
        </div>
      </div>
    ` : `
      <a href="/auth.html" class="btn btn-ghost btn-sm">Login</a>
      <a href="/auth.html#signup" class="btn btn-primary btn-sm">Sign Up</a>
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
        <span class="tt-icon">${themeIcon}</span> Toggle Theme
      </button>
    ` + (isLoggedIn ? `
      <a href="/profile.html" class="navbar-mobile-link">👤 Profile</a>
      <a href="#" class="navbar-mobile-link" onclick="NavComponent.logout(event)">🚪 Logout</a>
    ` : `
      <a href="/auth.html" class="btn btn-ghost btn-full">Login</a>
      <a href="/auth.html#signup" class="btn btn-primary btn-full">Sign Up</a>
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
};

// Auto-initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
  NavComponent.init('nav-root');
});

window.NavComponent = NavComponent;
