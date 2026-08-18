import React from 'react';

export const TitleTable = ({ items, loading }) => {
  if (loading) {
    return (
      <div className="glass-panel" style={{ padding: '40px', textAlign: 'center', color: 'var(--text-secondary)' }}>
        Loading registered titles from PRGI Database...
      </div>
    );
  }

  if (!items || items.length === 0) {
    return (
      <div className="glass-panel" style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
        No titles match your search criteria.
      </div>
    );
  }

  return (
    <div className="glass-panel" style={{ overflow: 'hidden' }}>
      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
          <thead>
            <tr style={{ background: 'rgba(15, 23, 42, 0.8)', borderBottom: '1px solid var(--border-color)' }}>
              <th style={{ padding: '16px 20px', color: 'var(--text-muted)', fontSize: '0.8rem', textTransform: 'uppercase' }}>S.No</th>
              <th style={{ padding: '16px 20px', color: 'var(--text-muted)', fontSize: '0.8rem', textTransform: 'uppercase' }}>Publication Title</th>
              <th style={{ padding: '16px 20px', color: 'var(--text-muted)', fontSize: '0.8rem', textTransform: 'uppercase' }}>Language</th>
            </tr>
          </thead>
          <tbody>
            {items.map((row, idx) => (
              <tr key={idx} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)', transition: 'background 0.2s ease' }}>
                <td style={{ padding: '14px 20px', color: 'var(--text-muted)', fontSize: '0.85rem' }}>#{row.sn || row.id}</td>
                <td style={{ padding: '14px 20px', color: '#FFF', fontWeight: 600, fontSize: '0.95rem' }}>
                  {row.title}
                  {row.reg_no && row.reg_no !== '-' && (
                    <span style={{ display: 'block', fontSize: '0.75rem', color: 'var(--accent-cyan)', marginTop: '2px' }}>
                      Reg: {row.reg_no}
                    </span>
                  )}
                </td>
                <td style={{ padding: '14px 20px', color: 'var(--text-secondary)', fontSize: '0.85rem' }}>
                  <span style={{ background: 'rgba(255, 255, 255, 0.06)', padding: '2px 8px', borderRadius: '4px' }}>
                    {row.language || 'English'}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
