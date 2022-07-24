from app import db
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class QuizzGameAnswer(db.Model):
    __tablename__ = 'QuizzGameAnswers'
    id = Column(Integer, primary_key=True)
    isCorrect = Column(Boolean)
    questionId = Column(Integer, ForeignKey('QuizzGameQuestions.id'), nullable=False)
    wordId = Column(Integer, ForeignKey('Words.id'), nullable=False)
    isImage = Column(Boolean)
    Word = relationship('Words')
    Question = relationship('QuizzGameQuestion', back_populates="Answers")

    def serialize(self):
        return {
            'id': self.id,
            'isCorrect': self.isCorrect,
            'questionId': self.questionId,
            'wordId': self.wordId,
            'isImage': self.isImage,
            'word': self.Word.serialize()
        }

