from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField, BooleanField

class LoginForm(FlaskForm):
    namaUser = StringField('Nama User : ')
    password = PasswordField('Password : ')
    jenisKelamin = RadioField('Jenis Kelamin : ', choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
    agama = SelectField('Pilih Agama : ', choices=[(1, 'Islam'), (2, 'Kristen'), (3, 'Hindu'), (4, 'Budha'), (5, 'Katolik')])
    hobi1 = BooleanField('Olahraga')
    hobi2 = BooleanField('Berenang')
    hobi3 = BooleanField('Membaca')
    submit = SubmitField('Kirim')
    