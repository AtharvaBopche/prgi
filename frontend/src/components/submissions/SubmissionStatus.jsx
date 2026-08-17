import React from 'react';
import { FileCheck, AlertTriangle, XCircle } from 'lucide-react';

export const SubmissionStatus = ({ submissions }) => {
  const total = submissions.length;
  const accepted = submissions.filter(s => s.status === 'ACCEPTED').length;
  const rejected = submissions.filter(s => s.status === 'REJECTED').length;
  const flagged = submissions.filter(s => s.status === 'FLAGGED_FOR_REVIEW').length;

  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '16px', marginBottom: '24px' }}>
      <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
        <div style={{ background: 'rgba(59, 130, 246, 0.15)', padding: '12px', borderRadius: '12px' }}>
          <FileCheck size={24} color="#60A5FA" />
        </div>
        <div>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Total Tracked</span>
          <h4 style={{ fontSize: '1.5rem', color: '#FFF', fontWeight: 700 }}>{total}</h4>
        </div>
      </div>

      <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
        <div style={{ background: 'rgba(16, 185, 129, 0.15)', padding: '12px', borderRadius: '12px' }}>
          <FileCheck size={24} color="#34D399" />
        </div>
        <div>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Eligible / Accepted</span>
          <h4 style={{ fontSize: '1.5rem', color: '#34D399', fontWeight: 700 }}>{accepted}</h4>
        </div>
      </div>

      <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
        <div style={{ background: 'rgba(239, 68, 68, 0.15)', padding: '12px', borderRadius: '12px' }}>
          <XCircle size={24} color="#F87171" />
        </div>
        <div>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Rejected</span>
          <h4 style={{ fontSize: '1.5rem', color: '#F87171', fontWeight: 700 }}>{rejected}</h4>
        </div>
      </div>

      <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
        <div style={{ background: 'rgba(245, 158, 11, 0.15)', padding: '12px', borderRadius: '12px' }}>
          <AlertTriangle size={24} color="#FBBF24" />
        </div>
        <div>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Flagged</span>
          <h4 style={{ fontSize: '1.5rem', color: '#FBBF24', fontWeight: 700 }}>{flagged}</h4>
        </div>
      </div>
    </div>
  );
};
