from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Database ORMs
class ClassroomGames(db.Model):
    __tablename__ = 'ClassroomGames'
    id = Column(Integer, primary_key=True)
    classroomId = Column(Integer, ForeignKey('Classroom.id'))
    gameId = Column(Integer, ForeignKey('Games.id'))
    Classroom = relationship('Classroom')
    Games = relationship('Games')

    def serialize(self):
        return {
            'id': self.id,
            'classroomId': self.classroomId,
            'gameId': self.gameId
        }

