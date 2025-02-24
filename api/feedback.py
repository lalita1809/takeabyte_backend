from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

from model.feedback import Feedback  # used for REST API building

# Create Blueprint for API
feedback_api = Blueprint('feedback_api', __name__, url_prefix='/api')
api = Api(feedback_api)

class FeedbackAPI:
    @staticmethod
    def get_feedback(name):
        feedback = {
            "KungPao": {
                "dish_name": "KungPao",
                "thumbs_up": 10,
                "thumbs_down": 15,
            },
            "OrangeChicken": {
                "dish_name": "Orange Chicken",
                "thumbs_up": 15,
                "thumbs_down": 25,
            },
        }
        return feedback.get(name)

    class _KungPao(Resource): 
             def get(self):
                feedback = FeedbackAPI.get_feedback("KungPao")
                if feedback:
                        return jsonify(feedback) 
                return {"message": "Data not found"}, 404

    class _OrangeChicken(Resource): 
        def get(self):
            feedback = FeedbackAPI.get_feedback("OrangeChicken")
            if feedback:
                return jsonify(feedback) 
            return {"message": "Data not found"}, 404

    class _AddFeedback(Resource):
        def post(self):
            """
            Create new feedback.
            """
            body = request.get_json()

            name = body.get('name')
            stars = body.get('stars')
            written_feedback = body.get('written_feedback')

            if not name or len(name) < 2:
                return {'message': 'Name is missing or too short'}, 400
            if stars is None:
                return {'message': 'Stars is missing'}, 400
            if not written_feedback or len(written_feedback) < 2:
                return {'message': 'Written Feedback is missing or too short'}, 400

            feedback_obj = Feedback(
                name=name,
                stars=stars,
                written_feedback=written_feedback
            )

            feedback = feedback_obj.create()
            if not feedback:
                return {'message': f'Error processing feedback for {name}'}, 400

            return jsonify(feedback.read())

    class _ReadFeedback(Resource):
        def get(self, name):
            """
            Retrieve feedback by dish name.
            """
            feedback = Feedback.query.filter_by(name=name).first()
            if not feedback:
                return {'message': f'Feedback for {name} not found'}, 404
            return jsonify(feedback.read())

    class _ReadAllFeedback(Resource):
        def get(self):
            """
            Retrieve all feedback.
            """
            feedbacks = Feedback.query.all()
            feedback_data = [feedback.read() for feedback in feedbacks]
            return jsonify(feedback_data)

    class _UpdateFeedback(Resource):
        def put(self):
            """
            Update feedback.
            """
            body = request.get_json()
            name = body.get('name')
           # if not name:
                #return {'message': 'Dish name is required for updating'}, 400

            feedback = Feedback.query.filter_by(name=name).first()
            if not feedback:
                return {'message': f'Feedback for {name} not found'}, 404

            feedback.update(body)
            return jsonify(feedback.read())

    class _DeleteFeedback(Resource):
        def delete(self):
            """
            Delete feedback.
            """
            body = request.get_json()
            name = body.get('name')

            if not name:
                return {'message': 'Dish name is required'}, 400

            feedback = Feedback.query.filter_by(name=name).first()
            if not feedback:
                return {'message': f'Feedback for {name} not found'}, 404

            feedback.delete()
            return jsonify({'message': f'Feedback for {name} deleted'})

# Register API routes
api.add_resource(FeedbackAPI._KungPao, '/feedback/KungPao')
api.add_resource(FeedbackAPI._OrangeChicken, '/feedback/OrangeChicken')
api.add_resource(FeedbackAPI._AddFeedback, '/feedback/addFeedback')
api.add_resource(FeedbackAPI._ReadFeedback, '/feedback/get/<string:name>')
api.add_resource(FeedbackAPI._ReadAllFeedback, '/feedback/getAll')
api.add_resource(FeedbackAPI._UpdateFeedback, '/feedback/update')
api.add_resource(FeedbackAPI._DeleteFeedback, '/feedback/delete')

# Instantiate API class
feedback_api_instance = FeedbackAPI()
