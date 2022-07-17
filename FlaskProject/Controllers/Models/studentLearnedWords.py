from app import db
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


# Database ORMs
class StudentLearnedWords(db.Model):
    __tablename__ = 'StudentLearnedWords'
    id = Column(Integer, primary_key=True)
    wordId = Column(Integer, ForeignKey('Words.id'))
    gameId = Column(Integer, ForeignKey('Games.id'))
    studentId = Column(Integer, ForeignKey('Student.id'))
    date = Column(DateTime, nullable=False)
    Word = relationship('Words')

    def serialize(self):
        return {
            'id': self.id,
            'wordId': self.wordId,
            'gameId': self.gameId,
            'studentId': self.studentId,
            'word': self.Word.serialize()
        }

