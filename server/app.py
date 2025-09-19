from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

# ------------------- ROUTES -------------------

# GET /messages
@app.get('/messages')
def get_messages():
    messages = Message.query.order_by(Message.created_at.asc()).all()
    return jsonify([m.to_dict() for m in messages])

# GET /messages/:id
@app.get('/messages/<int:id>')
def get_message_by_id(id):
    message = Message.query.get_or_404(id)
    return jsonify(message.to_dict())

# POST /messages
@app.post('/messages')
def create_message():
    data = request.get_json()
    new_message = Message(
        body=data.get("body"),
        username=data.get("username")
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201

# PATCH /messages/:id
@app.patch('/messages/<int:id>')
def update_message(id):
    message = Message.query.get_or_404(id)
    data = request.get_json()
    if "body" in data:
        message.body = data["body"]
    db.session.commit()
    return jsonify(message.to_dict())

# DELETE /messages/:id
@app.delete('/messages/<int:id>')
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return make_response({"message": "Deleted successfully"}, 204)


# ------------------- MAIN -------------------
if __name__ == '__main__':
    app.run(port=5555, debug=True)
