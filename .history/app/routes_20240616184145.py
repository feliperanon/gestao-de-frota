from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Vehicle

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)

@bp.route('/add', methods=['POST'])
def add_vehicle():
    license_plate = request.form.get('license_plate')
    model = request.form.get('model')
    if license_plate and model:
        new_vehicle = Vehicle(license_plate=license_plate, model=model)
        db.session.add(new_vehicle)
        db.session.commit()
    return redirect(url_for('main.index'))
