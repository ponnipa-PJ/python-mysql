from . import db
from collections import OrderedDict
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updatedAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    user = db.relationship('User', backref='posts')
    
    def to_dict(self):
        return OrderedDict({
            'id': self.id,
            'userId': self.userId,
            'title': self.title,
            'content': self.content,
            'createdAt': self.createdAt.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.createdAt, datetime) else self.createdAt,
            'updatedAt': self.updatedAt.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.updatedAt, datetime) else self.updatedAt,        
        })