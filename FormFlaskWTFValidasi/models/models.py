from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, URL

class KomentarForm(FlaskForm):
    nama = StringField('Nama : ', [DataRequired(), Length(max=50)])
    email = StringField('Email : ', [DataRequired(), Email('Email harus benar.')])
    url = StringField('URL : ', [DataRequired(), URL()])
    komentar = TextAreaField('Komentar', [DataRequired()])
    submit = SubmitField('Kirim')