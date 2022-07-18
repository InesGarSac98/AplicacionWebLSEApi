from app import db
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


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
