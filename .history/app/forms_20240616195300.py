from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class VehicleForm(FlaskForm):
    license_plate = StringField(
        'Placa', 
        validators=[
            DataRequired(message="Por favor, insira a placa do veículo."),
            Length(min=1, max=10, message="A placa deve ter entre 1 e 10 caracteres."),
            Regexp(r'^[A-Z]{3}\d{4}$', message="Formato de placa inválido. Use AAA9999.")  # Validador de formato
        ]
    )
    model = StringField(
        'Modelo', 
        validators=[
            DataRequired(message="Por favor, insira o modelo do veículo."),
            Length(min=1, max=50, message="O modelo deve ter entre 1 e 50 caracteres.")
        ]
    )
    submit = SubmitField('Adicionar Veículo')

