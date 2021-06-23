from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError
from application import db
from application.models import Tags

def get_tags():
    return Tags.query

class ideaForm(FlaskForm):
    title = StringField('Enter the title for your idea:', validators=[DataRequired(), Length(max=30)])
    description = StringField('Enter a description for your idea:', validators=[Length(max=200)])
    tag_id = QuerySelectField('Choose a tag that suits your idea:', query_factory=get_tags, get_label='name', validators=[DataRequired()])
    name = StringField('Enter your name:', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Add idea!')