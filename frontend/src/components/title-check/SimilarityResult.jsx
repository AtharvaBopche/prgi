import React from 'react';

export const SimilarityResult = ({ title, normalizedTitle, highestSimilarity, status, summary }) => {
  const getBadgeClass = () => {
    if (status === 'ACCEPTED') return 'badge-accepted';
    if (status === 'FLAGGED_FOR_REVIEW') return 'badge-flagged';
    return 'badge-rejected';
  };

  return (
    <div className="glass-panel" style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Submitted Title</span>
          <h2 style={{ fontSize: '1.6rem', color: '#FFF', fontWeight: 700 }}>{title}</h2>
          <code style={{ fontSize: '0.8rem', color: 'var(--accent-cyan)', background: 'rgba(6, 182, 212, 0.1)', padding: '2px 8px', borderRadius: '4px' }}>
            Canonical: {normalizedTitle}
          </code>
        </div>
        <span className={`badge ${getBadgeClass()}`} style={{ fontSize: '0.9rem', padding: '6px 16px' }}>
          {status.replace(/_/g, ' ')}
        </span>
      </div>

      <div style={{ borderTop: '1px solid var(--border-color)', paddingTop: '16px', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '16px' }}>
        <div style={{ background: 'rgba(15, 23, 42, 0.5)', padding: '12px 16px', borderRadius: '10px' }}>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Highest Similarity</span>
          <p style={{ fontSize: '1.4rem', fontWeight: 700, color: highestSimilarity >= 70 ? 'var(--accent-rose)' : highestSimilarity >= 40 ? 'var(--accent-amber)' : 'var(--accent-emerald)' }}>
            {highestSimilarity}%
          </p>
        </div>

        <div style={{ background: 'rgba(15, 23, 42, 0.5)', padding: '12px 16px', borderRadius: '10px', gridColumn: 'span 2' }}>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>System Decision Summary</span>
          <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginTop: '4px' }}>{summary}</p>
        </div>
      </div>
    </div>
  );
};
