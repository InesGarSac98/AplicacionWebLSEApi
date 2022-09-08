from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Student(db.Model):
	__tablename__ = 'Student'
	id = Column(Integer, primary_key=True)
	userId = Column(Integer, ForeignKey('User.id'), nullable=False)
	classroomId = Column(Integer, ForeignKey('Classroom.id'), nullable=False)
	User = relationship('User')
	Classroom = relationship('Classroom', back_populates="Students")

	def serialize(self):
		userSerialized = None
		if self.User is not None:
			userSerialized = self.User.serialize()
		return {
			'id': self.id,
			'userId': self.userId,
			'classroomId': self.classroomId,
			'user': self.User.serialize()
		}
