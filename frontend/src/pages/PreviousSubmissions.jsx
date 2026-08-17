import React from 'react';
import { SubmissionStatus } from '../components/submissions/SubmissionStatus';
import { SubmissionList } from '../components/submissions/SubmissionList';

export const PreviousSubmissions = ({ submissions = [] }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      <div>
        <h2 style={{ fontSize: '1.8rem', color: '#FFF', fontWeight: 700 }}>Application Submission History</h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', marginTop: '4px' }}>
          Session history of checked publication titles. <i>(Note: This list is stored in frontend session memory and clears upon page reload)</i>.
        </p>
      </div>

      <SubmissionStatus submissions={submissions} />

      <SubmissionList submissions={submissions} />
    </div>
  );
};
