import React from 'react';
import { SubmissionStatus } from '../components/submissions/SubmissionStatus';
import { SubmissionList } from '../components/submissions/SubmissionList';
import { Loading } from '../components/common/Loading';
import { ErrorMessage } from '../components/common/ErrorMessage';
import { useSubmissions } from '../hooks/useSubmissions';

export const PreviousSubmissions = () => {
  const { submissions, loading, error } = useSubmissions();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      <div>
        <h2 style={{ fontSize: '1.8rem', color: '#FFF', fontWeight: 700 }}>Application Submission History</h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', marginTop: '4px' }}>
          Saved verification requests from the application database.
        </p>
      </div>

      {error && <ErrorMessage message={error} />}
      {loading ? <Loading text="Loading saved submissions..." /> : <>
        <SubmissionStatus submissions={submissions} />
        <SubmissionList submissions={submissions} />
      </>}
    </div>
  );
};
