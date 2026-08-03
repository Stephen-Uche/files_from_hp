from datetime import datetime
from app.db import sqlalchemy

class Company(sqlalchemy.Model):

	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	name = sqlalchemy.Column(sqlalchemy.String(100), unique=False, nullable=False)
	about = sqlalchemy.Column(sqlalchemy.Text)
	mission_statement = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
	vision = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)	
	contact_email = sqlalchemy.Column(sqlalchemy.String(120), unique=True, nullable=True)
	phone = sqlalchemy.Column(sqlalchemy.Integer, unique=True, nullable=True)
	created_by = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
	created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
	updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)

	address = sqlalchemy.relationship('Addresses', backref='company', lazy='dynamic', passive_deletes=True)
	offerings = sqlalchemy.relationship('Offerings', backref='company', lazy='dynamic', passive_deletes=True)
	core_values = sqlalchemy.relationship('CoreValues', backref='company', lazy='dynamic', passive_deletes=True)

	def __repr__(self):
		return '<Company {}>'.format(self.name)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name, 
			'about': self.about,
			'mission_statement': self.mission_statement,
			'vision': self.vision,
			'contact_email': self.contact_email,
			'phone': self.phone,
			'created_by': self.created_by
		}
	

class Offerings(sqlalchemy.Model):

	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	company_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Company.id, ondelete='CASCADE'))
	offering = sqlalchemy.Column(sqlalchemy.String(120), nullable=False)
	description = sqlalchemy.Column(sqlalchemy.Text)
	created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
	updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<Service {}>'.format(self.offering)

	def to_json(self):
		return {
			'id': self.id,
			'offering': self.offering,
			'description': self.description
		}
	

class CoreValues(sqlalchemy.Model):

	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	company_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Company.id, ondelete='CASCADE'))
	value = sqlalchemy.Column(sqlalchemy.String(120), nullable=False)
	description = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
	created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
	updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<Core Values {}>'.format(self.value)

	def to_json(self):
		return {
			'id': self.id,
			'value': self.value,
			'description': self.description
		}
	

class Addresses(sqlalchemy.Model):

	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	company_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Company.id, ondelete='CASCADE'))
	address = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
	country = sqlalchemy.Column(sqlalchemy.String(30), nullable=True)
	city = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
	postal_code = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
	created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
	updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<Adress {}>'.format(self.address)

	def to_json(self):
		return {
			'id': self.id,
			'address': self.address,
			'country': self.country,
			'city': self.city,
			'postal_code': self.postal_code
		}