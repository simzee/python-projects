from ..config import db

class Sock(db.Model):
	__tablename__ = 'socks'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	style = db.Column(db.String)
	color = db.Column(db.String)
	quantity = db.Column(db.Integer)
	price = db.Column(db.Float)
	updated = db.Column(db.String)

	def __init__(self, name, style, color, quantity, price, updated):
		self.name = name
		self.style = style
		self.color = color
		self.quantity = quantity
		self.price = price
		self.updated = updated
