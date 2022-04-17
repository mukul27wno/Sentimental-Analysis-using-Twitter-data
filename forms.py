from flask_wtf import FlaskForm #wt forms
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

class AddTaskForm(FlaskForm):
    hashtag = StringField('Query - ', validators=[DataRequired()])
    noft = StringField('Number of Tweets - ', validators=[DataRequired()])
    lng = StringField('Language - ', validators=[DataRequired()])
    submit = SubmitField('Submit')