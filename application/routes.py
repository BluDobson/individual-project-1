from application import app, db
from application.models import Ideas, Tags
from application.forms import ideaForm, updateideaForm
from flask import Flask, render_template, request, redirect, url_for

def get_num(string):
    ls = ""
    for char in string:
        if char.isdigit():
            ls += char
    return int(ls)

@app.route('/')
def ideas_home():
    all_ideas = Ideas.query.all()
    all_tags = Tags.query.all()
    return render_template('ideas.html', ideas = all_ideas, tags = all_tags)

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
            return redirect(url_for('ideas_home'))

        else:
            return render_template('idea_entry.html', form=form, title="", description="", tag_id="", name="")
    else:
        return render_template('idea_entry.html', form=form)

@app.route('/update/idea', methods=['GET', 'POST'])
def update_idea():
    form = updateideaForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            idea_id = str(form.id.data)
            idea_id = get_num(idea_id)
            idea = Ideas.query.get(idea_id)
            if form.title.data != "":
                idea.title = form.title.data
            else:
                pass
            if form.description.data != "":
                idea.description = form.description.data
            else:
                pass
            tag_id = str(form.tag_id.data)
            tag_id = get_num(tag_id)
            idea.tag_id = tag_id
            if form.name.data != "":
                idea.name = form.name.data
            else:
                pass
            db.session.commit()
            return redirect(url_for('ideas_home'))
        else:
            return render_template('idea_update.html', form=form, id="", title="", description="", tag_id="", name="")
    else:
        return render_template('idea_update.html', form=form)

@app.route('/delete/idea', methods=['GET', 'POST'])
def delete_idea():
    form = deleteideaForm()
    if request.method == 'POST':
        idea_id = str(form.id.data)
        idea_id = get_num(idea_id)
        idea = Ideas.query.get(idea_id)
        db.session.delete(idea)
        db.session.commit()
        return redirect(url_for('ideas_home'))
    else:
        return render_template('idea_delete.html', form=form)
