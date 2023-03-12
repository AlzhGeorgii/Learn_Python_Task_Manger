from datetime import datetime

from sqlalchemy.orm import relationship

from webapp.db import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_start = db.Column(db.DateTime, nullable=False, default=datetime.now())
    date_end = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"<Project {self.username}>"


class Project_member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), index=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id", ondelete="CASCADE"), index=True)
    role = db.Column(db.String(10))
    user = relationship("User", backref="project_member")
    project = relationship("Project", backref="project_member")

    def __repr__(self) -> str:
        return f"<Project_member id {self.id} role {self.username}>"
