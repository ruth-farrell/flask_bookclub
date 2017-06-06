from flask_wtf import Form
from wtforms import DateField, StringField, PasswordField, BooleanField, IntegerField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Optional

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class BookForm(Form):
    title = StringField('title', validators=[DataRequired()])
    due_date =  DateField('due_date', format='%d/%m/%Y',
            validators=[Optional()])
    info = StringField('info', widget=TextArea(), validators=[Optional()])
    notify = BooleanField('notify', default=False)

class ReviewForm(Form):
    star = IntegerField('star', validators=[DataRequired()])
    text = StringField('text', widget=TextArea(), validators=[Optional()])