import React from 'react';
import { AlertCircle, CheckCircle2 } from 'lucide-react';

export const GuidelineResult = ({ violations }) => {
  if (!violations || violations.length === 0) {
    return (
      <div className="glass-panel" style={{ padding: '20px', display: 'flex', alignItems: 'center', gap: '12px', background: 'rgba(16, 185, 129, 0.1)' }}>
        <CheckCircle2 size={24} color="#34D399" />
        <div>
          <h4 style={{ color: '#34D399', fontSize: '0.95rem' }}>Guideline Compliance Passed</h4>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>No prohibited words, periodicity modifications, or combined title violations detected.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="glass-panel" style={{ padding: '24px' }}>
      <h3 style={{ fontSize: '1.1rem', color: '#F87171', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <AlertCircle size={20} />
        PRGI Guideline Violations ({violations.length})
      </h3>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {violations.map((violation, idx) => (
          <div
            key={idx}
            style={{
              background: 'rgba(239, 68, 68, 0.1)',
              border: '1px solid rgba(239, 68, 68, 0.25)',
              padding: '14px 18px',
              borderRadius: '12px'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontWeight: 600, color: '#F87171', fontSize: '0.95rem' }}>{violation.message}</span>
              <code style={{ fontSize: '0.75rem', background: 'rgba(0,0,0,0.3)', padding: '2px 8px', borderRadius: '4px', color: '#FCA5A5' }}>
                {violation.code}
              </code>
            </div>
            {violation.details && (
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', marginTop: '6px' }}>
                {violation.details}
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};
