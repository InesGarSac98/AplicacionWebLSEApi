from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Classroom(db.Model):
    __tablename__ = 'Classroom'
    id = Column(Integer, primary_key=True)
    teacherId = Column(Integer, ForeignKey('Teacher.id'), nullable=False)
    name = Column(String(70), nullable=False)
    classroomCode = Column(String(70), unique=True, nullable=False)
    Teacher = relationship('Teacher')
    Students = relationship('Student', back_populates="Classroom")
    ClassroomWords = relationship('ClassroomWords', back_populates="Classroom", )
    ClassroomGames = relationship('ClassroomGames', back_populates="Classroom")

    def serialize(self):
        students = []
        for student in self.Students:
            students.append(student.serialize())
        return {
            'id': self.id,
            'teacherId': self.teacherId,
            'name': self.name,
            'classroomCode': self.classroomCode,
            'students': students
        }
