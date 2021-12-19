from wtforms import (
    StringField,
    validators,
    TextAreaField,
)
from flask_wtf import FlaskForm


class AskForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=10, max=50)])
    body = TextAreaField('Body', [validators.Length(min=10, max=1000)])


class AnswerForm(FlaskForm):
    body = TextAreaField('Body', [validators.Length(min=10, max=1000)])
