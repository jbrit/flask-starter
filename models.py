from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Example(db.Model):
    __tablename__ = 'examples'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Example {}>'.format(self.id)
