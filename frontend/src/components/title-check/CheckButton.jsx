import React from 'react';
import { ShieldCheck } from 'lucide-react';

export const CheckButton = ({ onClick, loading, disabled }) => {
  return (
    <button
      className="btn-primary"
      onClick={onClick}
      disabled={disabled || loading}
      style={{ height: '54px', padding: '0 28px', fontSize: '1rem', whiteSpace: 'nowrap' }}
    >
      <ShieldCheck size={20} />
      {loading ? 'Verifying Title...' : 'Verify Title'}
    </button>
  );
};
