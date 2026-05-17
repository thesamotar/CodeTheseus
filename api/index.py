"""
Vercel Serverless Function Entry Point
Adapts FastAPI app for Vercel's serverless environment
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.api.main import app

# Vercel expects a handler function
handler = app

# Made with Bob
