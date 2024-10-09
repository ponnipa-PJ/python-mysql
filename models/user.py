from . import db
from datetime import datetime
from collections import OrderedDict

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthDate = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return OrderedDict({
            'id': self.id,
            'name': self.name,
            'birthDate': self.birthDate.strftime('%Y-%m-%d'),
            'age': self.calculateAge()
        })
        
    def calculateAge(self):
        today = datetime.today()
        age = today.year - self.birthDate.year 
        
        if (today.month, today.day) < (self.birthDate.month, self.birthDate.day):
            age -=1
        return age
            