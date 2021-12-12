from flask import request, render_template, make_response, app
# from app import app
from models import db, Project

@app.route('/', methods = ['GET'])
def project_records():
    name = request.args.get('name')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if name and start_date and end_date:
        new_project = Project(
            name=name,
            start_date=start_date,
            end_date=end_date
        )
        db.session.add(new_project) # doaje nowy rekord
        db.session.commit() # zatwierdza nowy rekord
    return make_response(f"{new_project} successfully added!")



