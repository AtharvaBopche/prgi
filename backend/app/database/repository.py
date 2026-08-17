import json
import uuid
from typing import List, Dict, Any, Tuple
from app.database.connection import get_db_connection
from app.services.preprocessing.normalizer import normalize_title
from app.services.verification.phonetic import get_soundex
from app.core.config import CANDIDATE_SEARCH_LIMIT

class TitleRepository:
    def get_candidate_titles(self, title: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Retrieves candidate titles from the database and submission history using:
        1. Exact prefix matching
        2. Token / word matching
        3. Soundex phonetic matching
        4. Trigram / Substring matching
        Returns (db_candidates, submission_candidates).
        """
        norm = normalize_title(title)
        soundex = get_soundex(title)
        tokens = norm.split()
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        candidates = {}
        
        # 1. Phonetic matching
        if soundex:
            cursor.execute("SELECT id, title, normalized_title, 'database' as source FROM prgi_titles WHERE soundex_code = ? LIMIT 200", (soundex,))
            for row in cursor.fetchall():
                candidates[row['id']] = dict(row)

        # 2. Token-based matching (matching any individual token)
        for token in tokens:
            if len(token) >= 3:
                cursor.execute(
                    "SELECT id, title, normalized_title, 'database' as source FROM prgi_titles WHERE normalized_title LIKE ? LIMIT 100",
                    (f"%{token}%",)
                )
                for row in cursor.fetchall():
                    candidates[row['id']] = dict(row)

        # If candidates set is small, fallback to top titles for candidate coverage
        if len(candidates) < 100:
            cursor.execute("SELECT id, title, normalized_title, 'database' as source FROM prgi_titles LIMIT ?", (CANDIDATE_SEARCH_LIMIT,))
            for row in cursor.fetchall():
                if row['id'] not in candidates:
                    candidates[row['id']] = dict(row)
                    
        db_candidates = list(candidates.values())

        # Retrieve prior submission candidates
        cursor.execute("SELECT id, submitted_title as title, normalized_title, 'submission_history' as source FROM submissions LIMIT 500")
        sub_candidates = [dict(row) for row in cursor.fetchall()]

        conn.close()
        return db_candidates, sub_candidates

    def get_all_registered_titles_set(self) -> set:
        """Returns set of all registered normalized titles for combination checks."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT normalized_title FROM prgi_titles")
        titles = {row['normalized_title'] for row in cursor.fetchall()}
        
        # Add submitted normalized titles
        cursor.execute("SELECT normalized_title FROM submissions WHERE status = 'ACCEPTED'")
        for row in cursor.fetchall():
            titles.add(row['normalized_title'])
            
        conn.close()
        return titles

    def get_paginated_titles(self, page: int = 1, limit: int = 20, search: str = "", language: str = "") -> Dict[str, Any]:
        """Returns paginated database titles with optional search & filter."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        offset = (page - 1) * limit
        query = "SELECT * FROM prgi_titles WHERE 1=1"
        params = []
        
        if search:
            query += " AND (title LIKE ? OR normalized_title LIKE ?)"
            params.extend([f"%{search}%", f"%{search.upper()}%"])
            
        if language and language.lower() != "all":
            query += " AND language = ?"
            params.append(language)
            
        # Count total
        count_query = query.replace("SELECT *", "SELECT COUNT(*)")
        cursor.execute(count_query, params)
        total_records = cursor.fetchone()[0]
        
        query += " ORDER BY title ASC LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        
        cursor.execute(query, params)
        items = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        
        return {
            "items": items,
            "total": total_records,
            "page": page,
            "limit": limit,
            "total_pages": (total_records + limit - 1) // limit if limit > 0 else 1
        }

    def save_submission(
        self,
        submitted_title: str,
        normalized_title: str,
        similarity_score: float,
        verification_probability: float,
        status: str,
        rejection_reasons: List[str]
    ) -> Dict[str, Any]:
        """Saves a title submission record into database for history tracking."""
        app_id = f"PRGI-{uuid.uuid4().hex[:8].upper()}"
        conn = get_db_connection()
        cursor = conn.cursor()
        
        reasons_json = json.dumps(rejection_reasons)
        
        cursor.execute("""
            INSERT INTO submissions (
                application_id, submitted_title, normalized_title,
                similarity_score, verification_probability, status, rejection_reasons
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (app_id, submitted_title, normalized_title, similarity_score, verification_probability, status, reasons_json))
        
        conn.commit()
        sub_id = cursor.lastrowid
        
        cursor.execute("SELECT * FROM submissions WHERE id = ?", (sub_id,))
        row = dict(cursor.fetchone())
        row['rejection_reasons'] = json.loads(row['rejection_reasons'])
        
        conn.close()
        return row

    def get_all_submissions(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Returns recent user submissions."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM submissions ORDER BY submitted_at DESC LIMIT ?", (limit,))
        rows = [dict(r) for r in cursor.fetchall()]
        for r in rows:
            if r.get('rejection_reasons'):
                try:
                    r['rejection_reasons'] = json.loads(r['rejection_reasons'])
                except Exception:
                    r['rejection_reasons'] = []
            else:
                r['rejection_reasons'] = []
        conn.close()
        return rows

    def get_db_stats(self) -> Dict[str, Any]:
        """Returns overall database stats."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM prgi_titles")
        total_titles = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM submissions")
        total_submissions = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM submissions WHERE status = 'ACCEPTED'")
        accepted_submissions = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM submissions WHERE status = 'REJECTED'")
        rejected_submissions = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            "total_registered_titles": total_titles,
            "total_submissions": total_submissions,
            "accepted_submissions": accepted_submissions,
            "rejected_submissions": rejected_submissions
        }

repo = TitleRepository()
