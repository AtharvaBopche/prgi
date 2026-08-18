import { useState, useEffect } from 'react';
import { getSubmissionsApi } from '../services/api';

export const useSubmissions = () => {
  const [submissions, setSubmissions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchSubmissions = async () => {
    setLoading(true);
    setError(null);
    try {
      const remoteData = await getSubmissionsApi();
      setSubmissions(remoteData);
    } catch (err) {
      setSubmissions([]);
      setError('Could not load submission history from the database.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSubmissions();
  }, []);

  return { submissions, loading, error, refreshSubmissions: fetchSubmissions };
};
