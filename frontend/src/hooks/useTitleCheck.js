import { useState } from 'react';
import { verifyTitleApi } from '../services/api';

export const useTitleCheck = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const checkTitle = async (title, ownerName = '') => {
    if (!title || !title.trim()) return null;
    setLoading(true);
    setError(null);
    try {
      const data = await verifyTitleApi(title, ownerName);
      setResult(data);
      return data;
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to complete title verification request.');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const resetResult = () => {
    setResult(null);
    setError(null);
  };

  return { loading, result, error, checkTitle, resetResult };
};
