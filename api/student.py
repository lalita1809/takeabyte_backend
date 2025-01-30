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
            """
            Update a student.
            """
            body = request.get_json()

            # Get student name from the request body
            name = body.get('name')
            if not name:
                return {'message': 'Student name is required for updating.'}, 400

            # Find the student in the database
            student = Student.query.filter_by(name=name).first()
            if student is None:
                return {'message': f'Student {name} not found'}, 404

            # Update the student object with the new data
            student.update(body)

            return jsonify(student.read())
    class _Delete(Resource):
        def delete(self):
            """
            Delete a student.
            """
            body = request.get_json()

            # Check if 'name' is provided in the request
            if not body or 'name' not in body:
                return {'message': 'Missing student name'}, 400  # Bad request

            # Extract student details from the request body
            name = body['name']
            age = body.get('age')
            grade = body.get('grade')
            favorite_color = body.get('favorite_color')

            # Check if the student exists in the database
            student = Student.query.filter_by(name=name).first()

            if student is None:
                return {'message': f'Student {name} not found'}, 404  # Not found

            # Compare current student data with the data in the request body
            if age is not None and student.age != age:
                return {'message': f'Age mismatch. Student age is {student.age}, but received {age}.'}, 400
            if grade is not None and student.grade != grade:
                return {'message': f'Grade mismatch. Student grade is {student.grade}, but received {grade}.'}, 400
            if favorite_color is not None and student.favorite_color != favorite_color:
                return {'message': f'Favorite color mismatch. Student color is {student.favorite_color}, but received {favorite_color}.'}, 400

            # Assuming student.read() returns a dictionary of their data
            try:
                json = student.read()
                if not isinstance(json, dict):
                    raise ValueError("Student data is not serializable")
            except Exception as e:
                return {'message': str(e)}, 500  # Server error

            # Proceed to delete the student
            student.delete()

            return jsonify({'message': f'Student {name} deleted', 'data': json}), 200  # OK response




    

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
api.add_resource(StudentAPI._Delete, '/student/delete')





# Instantiate the StudentAPI to register the endpoints
student_api_instance = StudentAPI()


    
