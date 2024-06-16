from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), unique=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Vehicle id={self.id} license_plate={self.license_plate} model={self.model} availability={self.availability}>'


