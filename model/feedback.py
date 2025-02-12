from sqlite3 import IntegrityError
from __init__ import app, db

class Feedback(db.Model): 
    __tablename__ = 'feedbacks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)
    recipe = db.Column(db.Text, nullable=False)
    thumbs_up = db.Column(db.Integer, default=0)
    thumbs_down = db.Column(db.Integer, default=0)
    written_feedback = db.Column(db.Text)

    def __init__(self, name, cuisine, recipe, thumbs_up=0, thumbs_down=0, written_feedback=None):
        self.name = name
        self.cuisine = cuisine
        self.recipe = recipe
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down
        self.written_feedback = written_feedback
        
    def delete(self):
        try:
            db.session.delete(self)  
            db.session.commit()  
            return self
        except Exception as e:  # Catch all database-related errors
            db.session.rollback()
            print(f"Error deleting feedback: {e}")
            return None
    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()  
            return self
        except Exception as e:  # Catch all database-related errors
            db.session.rollback()
            print(f"Error creating feedback: {e}")
            return None
    
    def read(self):
        return {
            "id": self.id,
            "name": self.name,
            "cuisine": self.cuisine,
            "recipe": self.recipe,
            "thumbs_up": self.thumbs_up,
            "thumbs_down": self.thumbs_down,
            "written_feedback": self.written_feedback,
        }

    def update(self, inputs):
        if not isinstance(inputs, dict):
            return self

        self.name = inputs.get("name", self.name)
        self.cuisine = inputs.get("cuisine", self.cuisine)
        self.recipe = inputs.get("recipe", self.recipe)
        self.thumbs_up = inputs.get("thumbs_up", self.thumbs_up)
        self.thumbs_down = inputs.get("thumbs_down", self.thumbs_down)
        self.written_feedback = inputs.get("written_feedback", self.written_feedback)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error updating feedback: {e}")
            return None
        return self

    @classmethod
    def restore(cls, data):
        for feedback_data in data:
            feedback_id = feedback_data.pop('id', None)
            feedback = cls.query.filter_by(name=feedback_data.get("name")).first()

            if feedback:
                feedback.update(feedback_data)
            else:
                new_feedback = cls(**feedback_data)
                new_feedback.create()

        return "Restore complete"

def initFeedback():
    with app.app_context():
        feedbacks = [
            Feedback(
                name="Alice",
                cuisine="Italian",
                recipe="Spaghetti Carbonara",
                thumbs_up=5,
                thumbs_down=1,
                written_feedback="Delicious and easy to make!"
            ),
            Feedback(
                name="Bob",
                cuisine="Asian",
                recipe="Sushi Rolls",
                thumbs_up=10,
                thumbs_down=0,
                written_feedback="Perfect for family gatherings!"
            ),
        ]
        for feedback in feedbacks:
            feedback.create()  # This will correctly add the feedback to the database

