from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TrainingLog(db.Model):
    __tablename__ = "TrainingLog"
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), unique=False, nullable=False)
    StartTime = db.Column(db.DateTime)
    EndTime = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id": self.Id,
            "name": self.Name,
            "starttime": self.StartTime,
            "endtime": self.EndTime
        }
