from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Database ORMs
class Classroom(db.Model):
    __tablename__ = 'Classroom'
    id = Column(Integer, primary_key=True)
    teacherId = Column(Integer, ForeignKey('Teacher.id'), nullable=False)
    name = Column(String(70), nullable=False)
    classroomCode = Column(String(70), unique=True, nullable=False)
    Teacher = relationship('Teacher')
    Students = relationship('Student', back_populates="Classroom")
    ClassroomWords = relationship('ClassroomWords', back_populates="Classroom")

    def serialize(self):
        return {
            'id': self.id,
            'teacherId': self.teacherId,
            'name': self.name,
            'classroomCode': self.classroomCode
        }


'''
class Teacher(db.Model):
	__tablename__ = 'Teacher'
	id = Column(Integer, primary_key=True)
	UserId = Column(Integer, ForeignKey('User.id'))
	User = relationship('User')
	Classrooms = relationship("Classroom")


class Classroom(db.Model):
	__tablename__ = 'Classroom'
	id = Column(Integer, primary_key=True)
	TeacherId = Column(Integer, ForeignKey('Teacher.id'))
 '''
'''
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))'''
