from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Vehicle
from app.forms import VehicleForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    vehicles = Vehicle.query.all()
    form = VehicleForm()
    return render_template('index.html', vehicles=vehicles, form=form)

@bp.route('/add', methods=['POST'])
def add_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        license_plate = form.license_plate.data
        model = form.model.data
        new_vehicle = Vehicle(license_plate=license_plate, model=model)
        db.session.add(new_vehicle)
        db.session.commit()
        flash('Veículo adicionado com sucesso!', 'success')
    else:
        flash('Erro ao adicionar veículo. Verifique os dados e tente novamente.', 'danger')
    return redirect(url_for('main.index'))

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_vehicle(id):
    vehicle = Vehicle.query.get(id)
    form = VehicleForm(obj=vehicle)
    if form.validate_on_submit():
        vehicle.license_plate = form.license_plate.data
        vehicle.model = form.model.data
        db.session.commit()
        flash('Veículo atualizado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit.html', form=form, vehicle=vehicle)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    flash('Veículo excluído com sucesso!', 'success')
    return redirect(url_for('main.index'))
