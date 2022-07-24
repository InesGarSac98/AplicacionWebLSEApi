from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ClassroomWords(db.Model):
    __tablename__ = 'ClassroomWords'
    id = Column(Integer, primary_key=True)
    wordId = Column(Integer, ForeignKey('Words.id'), nullable=False)
    classroomId = Column(Integer, ForeignKey('Classroom.id'), nullable=False)
    Classroom = relationship('Classroom', back_populates='ClassroomWords')
    Word = relationship('Words')

    def serialize(self):
        return {
            'id': self.id,
            'wordId': self.wordId,
            'classroomId': self.classroomId,
            'word': self.Word.serialize()
        }

