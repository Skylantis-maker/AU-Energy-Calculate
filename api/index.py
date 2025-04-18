from flask import Flask
from backend.app import app

# Vercel handler
def handler(request):
    return app 