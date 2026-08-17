import React from 'react';

export const Button = ({ children, onClick, disabled, variant = 'primary', type = 'button', style = {} }) => {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={variant === 'primary' ? 'btn-primary' : ''}
      style={{
        ...style,
        opacity: disabled ? 0.6 : 1,
        cursor: disabled ? 'not-allowed' : 'pointer'
      }}
    >
      {children}
    </button>
  );
};
