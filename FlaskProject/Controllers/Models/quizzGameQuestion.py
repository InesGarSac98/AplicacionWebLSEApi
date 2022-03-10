from app import db
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship


class QuizzGameQuestion(db.Model):
    __tablename__ = 'QuizzGameQuestions'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    wordId = Column(Integer, ForeignKey('Words.id'))
    gameId = Column(Integer, ForeignKey('Games.id'))
    showImage = Column(Boolean)
    Answers = relationship('QuizzGameAnswer')
    Word = relationship('Words')

    def serialize(self):
        serializedAnswers = []
        for answer in self.Answers:
            serializedAnswers.append(answer.serialize())
        return {
            'id': self.id,
            'name': self.name,
            'wordId': self.wordId,
            'gameId': self.gameId,
            'showImage': self.showImage,
            'answers': serializedAnswers,
            'word': self.Word.serialize()

        }


