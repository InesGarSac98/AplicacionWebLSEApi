from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Database ORMs
class studentAvailableGame(db.Model):
    __tablename__ = 'StudentAvailableGame'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('User.id'))
    studentId = Column(Integer, ForeignKey('Student.id'))
    teacherId = Column(Integer, ForeignKey('Teacher.id'))

    User = relationship('User')
    Student = relationship('Student')
    Teacher = relationship('Teacher')

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'studentId': self.studentId,
            'teacherId': self.teacherId
        }
