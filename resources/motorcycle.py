from flask_restful import Resource, reqparse
from models.motorcycle import MotorcycleModel
from flask_jwt_extended import jwt_required
#to get the headers
from flask import request

class Motorcycle(Resource):
    
    
    
    parser = reqparse.RequestParser()
    
    parser.add_argument('make', 
                        type=str, 
                        required=True, 
                        help="This field cannot be left blank")
    
    parser.add_argument('model',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('year',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('price',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('photo',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = Motorcycle.parser.parse_args()
        user_id = request.headers.get('user_id')
        data['user_id'] = user_id
        motorcycle = MotorcycleModel(**data)

        try:
            motorcycle.save_to_db()
        except: 
              return {'message': 'An error occured while creating the post'}, 500
        return motorcycle.json(), 201
        
    
class MotoModify(Resource):
    
    # @jwt_required  # No longer needs brackets
    def get(self, id):
        motorcycle = MotorcycleModel.find_by_id(id)
        if motorcycle:
            return motorcycle.json()
        return {'message': "Motorcycle not found"}

        
    def delete(self, id):
        motorcycle = MotorcycleModel.find_by_id(id)
        if motorcycle:
            motorcycle.delete_from_db()
        return {"message": "Item deleted"}
 
 
 #put method isnt working
    @classmethod
    def put(self, id):
        data = request.get_json()
        # print(data)
        motorcycle = MotorcycleModel.find_by_id(id)      
        
        if not motorcycle:
            return 'not found'
        # if data["make"]:
        #     motorcycle.make = data["make"]
        for k,v  in data.iteritems():
            setattr(motorcycle, k, v)
        # motorcycle.model = data["model"]
        # motorcycle.year = data['year']
        # motorcycle.price = data["price"]
        # motorcycle.description = data["description"]
        # motorcycle.photo = data["photo"]
        # motorcycle = data
        motorcycle.save_to_db()

        return "moto updated"
            
    
    
    
class MotoList(Resource):
    def get(self):
        return {'motos': [moto.json() for moto in MotorcycleModel.query.all()]}