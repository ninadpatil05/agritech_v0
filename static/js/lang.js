// Language Management for Bilingual Support
const Lang = {
  set: function(lang) {
    localStorage.setItem('lang', lang);
    this.updateElements();
    this.updateToggle();
  },

  get: function() {
    return localStorage.getItem('lang') || 'en';
  },

  updateElements: function() {
    const lang = this.get();
    const elements = document.querySelectorAll('[data-en][data-hi]');
    
    elements.forEach(el => {
      if (lang === 'hi') {
        el.textContent = el.dataset.hi;
      } else {
        el.textContent = el.dataset.en;
      }
    });
  },

  updateToggle: function() {
    const lang = this.get();
    const buttons = document.querySelectorAll('.language-toggle button');
    
    buttons.forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.lang === lang) {
        btn.classList.add('active');
      }
    });
  },

  init: function() {
    this.updateElements();
    this.updateToggle();

    // Setup toggle buttons
    document.querySelectorAll('.language-toggle button').forEach(btn => {
      btn.addEventListener('click', () => {
        this.set(btn.dataset.lang);
      });
    });
  }
};

window.Lang = Lang;

// Auto-initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
  Lang.init();
});
