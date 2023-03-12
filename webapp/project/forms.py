from datetime import date

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired


class NewProjectForm(FlaskForm):
    name = StringField("Название проекта", validators=[DataRequired()], render_kw={"class": "form-control"})
    description = TextAreaField("Краткое описание проекта", render_kw={"class": "form-control"})
    date_end = DateField("Дата окончания проекта", render_kw={"class": "form-control", "min": date.today().strftime("%Y-%m-%d")})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})
