import flask
from flask import Blueprint, render_template
from flask_login import login_required
from wtforms import Form, PasswordField, StringField, validators
from wtforms.widgets import TextArea

cadastrar_paciente = Blueprint('cadastrar_paciente', __name__)


class CadastroForm(Form):
    message = "É obrigatório o preenchimento do usuário"
    nome_completo = StringField('Nome Completo', validators=[validators.DataRequired(
        message=message)])
    data_nascimento = StringField('Data de nascimento', validators=[validators.DataRequired(
        message=message)])
    sexo = StringField('Sexo', validators=[validators.DataRequired(
        message=message)])
    endereco = StringField('Endereço', validators=[validators.DataRequired(
        message=message)])
    cidade = StringField('Cidade', validators=[validators.DataRequired(
        message=message)])
    estado = StringField('Estado', validators=[validators.DataRequired(
        message=message)])
    cep = StringField('CEP', validators=[validators.DataRequired(
        message=message)])
    cns = StringField('CNS', validators=[validators.DataRequired(
        message=message)])
    alergias = StringField('Alergias', validators=[validators.DataRequired(
        message=message)])
    comorbidades = StringField('Comorbidades', validators=[validators.DataRequired(
        message=message)])
    historia_clinica = StringField('História Clínica', widget=TextArea(), validators=[validators.DataRequired(
        message=message)])
    

@cadastrar_paciente.route('/cadastrar-paciente')
def cadastro_paciente():
    form = CadastroForm(flask.request.form)
    return render_template('cadastrar-paciente.html', form=form)