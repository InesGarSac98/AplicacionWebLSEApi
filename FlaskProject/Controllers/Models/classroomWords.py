from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Database ORMs
class ClassroomWords(db.Model):
    __tablename__ = 'ClassroomWords'
    id = Column(Integer, primary_key=True)
    wordId = Column(Integer, ForeignKey('Words.id'))
    classroomId = Column(Integer, ForeignKey('Classroom.id'))
    Classroom = relationship('Classroom', back_populates='ClassroomWords')
    Word = relationship('Words')

    def serialize(self):
        return {
            'id': self.id,
            'wordId': self.wordId,
            'classroomId': self.classroomId
        }

