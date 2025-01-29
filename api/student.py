from flask import Blueprint, request, jsonify, current_app, Response, g
from flask_restful import Api, Resource # used for REST API building
from model.student import Student


student_api = Blueprint('student_api', __name__,
                   url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(student_api)

class StudentAPI:
    @staticmethod
    def get_student(name): 
        students = {
            "Ahmad": {
                "name": "Ahmad",
                "age": 15,
                "grade": "Sophomore",
                "favorite_color": "Blue",
            },
            "Nathan": {
                "name": "Nathan Tejidor",
                "age": 16,
                "grade": "Sophomore",
                "favorite_color": "Red",
            },
            "Bailey": {
                "name": "Bailey Leeder",
                "age": 16,
                "grade": "Junior",
                "favorite_color": "Green",
            },
            "Yuva": {
                "name": "Yuva Bala",
                "age": 15,
                "grade": "Sophomore",
                "favorite_color": "Navy Blue",
            },
            "Joanna": {
                "name": "Joanna Hu",
                "age": 17,
                "grade": "Senior",
                "favorite_color": "Blue",
            },
            "Lalita": {
                "name": "Lalita Narayanan",
                "age": 17,
                "grade": "Senior",
                "favorite_color": "Purple",
            },
        }
        return students.get(name)

    class _lalita(Resource): 
        def get(self):
            student = StudentAPI.get_student("Lalita")
            if student:
                return jsonify(student) 
            return {"Data not found"}, 404
    class _yuva(Resource): 
        def get(self):
            student = StudentAPI.get_student("Yuva")
            if student:
                return jsonify(student) 
            return {"Data not found"}, 404
    class _bailey(Resource): 
        def get(self):
            student = StudentAPI.get_student("Bailey")
            if student:
                return jsonify(student) 
    class _joanna(Resource): 
        def get(self):
            student = StudentAPI.get_student("Joanna")
            if student:
                return jsonify(student) 
            return {"Data not found"}, 404
    class _ahmad(Resource): 
        def get(self):
            student = StudentAPI.get_student("Ahmad")
            if student:
                return jsonify(student) 
            return {"Data not found"}, 404 
    class _nathan(Resource): 
        def get(self):
            student = StudentAPI.get_student("Nathan")
            if student:
                return jsonify(student) 
            return {"Data not found"}, 404
    
    class _addStudent(Resource):
        def post(self):
            """
            Create a new Student.
            """
            body = request.get_json()

            # Validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': 'Name is missing, or is less than 2 characters'}, 400

            age = body.get('age')
            if age is None:
                return {'message': 'Age is missing'}, 400
            
            grade = body.get('grade')
            if grade is None:
                return {'message': 'Grade is missing'}, 400
            
            favorite_color = body.get('favorite_color')
            if favorite_color is None or len(favorite_color) < 2:
                return {'message': 'Favorite Color is missing, or is less than 2 characters'}, 400

            # Setup minimal Student OBJECT
            student_obj = Student(name=name, age=age, grade=grade, favorite_color=favorite_color)

            # Add user to database
            student = student_obj.create()  # pass the body elements to be saved in the database
            if not student:  # failure returns error message
                return {'message': f'Processed {name}'}, 400
            return jsonify(student.read())
    class _Read(Resource):
        def get(self, name):
            """
            Retrieve a single student by their name.
            """
            try:
                # Query the database for a student with the specified name
                student = Student.query.filter_by(name=name).first()

                # If no student is found, return a 404 error
                if not student:
                    return {'message': f'Student with name "{name}" not found'}, 404

                # Return the serialized student data
                return jsonify(student.read())
            except Exception as e:
                return {'message': f'Error retrieving student: {str(e)}'}, 500
    class _ReadGeneral(Resource):
        def get(self):
            """
            Retrieve a single student by their name.
            """
            try:
                # Query all students from the database
                students = Student.query.all()

                # Use the model's read method or create a list of serialized data
                student_data = [student.read() for student in students]

                # Return the serialized student data
                return jsonify(student_data)
            except Exception as e:
                return {'message': f'Error retrieving student: {str(e)}'}, 500
    class _Update(Resource):
        def put(self):
            data = request.get_json()  # Parse JSON from the request body
            if not data:
                return jsonify({"message": "Invalid input"}), 400

            name = data.get("name", "")
            student = Student.query.filter_by(name=name).first()  # Find the student by name
            if not student:
                return jsonify({"message": "Student not found"}), 404

            # Call the update method of the Student model
            updated_student = student.update(data)
            if updated_student:
                return jsonify({"name": updated_student.name}), 200
            else:
                return jsonify({"message": "Failed to update student"}), 500

    

    # building RESTapi endpoint
api.add_resource(StudentAPI._bailey, '/student/bailey')          
api.add_resource(StudentAPI._joanna, '/student/joanna')
api.add_resource(StudentAPI._lalita, '/student/lalita')
api.add_resource(StudentAPI._yuva, '/student/yuva')
api.add_resource(StudentAPI._nathan, '/student/nathan')
api.add_resource(StudentAPI._ahmad, '/student/ahmad')
api.add_resource(StudentAPI._addStudent, '/student/add')
api.add_resource(StudentAPI._Read, '/studentGet/<string:name>')
api.add_resource(StudentAPI._ReadGeneral, '/studentGet/')
api.add_resource(StudentAPI._Update, '/student/update')




# Instantiate the StudentAPI to register the endpoints
student_api_instance = StudentAPI()


    
