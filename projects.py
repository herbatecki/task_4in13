# projects.py

from app import app, db
from app.models import Project

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Project": Project
    }
