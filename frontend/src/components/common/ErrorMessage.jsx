import React from 'react';
import { AlertCircle } from 'lucide-react';

export const ErrorMessage = ({ message }) => {
  if (!message) return null;
  return (
    <div style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.3)', color: '#F87171', padding: '14px 18px', borderRadius: '12px', display: 'flex', alignItems: 'center', gap: '12px', margin: '16px 0' }}>
      <AlertCircle size={20} style={{ flexShrink: 0 }} />
      <span style={{ fontSize: '0.9rem', fontWeight: 500 }}>{message}</span>
    </div>
  );
};
