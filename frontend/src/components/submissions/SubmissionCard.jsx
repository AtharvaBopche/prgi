import React from 'react';
import { Calendar, Hash, FileText } from 'lucide-react';

export const SubmissionCard = ({ submission }) => {
  const getStatusBadge = (status) => {
    if (status === 'ACCEPTED') return <span className="badge badge-accepted">Accepted</span>;
    if (status === 'FLAGGED_FOR_REVIEW') return <span className="badge badge-flagged">Flagged</span>;
    return <span className="badge badge-rejected">Rejected</span>;
  };

  const formattedDate = new Date(submission.submitted_at || Date.now()).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });

  return (
    <div className="glass-panel" style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <FileText size={16} color="var(--accent-blue)" />
            <h3 style={{ fontSize: '1.2rem', color: '#FFF', fontWeight: 700 }}>{submission.submitted_title}</h3>
          </div>
          {submission.application_id && (
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px', marginTop: '2px' }}>
              <Hash size={12} /> {submission.application_id}
            </span>
          )}
        </div>
        {getStatusBadge(submission.status)}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px', background: 'rgba(15, 23, 42, 0.5)', padding: '12px', borderRadius: '10px' }}>
        <div>
          <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Highest Similarity</span>
          <p style={{ fontWeight: 700, color: 'var(--text-primary)' }}>{submission.similarity_score}%</p>
        </div>
        <div>
          <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Verification Prob.</span>
          <p style={{ fontWeight: 700, color: submission.verification_probability > 50 ? '#34D399' : '#F87171' }}>
            {submission.verification_probability}%
          </p>
        </div>
      </div>

      {submission.rejection_reasons && submission.rejection_reasons.length > 0 && (
        <div style={{ fontSize: '0.8rem', color: '#F87171', background: 'rgba(239, 68, 68, 0.1)', padding: '8px 12px', borderRadius: '8px' }}>
          <strong>Reasons:</strong> {submission.rejection_reasons.join(', ')}
        </div>
      )}

      <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px', borderTop: '1px solid var(--border-color)', paddingTop: '10px' }}>
        <Calendar size={12} /> {formattedDate}
      </div>
    </div>
  );
};
