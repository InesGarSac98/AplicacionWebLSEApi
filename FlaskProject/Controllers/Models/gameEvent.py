from app import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, Float


class GameEvent(db.Model):
    __tablename__ = 'GameEvents'
    id = Column(Integer, primary_key=True)
    gameId = Column(Integer, ForeignKey('Games.id'), nullable=False)
    studentId = Column(Integer, ForeignKey('Student.id'), nullable=False)
    status = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    leftTime = Column(Float, nullable=False)
    gamePlayId = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)
    events = Column(Text, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'gameId': self.gameId,
            'studentId': self.studentId,
            'status': self.status,
            'date': self.date,
            'leftTime': self.leftTime,
            'gamePlayId': self.gamePlayId,
            'score': self.score,
            'events': self.events
        }
