from flask import request
from flask_restful import Resource


class DAGResource(Resource):

    def post(self):
        data = request.get_json()
        try:
            pet_model = pet_schema.load(data, instance=Pet(), partial=True)
        except ValidationError as e:
            return jsonify(e.messages)
        db.session.add(pet_model)
        db.session.commit()
        return pet_schema.dump(pet_model)