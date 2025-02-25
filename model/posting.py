from sqlite3 import IntegrityError
from __init__ import app, db


class Posting(db.Model):
    __tablename__ = 'postings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    dish = db.Column(db.String(100))
    cuisine = db.Column(db.String(50))
    link = db.Column(db.String(255))
    comments = db.Column(db.Text)


    def __init__(self, name, dish, cuisine, link, comments):
        self.name = name
        self.dish = dish
        self.cuisine = cuisine
        self.link = link
        self.comments = comments


    def create(self):
        try:
            db.session.add(self)  # Prepare to persist posting object to the postings table
            db.session.commit()  # Commit the changes to the database
            return self
        except IntegrityError:
            db.session.rollback()
            return None




    def read(self):
            """
            Converts the user object to a dictionary.
           
            Returns:
                dict: A dictionary representation of the user object.
            """
            data = {
                "name": self.name,
                "dish": self.dish,
                "cuisine": self.cuisine,
                "link": self.link,
                "comments": self.comments,
            }
            return data



    def update(self, inputs):
            """
            Updates the student object with new data.
           
            Args:
                inputs (dict): A dictionary containing the new data for the student.
           
            Returns:
                Student: The updated user object, or None on error.
            """
            if not isinstance(inputs, dict):
                return self


            name = inputs.get("name", "")
            dish = inputs.get("dish", "")
            cuisine = inputs.get("cuisine", "")
            link = inputs.get("link", "")
            comments = inputs.get("comments", "")


            # Update table with new data
            if name:
                self.name = name
            if dish:
                self.dish = dish
            if link:
                self.link = link
            if cuisine:
                self.cuisine = cuisine
            if comments:
                self.comments = comments
               
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                return None
            return self
    def delete(self):
        """
        Removes the user object from the database and commits the transaction.
       
        Returns:
            None
        """
            # try:
            # # posting_to_delete = Posting.query.filter_by(name=self.name).first()
            # # if posting_to_delete:
            #     db.session.delete(posting_to_delete)
            #     db.session.commit()
            # # else:
            # #     return None
            # # except IntegrityError:
            # # db.session.rollback()
            # # return None
        try:
            db.session.delete(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return None  




    def restore(data):
            posting = {}
            for posting_data in data:
                _ = posting_data.pop('id', None)  # Remove 'id' from user_data and store it in user_id
                _name = posting_data.get("name", None)
                posting = Posting.query.filter_by(name=_name).first()
                print(type(posting))
                if posting:
                    posting.update(posting_data)
                else:
                    posting = Posting(**posting_data)
                    posting.create()
            return posting
    def add(self):
        # Add the instance to the database
        db.session.add(self)
        db.session.commit()
        return self




def initPostings():
    with app.app_context():
        db.create_all()
        p1 = Posting(
            name='Martha',
            dish='Cornbread',
            cuisine='American',
            link='https://www.marthastewart.com/859136/classic-cornbread',
            comments='Tastes amazing, very quick and easy to make too. Highly recommend for those who want to make cornbread.'
        )
        p2 = Posting(
            name='Wayne',
            dish='Stir Fry Tofu',
            cuisine='Chinese',
            link='https://rainbowplantlife.com/tofu-stir-fry/',
            comments='Very savory flavors and pretty simple ingredients everybody has at home. Would recommend.'
        )
        postings = [p1, p2]
        for posting in postings:
            try:
                posting.create()
            except IntegrityError:
                '''Fails with bad or duplicate data'''
                db.session.rollback()
