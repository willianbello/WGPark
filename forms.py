# coding=UTF-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

# Função para pegar data e hora atual, converter para o formato normal e mandar para o index
data = datetime.now()
datatxt = data.strftime("%d/%m/%Y")
horatxt = data.strftime("%H:%M:%S")


# Cria os campos no HTML para inserir/mostrar dados
class FormularioDeCadastro(FlaskForm):

    placa = StringField('Placa', validators=[DataRequired()], render_kw={
                        "placeholder": "ABC-1234"})
    data = StringField('Data', id="datacadastro", render_kw={
                       "readonly": "datacadastro"})
    hora = StringField('Hora', id="horacadastro", render_kw={
                       "readonly": "horacadastro"})
    add = SubmitField('Adicionar', render_kw={"class": "btn btn-success"})


class FormulariodeExclusao(FlaskForm):

    pkcodentr = StringField('Cod placa')

    placacarsd = StringField(
        'Placa')

    dataentrsd = StringField('Data entrada')

    horaentrsd = StringField('Hora entrada')

    datasd = StringField('Data saída', render_kw={
        "readonly"" ""value": datatxt})

    horasd = StringField('Hora saída', render_kw={
        "readonly"" ""value": horatxt})

    remover = SubmitField('Remover veículo', render_kw={
        "class": "btn btn-success"})
