from flask_restful import Resource, reqparse,request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user import UserModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class UserRegister(Resource):
    
    TABLE_NAME = 'users'
    
    parser = reqparse.RequestParser()
    
    parser.add_argument('username', 
                        type=str, 
                        required=True, 
                        help="This field cannot be left blank")
    
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('first_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('age',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('role',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    
    def post(self):
        
        data = UserRegister.parser.parse_args()
        hashed_pw = bcrypt.generate_password_hash(request.json["password"]).decode("utf-8")
    
        if UserModel.find_by_username(data['username']) or  UserModel.find_by_username(data['email']):
            return {'message': 'User with that username/email already exists'}, 400
        data['password'] = hashed_pw
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User created successfully'}, 201
    
 
    
class User(Resource):
    
    @classmethod
    def get(cls, user_id:int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json(), 200
    @classmethod    
    def delete(cls,user_id:int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user.delete_from_db()


# when logging it asks all the fields to be filled! so not working properly

    
class UserLogin(Resource):
    
    def post(self):
        data =UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        
        
        # if user and safe_str_cmp(user.password, data['password']) and bcrypt.check_password_hash(user.password, request.json["password"]):
        #     access_token = create_access_token(identity=user.id, fresh=True)
        #     refresh_token = create_refresh_token(user.id)
        #     return {
        #             'access_token': access_token,
        #             'refresh_token': refresh_token
        #         }, 200
        # return {'message': 'Invalid Credentials!'}, 401
        if user and  bcrypt.check_password_hash(user.password, request.json["password"]):
            return {'message':'logged in'}
            
            
        return {'message': 'Invalid Credentials!'}, 401
            