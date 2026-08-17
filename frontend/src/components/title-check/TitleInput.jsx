import React from 'react';
import { Search } from 'lucide-react';

export const TitleInput = ({ value, onChange, onSubmit, disabled }) => {
  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !disabled) {
      onSubmit();
    }
  };

  return (
    <div style={{ position: 'relative', width: '100%' }}>
      <input
        type="text"
        className="input-field"
        placeholder="Enter proposed publication title (e.g., Namascar, Police News, Daily Evening)..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={disabled}
        style={{ paddingLeft: '48px', height: '54px', fontSize: '1.05rem' }}
      />
      <Search
        size={20}
        style={{ position: 'absolute', left: '16px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }}
      />
    </div>
  );
};
