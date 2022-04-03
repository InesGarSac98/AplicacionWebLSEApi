from app import db
from sqlalchemy import String, Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class QuizzGameAnswer(db.Model):
    __tablename__ = 'QuizzGameAnswers'
    id = Column(Integer, primary_key=True)
    isCorrect = Column(Boolean)
    questionId = Column(Integer, ForeignKey('QuizzGameQuestions.id'))
    wordId = Column(Integer, ForeignKey('Words.id'))
    isImage = Column(Boolean)
    Word = relationship('Words')

    def serialize(self):
        return {
            'id': self.id,
            'isCorrect': self.isCorrect,
            'questionId': self.questionId,
            'wordId': self.wordId,
            'isImage': self.isImage,
            'word': self.Word.serialize()
        }


