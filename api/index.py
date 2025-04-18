import sys
import os
from flask import Flask

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import app

# Vercel serverless function handler
def handler(request):
    """Handle requests for Vercel serverless functions"""
    return app 