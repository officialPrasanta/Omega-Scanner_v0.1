from flask_wtf import FlaskForm
from wtforms import SelectField
from core.etc.parse_json import RenderJson

command = RenderJson()
choices = command['title']

class Form(FlaskForm):
    dorksList = SelectField('Dorks', choices=choices)
