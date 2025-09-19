from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Message(db.Model, SerializerMixin):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)

    created_at = db.Column(DateTime, server_default=func.now())
    updated_at = db.Column(DateTime, onupdate=func.now(), server_default=func.now())

    def __repr__(self):
        return f"<Message {self.id}: {self.username} - {self.body[:20]}>"
