from flask_wtf import FlaskForm #wt forms
from wtforms import StringField, SubmitField, SelectField, DecimalField, IntegerField
from wtforms.validators import DataRequired 

class AddTaskForm(FlaskForm):
    hashtag = StringField('Query - ', validators=[DataRequired()])
    noft = IntegerField('Number of Tweets - ')
    lng = SelectField('Language - ', choices=[('en'), ('hi'),('ur'),('ru'),('de')], validators=[DataRequired()])
    # noft = StringField('Number of Tweets - ', validators=[DataRequired()])
    # lng = StringField('Language - ', validators=[DataRequired()])
    submit = SubmitField('Submit')