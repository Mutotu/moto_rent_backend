from db import db
from datetime import datetime
from models.motorcycle import MotorcycleModel

class RentModel(db.Model):
    
    __tablename__ = 'rent'
    
    id = db.Column( db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    moto_id = db.Column(db.Integer, db.ForeignKey('motorcycles.id'))
    start_date = db.Column( db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    total_price = db.Column(db.Float)
    confirmed = db.Column(db.Boolean)
    date = db.Column(db.DateTime, default=datetime.utcnow)
   
    def __init__(self, user_id, moto_id, start_date, end_date):
        self.user_id = user_id
        self.moto_id = moto_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = 0
        self.confirmed = False
        self.date = datetime.now()
        
    def json(self):
        return {
            "rent_info":{
            'id':self.id,
            'user_id':self.user_id,
            'moto_id':self.moto_id,
            'start_date':self.start_date,
            'end_date':self.end_date,
            'total_price':self.total_price,
            'confirmed':self.confirmed,
             'date':self.date.isoformat()
            
            }
           
        }
        
        
    def save_to_db(self):
        self.confirmed = True
        # self.total_price = 0
        db.session.add(self)      
        db.session.commit()
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
        
    def charge_total(self, moto_id):
        moto_qs = MotorcycleModel.query.find_by_id(id=moto_id)
        days = int(self.end_date) - int(self.start_date)
        # if moto_qs:
        moto = moto_qs.first()

        return moto.price * days
        # return 0  