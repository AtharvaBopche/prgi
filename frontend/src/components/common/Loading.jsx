import React from 'react';
import { Loader2 } from 'lucide-react';

export const Loading = ({ text = 'Verifying title against 160,000+ PRGI registered titles...' }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '40px', gap: '16px' }}>
      <Loader2 size={40} className="animate-spin" style={{ color: 'var(--accent-blue)', animation: 'spin 1s linear infinite' }} />
      <p style={{ color: 'var(--text-secondary)', fontWeight: 500, fontSize: '0.95rem' }}>{text}</p>
      <style>{`
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
};
