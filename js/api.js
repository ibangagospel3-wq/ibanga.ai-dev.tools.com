window.IBANGA_API_BASE_URL ||= window.IBANGA_API_URL;

function apiToken() {
  return localStorage.getItem('token');
}

async function apiRequest(path, options = {}) {
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {})
  };

  const token = apiToken();

  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

  const response = await fetch(`${window.IBANGA_API_BASE_URL}${path}`, {
    ...options,
    headers
  });

  const data = await response.json().catch(() => ({}));

  if (response.status === 401) {
    throw new Error(data.detail || 'Your session has expired. Please log in again.');
  }

  if (!response.ok) {
    throw new Error(data.detail || 'Request failed');
  }

  return data;
}

async function registerUser(payload) {
  return apiRequest('/auth/register', {
    method: 'POST',
    body: JSON.stringify(payload)
  });
}

async function loginUser(payload) {
  const data = await apiRequest('/auth/login', {
    method: 'POST',
    body: JSON.stringify(payload)
  });

  localStorage.setItem('token', data.access_token);

  return data;
}

async function logoutUser() {
  try {
    return await apiRequest('/auth/logout', {
      method: 'POST'
    });
  } finally {
    localStorage.removeItem('token');
  }
}

async function getCurrentUser() {
  return apiRequest('/auth/me');
}

async function getProjects() {
  return apiRequest('/projects');
}

async function createProject(project) {
  return apiRequest('/projects', {
    method: 'POST',
    body: JSON.stringify(project)
  });
}

async function updateProject(id, project) {
  return apiRequest(`/projects/${id}`, {
    method: 'PUT',
    body: JSON.stringify(project)
  });
}

async function deleteProjectFromAPI(id) {
  return apiRequest(`/projects/${id}`, {
    method: 'DELETE'
  });
}

async function getLessons(category = '') {
  return apiRequest(
    `/lessons${category ? `?category=${encodeURIComponent(category)}` : ''}`
  );
}

async function completeLessonAPI(id) {
  return apiRequest(`/progress/${id}/complete`, {
    method: 'POST'
  });
}

async function getChallenges() {
  return apiRequest('/challenges');
}

async function submitChallenge(id, payload) {
  return apiRequest(`/challenges/${id}/submit`, {
    method: 'POST',
    body: JSON.stringify(payload)
  });
}

async function sendAIMessageAPI(payload) {
  return apiRequest('/ai/chat', {
    method: 'POST',
    body: JSON.stringify(payload)
  });
}

async function explainCode(payload) {
  return apiRequest('/ai/explain-code', {
    method: 'POST',
    body: JSON.stringify(payload)
  });
}

async function debugCode(payload) {
  return apiRequest('/ai/debug-code', {
    method: 'POST',
    body: JSON.stringify(payload)
  });
}

async function improveCode(payload) {
  return apiRequest('/ai/improve-code', {
    method: 'POST',
    body: JSON.stringify(payload)
  });
}