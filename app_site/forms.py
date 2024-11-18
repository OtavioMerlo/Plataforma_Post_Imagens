from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app_site.models import Usuario

class FormLogin(FlaskForm):
    email=StringField("E-mail", validators=[DataRequired(),Email()])
    senha=PasswordField("Password", validators=[DataRequired()])
    btn_confirm=SubmitField("Entrar")

class FormCriarConta(FlaskForm):
    email=StringField("E-mail", validators=[DataRequired(),Email()])
    nome=StringField("Username", validators=[DataRequired()])
    senha=PasswordField("Password", validators=[DataRequired(),Length(6,20)])
    c_senha=PasswordField("Confirm Password", validators=[DataRequired(),EqualTo("senha")])
    btn_confirmCC=SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario=Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")


class FormFoto(FlaskForm):
    foto=FileField("Picture", validators=[DataRequired()])
    btn_confirm=SubmitField("Send")