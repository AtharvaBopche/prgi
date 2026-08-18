"""Vercel entry point for the FastAPI backend.

Vercel recognises the exported ``app`` object and serves it at ``/api``.
The application itself stays in ``backend/app`` so local development remains
unchanged.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_ROOT = PROJECT_ROOT / "backend"

if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.main import app  # noqa: E402
