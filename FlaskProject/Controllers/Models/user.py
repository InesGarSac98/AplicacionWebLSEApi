from app import db
from sqlalchemy import String, Column, Integer


# Database ORMs
class User(db.Model):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(100))
    email = Column(String(70), unique=True)
    role = Column(String(15))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'role': self.role,
        }
