from app import db
from sqlalchemy import String, Column, Integer


class Games(db.Model):
    __tablename__ = 'Games'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    image = Column(String)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image
        }


