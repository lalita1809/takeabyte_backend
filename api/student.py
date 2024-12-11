from flask import Blueprint, jsonify
from flask_restful import Api, Resource # used for REST API building


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
                "age": 16,
                "major": "Something medical related",
                "university": "University of California, Los Angeles ",
            },
            "Nathan": {
                "name": "Nathaan Tejidor",
                "age": 16,
                "major": "Engine",
                "university": "Idk",
            },
            "Bailey": {
                "name": "Bailey Leeder",
                "age": 16,
                "major": "Chem Maybe",
                "university": "Del Norte",
            },
            "Yuva": {
                "name": "Yuva Bala",
                "age": 15,
                "major": "Buisness",
                "university": "NYU",
            },
            "Joanna": {
                "name": "Joanna Hu",
                "age": 17,
                "major": "engineering",
                "university": "harvard",
            },
            "Lalita": {
                "name": "Lalita Narayanan",
                "age": 17,
                "major": "bioinformatics",
                "university": "UCLA",
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

    

    # building RESTapi endpoint
api.add_resource(StudentAPI._bailey, '/student/bailey')          
api.add_resource(StudentAPI._joanna, '/student/joanna')
api.add_resource(StudentAPI._lalita, '/student/lalita')
api.add_resource(StudentAPI._yuva, '/student/yuva')
api.add_resource(StudentAPI._nathan, '/student/nathan')
api.add_resource(StudentAPI._ahmad, '/student/ahmad')


# Instantiate the StudentAPI to register the endpoints
student_api_instance = StudentAPI()


    