from app import db
from sqlalchemy import Column, Integer, ForeignKey


class MemoryGameClassroomConfiguration(db.Model):
    __tablename__ = 'MemoryGameClassroomConfiguration'
    id = Column(Integer, primary_key=True)
    classroomId = Column(Integer, ForeignKey('Classroom.id'))
    gameId = Column(Integer, ForeignKey('Games.id'))
    time = Column(Integer)

    def serialize(self):
        return {
            'id': self.id,
            'classroomId': self.classroomId,
            'gameId': self.gameId,
            'time': self.time
        }




