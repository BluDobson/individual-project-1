from application import app, db
from application.models import Ideas, Tags
from application.forms import ideaForm
from flask import Flask, render_template, request

def get_num(string):
    ls = ""
    for char in string:
        if char.isdigit():
            ls += char
    return int(ls)

@app.route('/')
def ideas_home():
    all_ideas = Ideas.query.all()
    tags = Tags.query.all()
    return render_template('ideas.html', ideas = all_ideas)

@app.route('/add/idea', methods=['GET', 'POST'])
def add_idea():
    form = ideaForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            tag_id = str(form.tag_id.data)
            tag_id = get_num(tag_id)
            name = form.name.data
            new_idea = Ideas(title=title, description=description, tag_id=tag_id, name=name)
            db.session.add(new_idea)
            db.session.commit()
            return f'Added {title} to ideas!'
        else:
            return render_template('idea_entry.html', form=form, title="", description="", tag_id="", name="")
    else:
        return render_template('idea_entry.html', form=form)
