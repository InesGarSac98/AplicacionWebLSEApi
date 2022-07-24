from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class QuizzGameClassroomConfiguration(db.Model):
    __tablename__ = 'QuizzGameClassroomConfiguration'
    id = Column(Integer, primary_key=True)
    classroomId = Column(Integer, ForeignKey('Classroom.id'), nullable=False)
    gameId = Column(Integer, ForeignKey('Games.id'), nullable=False)
    time = Column(Integer, nullable=False)
    numberOfQuestions = Column(Integer, nullable=False)
    Questions = relationship('QuizzGameQuestion')

    def serialize(self):
        serializedQuestions = []
        for question in self.Questions:
            serializedQuestions.append(question.serialize())
        return {
            'id': self.id,
            'classroomId': self.classroomId,
            'gameId': self.gameId,
            'time': self.time,
            'numberOfQuestions': self.numberOfQuestions,
            'questions': serializedQuestions
        }



