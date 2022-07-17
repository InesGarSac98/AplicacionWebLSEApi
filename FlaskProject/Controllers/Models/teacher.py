from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# Database ORMs
class Teacher(db.Model):
	__tablename__ = 'Teacher'
	id = Column(Integer, primary_key=True)
	userId = Column(Integer, ForeignKey('User.id'))
	schoolName = Column(String(70))
	User = relationship('User')

	def serialize(self):
		return {
			'id': self.id,
			'userId': self.userId,
			'schoolName': self.schoolName,
			'user': self.User.serialize()
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