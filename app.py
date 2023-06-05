from flask import Flask, render_template, request, jsonify, logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from random import randint
from appconfig.config import DevelopmentConfig, ProductionConfig
from model import db, TrainingLog
from flask_cors import CORS
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import os

app = Flask(__name__)
jwt = JWTManager(app)
CORS(app)


if os.getenv("RUNENVIRONMENT") == "Production":
    app.config.from_object(ProductionConfig())
    print("Environment: Production")
else:
    app.config.from_object(DevelopmentConfig())
    print("Environment: Development")

db.app = app
db.init_app(app)
migrate = Migrate(app, db)

# For debugging purposes, keep out of production code:
# @jwt.invalid_token_loader
# def invalid_token_callback(error):
#     print("Invalid token callback")
#     print("Error:", error)
#     return jsonify({"msg": "Invalid token"}), 422


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/addLogEntry", methods=["POST"])
@jwt_required()
def api_add_log_entry():
    data = request.get_json()
    log_entry = TrainingLog()
    print(data)
    log_entry.Name = data["name"]
    log_entry.StartTime = datetime.fromisoformat(data["starttime"])
    log_entry.EndTime = datetime.fromisoformat(data["endtime"])
    db.session.add(log_entry)
    db.session.commit()

    response = jsonify(log_entry.to_dict())
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/api/getLogEntry/<id>")
@jwt_required()
def get_log_entry(id):
    log_entry = TrainingLog.query.filter_by(Id=id).first_or_404()
    return jsonify(log_entry.to_dict())

@app.route("/api/getTrainingLog")
@jwt_required()
def get_training_log():
    training_log = TrainingLog.query.all()
    log_entries = []
    for entry in training_log:
        log_entries.append({"id": entry.Id, "name": entry.Name})
    return jsonify(log_entries)

def run():
    with app.app_context():
        print("Doing create_all")
        db.create_all()
        # upgrade()
        app.run()

if __name__ == "__main__":
    run()
