// Toast Notification System
const Toast = {
  container: null,

  init: function() {
    if (!this.container) {
      this.container = document.createElement('div');
      this.container.className = 'toast-container';
      document.body.appendChild(this.container);
    }
  },

  show: function(message, type = 'info', title = '') {
    this.init();

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    toast.innerHTML = `
      ${title ? `<div class="toast-title">${title}</div>` : ''}
      <div class="toast-message">${message}</div>
    `;

    this.container.appendChild(toast);

    // Auto dismiss after 4 seconds
    setTimeout(() => {
      toast.style.animation = 'slideOutRight 0.3s ease forwards';
      setTimeout(() => {
        toast.remove();
      }, 300);
    }, 4000);
  },

  success: function(message, title = 'Success') {
    this.show(message, 'success', title);
  },

  error: function(message, title = 'Error') {
    this.show(message, 'error', title);
  },

  warning: function(message, title = 'Warning') {
    this.show(message, 'warning', title);
  },

  info: function(message, title = 'Info') {
    this.show(message, 'info', title);
  }
};

window.Toast = Toast;

// Form Validation Helper
const FormValidator = {
  validateEmail: function(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  },

  validatePhone: function(phone) {
    const re = /^[0-9]{10}$/;
    return phone === '' || re.test(phone.replace(/[^0-9]/g, ''));
  },

  validatePassword: function(password) {
    return password.length >= 6;
  },

  getPasswordStrength: function(password) {
    if (password.length < 6) return 'weak';
    if (password.length < 8) return 'medium';
    
    const hasUpper = /[A-Z]/.test(password);
    const hasLower = /[a-z]/.test(password);
    const hasNumber = /[0-9]/.test(password);
    const hasSpecial = /[!@#$%^&*(),.?":{}|<>]/.test(password);
    
    const strength = [hasUpper, hasLower, hasNumber, hasSpecial].filter(Boolean).length;
    
    if (strength >= 3 && password.length >= 8) return 'strong';
    if (strength >= 2) return 'medium';
    return 'weak';
  },

  showError: function(input, message) {
    const formGroup = input.closest('.form-group');
    if (!formGroup) return;

    input.classList.add('error');
    
    let errorEl = formGroup.querySelector('.form-error');
    if (!errorEl) {
      errorEl = document.createElement('div');
      errorEl.className = 'form-error';
      formGroup.appendChild(errorEl);
    }
    
    errorEl.textContent = message;
    errorEl.classList.add('show');
  },

  clearError: function(input) {
    const formGroup = input.closest('.form-group');
    if (!formGroup) return;

    input.classList.remove('error');
    
    const errorEl = formGroup.querySelector('.form-error');
    if (errorEl) {
      errorEl.classList.remove('show');
    }
  },

  clearAllErrors: function(form) {
    form.querySelectorAll('.form-input').forEach(input => {
      this.clearError(input);
    });
  }
};

window.FormValidator = FormValidator;

// Modal Helper
const Modal = {
  show: function(id, triggerEl) {
    const modal = document.getElementById(id);
    if (modal) {
      modal._trigger = triggerEl || document.activeElement;
      modal.classList.add('show');
      document.body.style.overflow = 'hidden';
      const focusable = modal.querySelector('button, [href], input, select, textarea');
      if (focusable) setTimeout(() => focusable.focus(), 50);
    }
  },
  hide: function(id) {
    const modal = document.getElementById(id);
    if (modal) {
      modal.classList.remove('show');
      document.body.style.overflow = '';
      if (modal._trigger && modal._trigger.focus) modal._trigger.focus();
    }
  },

  init: function() {
    // Close modal on overlay click
    document.querySelectorAll('.modal-overlay').forEach(overlay => {
      overlay.addEventListener('click', function(e) {
        if (e.target === this) {
          this.classList.remove('show');
          document.body.style.overflow = '';
          if (this._trigger) this._trigger.focus();
        }
      });
    });

    // Close modal on close button click
    document.querySelectorAll('.modal-close').forEach(btn => {
      btn.addEventListener('click', function() {
        const modal = this.closest('.modal-overlay');
        if (modal) {
          modal.classList.remove('show');
          document.body.style.overflow = '';
          if (modal._trigger) modal._trigger.focus();
        }
      });
    });

    // Keyboard Escape listener
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.show').forEach(m => {
          m.classList.remove('show');
          document.body.style.overflow = '';
          if (m._trigger) m._trigger.focus();
        });
      }
    });
  }
};

window.Modal = Modal;

// Date Formatter
const DateFormatter = {
  format: function(date, format = 'short') {
    const d = new Date(date);
    const loc = window.Lang ? Lang.locale() : 'en-IN';
    
    if (format === 'short') {
      return d.toLocaleDateString(loc, {
        day: 'numeric',
        month: 'short',
        year: 'numeric'
      });
    }
    
    if (format === 'long') {
      return d.toLocaleDateString(loc, {
        weekday: 'long',
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      });
    }
    
    if (format === 'time') {
      return d.toLocaleTimeString(loc, {
        hour: '2-digit',
        minute: '2-digit'
      });
    }
    
    if (format === 'datetime') {
      return d.toLocaleDateString(loc, {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    }
    
    return d.toISOString();
  },

  today: function() {
    return this.format(new Date(), 'long');
  }
};

window.DateFormatter = DateFormatter;

// CSV Export Helper
const CSVExporter = {
  export: function(data, filename) {
    if (!data || !data.length) return;

    const headers = Object.keys(data[0]);
    const csvContent = [
      headers.join(','),
      ...data.map(row => headers.map(header => {
        let value = row[header] || '';
        // Escape quotes and wrap in quotes if contains comma
        if (typeof value === 'string' && (value.includes(',') || value.includes('"'))) {
          value = `"${value.replace(/"/g, '""')}"`;
        }
        return value;
      }).join(','))
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = filename || 'export.csv';
    link.click();
    
    URL.revokeObjectURL(url);
  }
};

window.CSVExporter = CSVExporter;

// Disease Class Parser
const DiseaseParser = {
  parse: function(className) {
    if (!className) return { crop: 'Unknown', disease: 'Unknown' };
    
    const parts = className.split('___');
    const crop = parts[0] || 'Unknown';
    let disease = parts[1] || 'Unknown';
    
    // Convert underscores to spaces and title case
    disease = disease.replace(/_/g, ' ')
                     .split(' ')
                     .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
                     .join(' ');
    
    return { crop, disease };
  },

  isHealthy: function(className) {
    return className && className.toLowerCase().includes('healthy');
  }
};

window.DiseaseParser = DiseaseParser;

// Confidence Color Helper
const ConfidenceHelper = {
  getClass: function(confidence) {
    if (confidence >= 0.80) return 'confidence-high';
    if (confidence >= 0.65) return 'confidence-medium';
    return 'confidence-low';
  },

  getColor: function(confidence) {
    if (confidence >= 0.80) return 'green';
    if (confidence >= 0.65) return 'yellow';
    return 'red';
  },

  formatPercent: function(confidence) {
    return Math.round(confidence * 100) + '%';
  }
};

window.ConfidenceHelper = ConfidenceHelper;

// Greeting Helper
const GreetingHelper = {
  get: function() {
    const hour = new Date().getHours();
    const t = window.Lang ? Lang.t.bind(Lang) : (k) => k;
    if (hour < 12) return t('greeting_morning');
    if (hour < 17) return t('greeting_afternoon');
    return t('greeting_evening');
  }
};

window.GreetingHelper = GreetingHelper;
