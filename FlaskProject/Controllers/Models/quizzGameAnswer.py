from app import db
from sqlalchemy import String, Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class QuizzGameAnswer(db.Model):
    __tablename__ = 'QuizzGameAnswers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    correct = Column(Boolean)
    questionId = Column(Integer, ForeignKey('QuizzGameQuestions.id'))
    showImage = Column(Boolean)
    wordId = Column(Integer, ForeignKey('Words.id'))
    Word = relationship('Words')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'correct': self.correct,
            'questionId': self.questionId,
            'showImage': self.showImage,
            'wordId': self.wordId,
            'word': self.Word.serialize()
        }


