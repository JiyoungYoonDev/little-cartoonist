const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

export async function fetchTeachers() {
  const response = await fetch(`${API_BASE_URL}/teachers`);
  if (!response.ok) throw new Error('Failed to fetch teachers');
  return response.json();
}

export async function fetchThemes() {
  const response = await fetch(`${API_BASE_URL}/themes`);
  if (!response.ok) throw new Error('Failed to fetch themes');
  return response.json();
}

export async function requestMockAssist(payload) {
  try {
    const response = await fetch(`${API_BASE_URL}/assists/mock`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error('Failed to request assist');
    }

    return response.json();
  } catch (error) {
    return {
      inferred_intent: 'encouragement',
      teacher_line: "Nice start! Let's draw together.",
      assist_strokes: [],
      expression: 'happy',
    };
  }
}
