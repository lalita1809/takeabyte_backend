from __init__ import db, app
from sqlalchemy.exc import IntegrityError

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    time = db.Column(db.Integer, nullable=True)

    def __init__(self, title, ingredients, instructions, time=None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.time = time

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.rollback()
            return None

    def read(self):
        return {
            "id": self.id,
            "title": self.title,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "time": self.time
        }

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        try:
            db.session.commit()
            return self
        except IntegrityError:
            db.session.rollback()
            return None

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return None

def initRecipe():
    with app.app_context():
        db.create_all()