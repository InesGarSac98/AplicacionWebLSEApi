from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ClassroomGames(db.Model):
    __tablename__ = 'ClassroomGames'
    id = Column(Integer, primary_key=True)
    classroomId = Column(Integer, ForeignKey('Classroom.id'), nullable=False)
    gameId = Column(Integer, ForeignKey('Games.id'), nullable=False)
    Classroom = relationship('Classroom')
    Game = relationship('Games')

    def serialize(self):
        return {
            'id': self.id,
            'classroomId': self.classroomId,
            'gameId': self.gameId,
            'game': self.Game.serialize()
        }

