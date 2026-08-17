import React from 'react';
import {
  BookOpen, ShieldAlert, Type, Hash, Link2, User, Star,
  Globe, Flag, Radio, AlertTriangle, FileText
} from 'lucide-react';

const guidelines = [
  {
    number: 1,
    icon: Type,
    color: '#60A5FA',
    bg: 'rgba(59,130,246,0.12)',
    border: 'rgba(59,130,246,0.25)',
    title: 'Multi-Word & Meaningful Titles',
    text: 'The proposed titles should preferably contain more than one word formed by combining distinct and meaningful terms. Generic, or root word titles shall not be registered.',
    examples: ['Manthan', 'Darpan', 'Inspire', 'Success', 'Khulasa', 'Rahasya', 'Katha', 'Herald', 'Malar', 'Mukhi', 'Nukkad'],
    exampleLabel: 'Examples of disallowed generic/root words'
  },
  {
    number: 2,
    icon: ShieldAlert,
    color: '#34D399',
    bg: 'rgba(16,185,129,0.12)',
    border: 'rgba(16,185,129,0.25)',
    title: 'Uniqueness & Phonetic Similarity',
    text: 'The proposed titles must be unique and shall not be phonetically or visually similar to any existing registered title whether in the same language across India or any other language within the same State.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 3,
    icon: AlertTriangle,
    color: '#FBBF24',
    bg: 'rgba(245,158,11,0.12)',
    border: 'rgba(245,158,11,0.25)',
    title: 'Prohibited Negative Connotations',
    text: 'Titles should be meaningful and clear. Titles with negative connotations with religious sentiments, obscene, absurd or offensive to public sentiments or those that could be misused with words like "crime", "corruption" etc. will not be registered.',
    examples: ['Crime', 'Corruption'],
    exampleLabel: 'Examples of disallowed terms'
  },
  {
    number: 4,
    icon: Hash,
    color: '#A78BFA',
    bg: 'rgba(139,92,246,0.12)',
    border: 'rgba(139,92,246,0.25)',
    title: 'Abbreviations & Numerals',
    text: 'Abbreviations, acronyms or numerals will be considered only if they are meaningfully and appropriately attached with other words.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 5,
    icon: Link2,
    color: '#F87171',
    bg: 'rgba(239,68,68,0.12)',
    border: 'rgba(239,68,68,0.25)',
    title: 'Combination of Existing Titles',
    text: 'Titles that combine existing registered titles whether in full, in part or by rearranging words or inserting non-distinctive terms that do not create a significantly different title will not be registered.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 6,
    icon: User,
    color: '#38BDF8',
    bg: 'rgba(56,189,248,0.12)',
    border: 'rgba(56,189,248,0.25)',
    title: 'Individual Names as Titles',
    text: "Titles denoting the name of an individual should not be the names of the owner or publisher of the proposed periodical.",
    examples: ['Rajan Times', 'Deepak Samachar', 'Jitendra News'],
    exampleLabel: 'Disallowed examples'
  },
  {
    number: 7,
    icon: Star,
    color: '#FB923C',
    bg: 'rgba(251,146,60,0.12)',
    border: 'rgba(251,146,60,0.25)',
    title: 'Non-Text Characters & Symbols',
    text: 'Titles containing non-text characters, or any form of signs, symbols including mathematical symbols (like "+", "*", etc.), pictographs, photographs, hallmarks, logos, monograms, phonograms, emojis, etc. are not allowed.',
    examples: ['+', '*', '©', '™', 'Emojis'],
    exampleLabel: 'Disallowed characters'
  },
  {
    number: 8,
    icon: Type,
    color: '#C084FC',
    bg: 'rgba(192,132,252,0.12)',
    border: 'rgba(192,132,252,0.25)',
    title: 'Disallowed Prefixes / Suffixes',
    text: 'Titles formed by insignificantly prefixing or suffixing generic or repetitive terms to an existing title will not be approved. This includes addition of city/state names, periodicity or language terms, or articles/prepositions/adjectives to an existing title.',
    examples: ['The Times', 'Daily', 'Dainik', 'Weekly', 'Vartha', 'Aaj', 'Today', 'Express', 'News', 'Khabar', 'Samachar', 'India', 'National', 'Rashtriya', 'Saptahik Weekly', 'Sandhya Evening', 'Daily Dainik News'],
    exampleLabel: 'Examples of disallowed prefix/suffix modifications'
  },
  {
    number: 9,
    icon: ShieldAlert,
    color: '#F43F5E',
    bg: 'rgba(244,63,94,0.12)',
    border: 'rgba(244,63,94,0.25)',
    title: 'Judicial & Legal Violations',
    text: 'The proposed title shall not be registered if it is found to be in violation of any judicial pronouncement including matters involving copyright, trademark infringement, contempt of court and defamation.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 10,
    icon: Flag,
    color: '#34D399',
    bg: 'rgba(16,185,129,0.12)',
    border: 'rgba(16,185,129,0.25)',
    title: 'Sovereignty & Public Order',
    text: 'Titles containing words which can be construed as affecting the sovereignty and integrity of India, Security of the State, International Relations, Public order, Morality and public decency, incite unrest or disorder etc. will not be registered.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 11,
    icon: Star,
    color: '#FBBF24',
    bg: 'rgba(245,158,11,0.12)',
    border: 'rgba(245,158,11,0.25)',
    title: 'National Symbols & Government Association',
    text: 'Titles similar to any national symbol, national motto, or suggesting misleading association with Central/State Governments, Local bodies, Constitutional or Statutory bodies or violative of The Emblems and Names (Prevention of Improper Use) Act, 1950 will not be registered.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 12,
    icon: ShieldAlert,
    color: '#F87171',
    bg: 'rgba(239,68,68,0.12)',
    border: 'rgba(239,68,68,0.25)',
    title: 'Government & Regulatory Organizations',
    text: 'Titles containing names of Government Organizations, Departments, Regulatory/Enforcement Agencies, Foreign Governments, International Organizations or words like Sarkar, Government, Parliament shall not be registered.',
    examples: ['Police', 'Bureau', 'Investigation Department', 'Vigilance', 'CID', 'CBI', 'Commission', 'Defence', 'UN', 'WHO', 'ILO', 'Sarkar', 'Parliament'],
    exampleLabel: 'Disallowed terms'
  },
  {
    number: 13,
    icon: Globe,
    color: '#38BDF8',
    bg: 'rgba(56,189,248,0.12)',
    border: 'rgba(56,189,248,0.25)',
    title: 'Foreign Country / Place Names',
    text: 'Titles suggesting any association with a foreign country, city, or place which does not correspond to the State or place of publication of the periodical shall not be registered.',
    examples: ['South Africa Times', 'Canada Times', 'New York Mirror'],
    exampleLabel: 'Disallowed examples'
  },
  {
    number: 14,
    icon: User,
    color: '#A78BFA',
    bg: 'rgba(139,92,246,0.12)',
    border: 'rgba(139,92,246,0.25)',
    title: 'Names of National Leaders',
    text: 'Titles with the names of national leaders or those resembling the names of prominent national leaders, Heads of Government, and functionaries of Central and State governments will not be registered. However, names of recognized national and state political parties will be considered if applied by the concerned organization.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 15,
    icon: Radio,
    color: '#FB923C',
    bg: 'rgba(251,146,60,0.12)',
    border: 'rgba(251,146,60,0.25)',
    title: 'TV Channel / Radio Station Titles',
    text: 'Title registered as a Satellite TV Channel/FM Radio/Community Radio Station with the Ministry of Information and Broadcasting shall not be registered unless the application is made by their owner or by their representative on his behalf.',
    examples: ['News Nation', 'News Time', 'Aajtak News', 'Akaashvani Times', 'Dabang News'],
    exampleLabel: 'Protected channel title examples'
  },
  {
    number: 16,
    icon: BookOpen,
    color: '#34D399',
    bg: 'rgba(16,185,129,0.12)',
    border: 'rgba(16,185,129,0.25)',
    title: 'Well-Known Periodical Titles',
    text: 'Titles resembling the titles of well-known periodicals if applied by anyone other than the existing owner of the well-known title shall not be registered. This is to avoid any false/misleading impression of association with the well-known periodical.',
    examples: [],
    exampleLabel: ''
  },
  {
    number: 17,
    icon: FileText,
    color: '#C084FC',
    bg: 'rgba(192,132,252,0.12)',
    border: 'rgba(192,132,252,0.25)',
    title: 'Non-Periodical Publications',
    text: 'Titles using words like Ad or Advertisement, Classifieds, Tender, Calendar, Panchang, Matrimonial, Yellow pages, pamphlet, brochure, directory, or any such publication which cannot be treated as a periodical shall not be registered.',
    examples: ['Advertisement', 'Classifieds', 'Tender', 'Calendar', 'Panchang', 'Matrimonial', 'Yellow Pages', 'Directory'],
    exampleLabel: 'Disallowed terms'
  },
  {
    number: 18,
    icon: ShieldAlert,
    color: '#F43F5E',
    bg: 'rgba(244,63,94,0.12)',
    border: 'rgba(244,63,94,0.25)',
    title: 'New Editions & Transfer Restrictions',
    text: 'Registration of new editions and transfer of ownership of an existing periodical with a title falling in the categories specified under points 3 and 9 to 13 of these guidelines will not be considered.',
    examples: [],
    exampleLabel: ''
  }
];

const GuidelineCard = ({ g }) => {
  const Icon = g.icon;

  return (
    <div
      className="glass-panel"
      style={{
        padding: '20px 24px',
        borderLeft: `3px solid ${g.color}`,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '14px', marginBottom: '14px' }}>
        <div style={{ background: g.bg, border: `1px solid ${g.border}`, padding: '10px', borderRadius: '10px', flexShrink: 0 }}>
          <Icon size={20} color={g.color} />
        </div>
        <div>
          <span style={{ fontSize: '0.72rem', color: g.color, textTransform: 'uppercase', letterSpacing: '0.08em', fontWeight: 700 }}>
            Guideline {g.number}
          </span>
          <h3 style={{ fontSize: '1rem', color: '#FFF', fontWeight: 600, marginTop: '2px' }}>{g.title}</h3>
        </div>
      </div>

      <div style={{ paddingTop: '14px', borderTop: `1px solid ${g.border}` }}>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.93rem', lineHeight: '1.7' }}>{g.text}</p>

        {g.examples && g.examples.length > 0 && (
          <div style={{ marginTop: '14px' }}>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              {g.exampleLabel}:
            </span>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginTop: '8px' }}>
              {g.examples.map((ex, i) => (
                <span key={i} style={{
                  background: g.bg,
                  border: `1px solid ${g.border}`,
                  color: g.color,
                  padding: '3px 12px',
                  borderRadius: '9999px',
                  fontSize: '0.82rem',
                  fontWeight: 500
                }}>
                  {ex}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export const Guidelines = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px', paddingBottom: '48px' }}>

      {/* Header */}
      <div className="glass-panel" style={{ padding: '32px', background: 'linear-gradient(135deg, rgba(37,99,235,0.15), rgba(139,92,246,0.15))', textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '10px', background: 'rgba(59,130,246,0.15)', border: '1px solid rgba(59,130,246,0.3)', padding: '6px 18px', borderRadius: '9999px', marginBottom: '16px' }}>
          <BookOpen size={16} color="#60A5FA" />
          <span style={{ fontSize: '0.8rem', color: '#60A5FA', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
            Official PRGI Policy Document
          </span>
        </div>
        <h2 style={{ fontSize: '1.9rem', color: '#FFF', fontWeight: 800, lineHeight: 1.3 }}>
          Guidelines for Admissibility of Titles<br />
          <span style={{ color: '#60A5FA' }}>for Registration of Periodicals</span>
        </h2>
        <p style={{ color: 'var(--text-secondary)', marginTop: '12px', fontSize: '0.95rem', maxWidth: '700px', margin: '12px auto 0' }}>
          Issued under Section 5(3)(C) read with Section 2(g) of the Press and Registration of Periodicals Act 2023.
          Effective from <strong style={{ color: '#FFF' }}>01 July 2025</strong>.
        </p>

        <div style={{ display: 'flex', justifyContent: 'center', flexWrap: 'wrap', gap: '16px', marginTop: '24px' }}>
          {[
            { label: 'Issuing Authority', value: 'Press Registrar General of India' },
            { label: 'Ministry', value: 'Information & Broadcasting' },
            { label: 'Total Guidelines', value: '18 Rules' },
          ].map((item, i) => (
            <div key={i} style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid var(--border-color)', padding: '10px 20px', borderRadius: '10px', textAlign: 'center' }}>
              <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)', textTransform: 'uppercase', display: 'block' }}>{item.label}</span>
              <strong style={{ color: '#FFF', fontSize: '0.9rem' }}>{item.value}</strong>
            </div>
          ))}
        </div>
      </div>

      {/* Preface */}
      <div className="glass-panel" style={{ padding: '20px 24px', borderLeft: '3px solid rgba(59,130,246,0.5)' }}>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.75 }}>
          These guidelines are implemented with effect from <strong style={{ color: '#FFF' }}>01.07.2025</strong>, superseding all earlier guidelines issued from time to time. 
          Applicants are advised to refer to the complete list of already registered titles accessible on PRGI's website before proposing new titles, and adhere to these guidelines while applying through the <strong style={{ color: '#FFF' }}>Press Sewa Portal</strong>.
        </p>
      </div>

      {/* Guideline Cards */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {guidelines.map(g => <GuidelineCard key={g.number} g={g} />)}
      </div>
    </div>
  );
};
