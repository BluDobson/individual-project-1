from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError
from application import db
from application.models import Tags, Ideas

def get_tags():
    return Tags.query

def get_idea():
    return Ideas.query

class ideaForm(FlaskForm):
    title = StringField('Enter the title for your idea:', validators=[DataRequired(message="The title field can't be empty"), Length(max=30, message="That title is too long")])
    description = StringField('Enter a description for your idea:', validators=[Length(max=200, message="That description is too long")])
    tag_id = QuerySelectField('Choose a tag that suits your idea:', query_factory=get_tags, get_label='name', validators=[DataRequired(message="A tag is required")])
    name = StringField('Enter your name:', validators=[DataRequired(), Length(max=20, message="That name is too long")])
    submit = SubmitField('Add idea!')

class updateideaForm(FlaskForm):
    id = QuerySelectField('Choose the idea you want to update:', query_factory=get_idea, get_label='title', validators=[DataRequired("An ID is required")])
    title = StringField('Update the title:', validators=[Length(max=30, message="That title is too long")])
    description = StringField('Update the description:', validators=[Length(max=200, message="That description is too long")])
    tag_id = QuerySelectField('Update the tag:', query_factory=get_tags, get_label='name')
    name = StringField('Update the name:', validators=[Length(max=20, message="That name is too long")])
    submit = SubmitField('Update idea!')

class deleteideaForm(FlaskForm):
    id = QuerySelectField('Choose the idea you want to delete:', query_factory=get_idea, get_label='title', validators=[DataRequired(message="An ID is required")])
    submit = SubmitField('Delete idea!')

