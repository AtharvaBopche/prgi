import React from 'react';

export const FilterBar = ({ language, onLanguageChange }) => {
  const languages = ["all", "English", "Hindi", "Gujarati", "Marathi", "Bengali", "Tamil", "Telugu", "Malayalam"];

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
      <label style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Language:</label>
      <select
        className="input-field"
        value={language}
        onChange={(e) => onLanguageChange(e.target.value)}
        style={{ width: 'auto', padding: '10px 14px', fontSize: '0.9rem', cursor: 'pointer' }}
      >
        {languages.map(lang => (
          <option key={lang} value={lang} style={{ background: '#0F172A', color: '#FFF' }}>
            {lang === 'all' ? 'All Languages' : lang}
          </option>
        ))}
      </select>
    </div>
  );
};
