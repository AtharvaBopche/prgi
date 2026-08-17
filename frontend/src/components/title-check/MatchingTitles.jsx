import React from 'react';
import { Layers, Volume2, Database, History } from 'lucide-react';

export const MatchingTitles = ({ matches }) => {
  if (!matches || matches.length === 0) {
    return (
      <div className="glass-panel" style={{ padding: '24px', textAlign: 'center' }}>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>No close matching registered titles found in database.</p>
      </div>
    );
  }

  return (
    <div className="glass-panel" style={{ padding: '24px' }}>
      <h3 style={{ fontSize: '1.1rem', color: '#FFF', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <Layers size={18} color="var(--accent-blue)" />
        Matching Registered Titles & Applications ({matches.length})
      </h3>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {matches.map((item, idx) => (
          <div
            key={idx}
            style={{
              background: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid var(--border-color)',
              padding: '14px 18px',
              borderRadius: '12px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }}
          >
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontWeight: 600, color: '#FFF', fontSize: '1.05rem' }}>{item.title}</span>
                {item.phonetic_match && (
                  <span style={{ background: 'rgba(139, 92, 246, 0.2)', color: '#A78BFA', padding: '2px 8px', borderRadius: '6px', fontSize: '0.75rem', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <Volume2 size={12} /> Phonetic Match
                  </span>
                )}
              </div>
              <div style={{ display: 'flex', gap: '12px', marginTop: '4px', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                  {item.source === 'database' ? <Database size={12} /> : <History size={12} />}
                  {item.source === 'database' ? 'Registered PRGI DB' : 'Prior User Application'}
                </span>
                <span>Type: <strong style={{ color: 'var(--text-secondary)' }}>{item.match_type.toUpperCase()}</strong></span>
              </div>
            </div>

            <div style={{ textAlign: 'right' }}>
              <span style={{ fontSize: '1.2rem', fontWeight: 700, color: item.similarity_percentage >= 70 ? 'var(--accent-rose)' : 'var(--accent-amber)' }}>
                {item.similarity_percentage}%
              </span>
              <span style={{ display: 'block', fontSize: '0.7rem', color: 'var(--text-muted)' }}>Match</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
