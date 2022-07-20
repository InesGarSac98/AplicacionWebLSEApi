from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ClassroomGames(db.Model):
    __tablename__ = 'ClassroomGames'
    id = Column(Integer, primary_key=True)
    classroomId = Column(Integer, ForeignKey('Classroom.id'))
    gameId = Column(Integer, ForeignKey('Games.id'))
    Classroom = relationship('Classroom')
    Game = relationship('Games')

    def serialize(self):
        return {
            'id': self.id,
            'classroomId': self.classroomId,
            'gameId': self.gameId,
            'game': self.Game.serialize()
        }

