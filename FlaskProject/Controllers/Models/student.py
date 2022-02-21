from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Database ORMs
class Student(db.Model):
	__tablename__ = 'Student'
	id = Column(Integer, primary_key=True)
	userId = Column(Integer, ForeignKey('User.id'))
	classroomId = Column(Integer, ForeignKey('Classroom.id'))
	User = relationship('User')
	Classroom = relationship('Classroom', back_populates="Students")

	def serialize(self):
		return {
			'id': self.id,
			'userId': self.userId,
			'classroomId': self.classroomId
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