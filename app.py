from flask import Flask, session
from flask import request, jsonify, json
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from db import db


from resources.user import UserRegister, UserLogin, User
from resources.motorcycle import Motorcycle, MotoList, MotoModify
from resources.comment import Comment
from resources.rent import Rent,RentedMotos
# from resources.image import ImageUpload
# from image_helper import IMAGE_SET



app = Flask(__name__)

CORS(app)

import os
from dotenv import load_dotenv
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

api = Api(app)
db.init_app(app)

@app.route('/')
def home():
    return 'Hello ulen'


api.add_resource(UserRegister, '/register')
api.add_resource(Motorcycle, '/post')
api.add_resource(MotoModify, '/moto/<int:id>')
api.add_resource(MotoList, '/motos')
api.add_resource(Comment, '/comment/<int:moto_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(RentedMotos, '/rent/<int:rent_id>')
api.add_resource(Rent, '/rent/<int:moto_id>')


if __name__ == '__main__':
    port = os.environ.get('PORT') or 5000
    app.run('0.0.0.0', port=port, debug=True)