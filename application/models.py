from application import db

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    Idea_tags = db.relationship('Ideas', backref='tag')

class Ideas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)