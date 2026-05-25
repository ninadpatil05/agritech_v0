// API Helper Module
const API = {
  get: (path) =>
    fetch('/api' + path, { credentials: 'include' }).then(r => r.json()),

  post: (path, body) =>
    fetch('/api' + path, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    }).then(r => r.json()),

  postForm: (path, formData) =>
    fetch('/api' + path, {
      method: 'POST',
      credentials: 'include',
      body: formData
    }).then(r => r.json()),

  del: (path) =>
    fetch('/api' + path, {
      method: 'DELETE',
      credentials: 'include'
    }).then(r => r.json()),
};

window.API = API;
