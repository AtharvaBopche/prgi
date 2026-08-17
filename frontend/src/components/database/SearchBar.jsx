import React from 'react';
import { Search } from 'lucide-react';

export const SearchBar = ({ value, onChange }) => {
  return (
    <div style={{ position: 'relative', flexGrow: 1 }}>
      <input
        type="text"
        className="input-field"
        placeholder="Search PRGI registered titles (e.g. Hindu, Samachar, Express)..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        style={{ paddingLeft: '44px' }}
      />
      <Search
        size={18}
        style={{ position: 'absolute', left: '16px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }}
      />
    </div>
  );
};
