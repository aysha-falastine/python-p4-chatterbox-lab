from app import app
from models import db, Message

with app.app_context():
    print("Seeding messages...")

    db.session.add_all([
        Message(body="Hello world!", username="Asha"),
        Message(body="First post here.", username="Ali"),
        Message(body="Flask is awesome!", username="Fatima"),
    ])

    db.session.commit()
    print("Seeding done.")
