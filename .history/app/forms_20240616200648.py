from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class VehicleForm(FlaskForm):
    license_plate = StringField('Placa', validators=[DataRequired(), Length(min=1, max=10)])
    model = StringField('Modelo', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Adicionar Veículo')



