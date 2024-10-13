from flask import *
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

import json
import os
import io

from models import *


current_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['SECRET_KEY'] = 'Thisissecret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.sqlite3"


jwt = JWTManager(app)
app.app_context().push()
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


@app.route('/instructor_login', methods=['POST'])
def instructor_login():
    data = request.get_json()
    user = Instructor.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Bad credentials'}), 401

    access_token = create_access_token(identity=user.username, expires_delta=timedelta(seconds=900))
    return jsonify({'access_token': access_token}), 200

@app.route('/student_login', methods=['POST'])
def student_login():
    data = request.get_json()
    user = Student.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Bad credentials'}), 401

    access_token = create_access_token(identity=user.username, expires_delta=timedelta(seconds=900))
    return jsonify({'access_token': access_token}), 200

@app.route('/instructor_signup', methods=['POST'])
def instructor_signup():
    data = request.get_json()
    user = Instructor.query.filter_by(username=data['username']).first()
    if not user:
        hashed_password = generate_password_hash(data['password'])
        new_user = Instructor(username=data['username'], password=hashed_password, email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=new_user.username, expires_delta=timedelta(seconds=900))
        return jsonify({'message': 'Registered successfully', 'access_token': access_token}), 200

    return jsonify({'message': 'User already exists'}), 400

@app.route('/student_signup', methods=['POST'])
def student_signup():
    data = request.get_json()
    print('hit')
    print(data)
    user = Student.query.filter_by(username=data['username']).first()
    if not user:
        hashed_password = generate_password_hash(data['password'])
        new_user = Student(username=data['username'], password=hashed_password, email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=new_user.username, expires_delta=timedelta(seconds=900))
        return jsonify({'message': 'Registered successfully', 'access_token': access_token}), 200

    return jsonify({'message': 'User already exists'}), 400



if __name__ == '__main__':
    app.run(debug=True)