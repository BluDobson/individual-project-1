from application import app, db
from application.models import Ideas, Tags
from flask import Flask, render_template

@app.route('/')
def ideas_home():
    all_ideas = Ideas.query.all()
    return render_template('ideas.html', ideas=all_ideas)