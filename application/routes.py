from application import app, db
from application.models import Ideas, Tags
from application.forms import ideaForm
from flask import Flask, render_template, request

@app.route('/')
def ideas_home():
    all_ideas = Ideas.query.all()

    return render_template('ideas.html', ideas = all_ideas)

@app.route('/add/idea', methods=['GET', 'POST'])
def add_idea():
    form = ideaForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            tag_id = form.tag_id.data
            name = form.name.data
            new_idea = Idea(title=title, description=description, tag_id=tag_id, name=name)
            db.session.add(new_idea)
            db.session.commit()
            return f'Added {title} to ideas!'
        else:
            return render_template('idea_entry.html', form=form, title="", description="", tag_id="", name="")
    else:
        return render_template('idea_entry.html', form=form)
