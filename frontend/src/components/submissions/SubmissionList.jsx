import React from 'react';
import { SubmissionCard } from './SubmissionCard';
import { History } from 'lucide-react';

export const SubmissionList = ({ submissions }) => {
  if (!submissions || submissions.length === 0) {
    return (
      <div className="glass-panel" style={{ padding: '40px', textAlign: 'center' }}>
        <History size={48} color="var(--text-muted)" style={{ marginBottom: '12px', opacity: 0.5 }} />
        <h3 style={{ color: 'var(--text-secondary)' }}>No Submission History Found</h3>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '4px' }}>
          Submit proposed titles on the Title Checker tab to populate application history.
        </p>
      </div>
    );
  }

  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '20px' }}>
      {submissions.map((sub, idx) => (
        <SubmissionCard key={idx} submission={sub} />
      ))}
    </div>
  );
};
