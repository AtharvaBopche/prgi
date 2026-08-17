import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_URL
  ? `${import.meta.env.VITE_API_URL}/api`
  : '/api';

export const verifyTitleApi = async (title, ownerName = '') => {
  const response = await axios.post(`${API_BASE}/title-check/verify`, {
    title,
    owner_name: ownerName
  });
  return response.data;
};

export const getSubmissionsApi = async (limit = 100) => {
  const response = await axios.get(`${API_BASE}/submissions/`, {
    params: { limit }
  });
  return response.data;
};

export const getDatabaseTitlesApi = async (page = 1, limit = 20, search = '', language = 'all') => {
  const response = await axios.get(`${API_BASE}/database/titles`, {
    params: { page, limit, search, language }
  });
  return response.data;
};

export const getDatabaseStatsApi = async () => {
  const response = await axios.get(`${API_BASE}/database/stats`);
  return response.data;
};
