from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Association table for many-to-many relationship between Student and Project
student_project = db.Table('student_project',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    projects = db.relationship('Project', secondary='student_project', back_populates='students')

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    projects = db.relationship('Project', backref='instructor', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'), nullable=False)
    milestones = db.relationship('Milestone', backref='project', lazy=True)
    git_info = db.relationship('GitInfo', backref='project', uselist=False)
    students = db.relationship('Student', secondary='student_project', back_populates='projects')

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class GitInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_url = db.Column(db.String(200), nullable=True)
    last_commit = db.Column(db.String(200), nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
