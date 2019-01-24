# coding=UTF-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Cria os campos no HTML para inserir/mostrar dados
class FormularioDeCadastro(FlaskForm):

    placa = StringField('Placa', validators=[DataRequired()], render_kw={"placeholder": "ABC-1234"})
    data = StringField('Data', id="datacadastro", render_kw={"readonly": "datacadastro"})
    hora = StringField('Hora', id="horacadastro", render_kw={"readonly": "horacadastro"})
    add = SubmitField('Adicionar')