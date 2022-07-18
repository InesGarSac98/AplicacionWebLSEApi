from app import db
from sqlalchemy import String, Column, Integer, ForeignKey


class Words(db.Model):
	__tablename__ = 'Words'
	id = Column(Integer, primary_key=True)
	teacherId = Column(Integer, ForeignKey('Teacher.id'), nullable=True)
	name = Column(String(100))
	image = Column(String(1000))
	video = Column(String(1000))
	videoDefinition = Column(String(1000))

	def serialize(self):
		return {
			'id': self.id,
			'teacherId': self.teacherId,
			'name': self.name,
			'image': self.image,
			'video': self.video,
			'videoDefinition': self.videoDefinition
		}
