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
      // 1. Fetch from backend API
      const remoteData = await getSubmissionsApi();
      
      // 2. Merge with local storage history so items stay in frontend even across page reloads
      const localHistory = JSON.parse(localStorage.getItem('prgi_submission_history') || '[]');
      
      // Merge unique by title
      const combinedMap = new Map();
      localHistory.forEach(item => {
        combinedMap.set(item.submitted_title, {
          submitted_title: item.submitted_title,
          similarity_score: item.highest_similarity || item.similarity_score,
          verification_probability: item.verification_probability,
          status: item.status,
          rejection_reasons: item.guideline_violations ? item.guideline_violations.map(v => v.message) : (item.rejection_reasons || []),
          submitted_at: item.processed_at || item.submitted_at || new Date().toISOString()
        });
      });

      remoteData.forEach(item => {
        if (!combinedMap.has(item.submitted_title)) {
          combinedMap.set(item.submitted_title, item);
        }
      });

      setSubmissions(Array.from(combinedMap.values()));
    } catch (err) {
      // Fallback to local storage if backend offline
      const localHistory = JSON.parse(localStorage.getItem('prgi_submission_history') || '[]');
      setSubmissions(localHistory);
      setError('Could not sync with backend database. Showing local session history.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSubmissions();
  }, []);

  return { submissions, loading, error, refreshSubmissions: fetchSubmissions };
};
