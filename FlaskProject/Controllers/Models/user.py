from app import db
from sqlalchemy import String, Column, Integer


class User(db.Model):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(70), unique=True, nullable=False)
    role = Column(String(15), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
        }
