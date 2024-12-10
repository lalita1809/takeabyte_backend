
from flask import Blueprint
from flask_restful import Api, Resource # used for REST API building


student_api = Blueprint('student_api', __name__,
                   url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(student_api)

class StudentAPI:
    @staticmethod
    def get_student(name):
        students = {
            "John": {
                "name": "John",
                "age": 65,
                "major": "Computer Science",
                "university": "University of Oregon"
            },
            "Bailey": {
                "name": "Bailey Leeder",
                "age": 16,
                "major": "Chem Maybe",
                "university": "ABC University"
            },
            "Yuva": {
                "name": "Yuva Bala",
                "age": 15,
                "major": "Buisness",
                "university": "NYU"
            }
            }
        return students.get(name)


class StudentAPI:        
    class _lalita(Resource): 
        def get(self):
            return {"message": "Lalita's data is not yet implemented"}, 200
    
    class _yuva(Resource): 
        def get(self):
            return {"message": "Yuva's data is not yet implemented"}, 200
    
    class _bailey(Resource): 
        def get(self):
            student = StudentAPI.get_student("Bailey")
            return student, 200
    
    class _joanna(Resource): 
        def get(self):
            return {"message": "Joanna's data is not yet implemented"}, 200
    
    class _ahmad(Resource): 
        def get(self):
            return {"message": "Ahmad's data is not yet implemented"}, 200
    
    class _nathan(Resource): 
        def get(self):
            return {"message": "Nathan's data is not yet implemented"}, 200

    

    # building RESTapi endpoint
api.add_resource(StudentAPI._bailey, '/student/bailey')          
api.add_resource(StudentAPI._joanna, '/student/joanna')
api.add_resource(StudentAPI._lalita, '/student/lalita')
api.add_resource(StudentAPI._yuva, '/student/yuva')
api.add_resource(StudentAPI._nathan, '/student/nathan')
api.add_resource(StudentAPI._ahmad, '/student/ahmad')


# Instantiate the StudentAPI to register the endpoints
student_api_instance = StudentAPI()


    