// Auth Guard - Protects routes that require authentication
document.addEventListener('DOMContentLoaded', function() {
  const page = document.querySelector('.auth-protected');
  
  if (!page) return;

  fetch('/api/me', { credentials: 'include' })
    .then(response => {
      if (response.status === 401) {
        window.location.href = '/auth.html';
        return null;
      }
      return response.json();
    })
    .then(data => {
      if (data) {
        const user = data.user || data;
        window.currentUser = user;
        sessionStorage.setItem('agritech_user', JSON.stringify(user));
        page.classList.add('loaded');
        
        // Dispatch custom event for other scripts
        window.dispatchEvent(new CustomEvent('userLoaded', { detail: user }));
      }
    })
    .catch(error => {
      console.error('Auth check failed:', error);
      window.location.href = '/auth.html';
    });
});
