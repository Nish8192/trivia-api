from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask_api import status

app = Flask(__name__)


app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import Questions_Answers

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/getAllQuestions", methods=['GET'])
def get_all_questions():
    try:
        questions_answers = Questions_Answers.query.all()
        if len(questions_answers) == 0:
            return jsonify(["No data available!"]), status.HTTP_200_OK
        else:
            return jsonify([e.serialize() for e in questions_answers]), status.HTTP_200_OK
    except Exception as e:
	    return(str(e))

@app.route("/addQuestion", methods=['POST'])
def add_question():
    if not request.form.get('question') or not request.form.get('option1') or not request.form.get('option2') or not request.form.get('option3') or not request.form.get('option4') or not request.form.get('correct_answer'):
        return jsonify({'error': 'Missing data!'}), status.HTTP_400_BAD_REQUEST
    if not type(request.form.get('question')) is str or not type(request.form.get('option1')) is str or not type(request.form.get('option2')) is str or not type(request.form.get('option3')) is str or not type(request.form.get('option4')) is str or not type(int(request.form.get('correct_answer'))) is int:
        return jsonify({'error': 'Invalid data types!'}), status.HTTP_400_BAD_REQUEST
    question = request.form.get('question')
    option1 = request.form.get('option1')
    option2 = request.form.get('option2')
    option3 = request.form.get('option3')
    option4 = request.form.get('option4')
    correct_answer = request.form.get('correct_answer')
    try:
        question_answer = Questions_Answers(
            question=question,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_answer=correct_answer,
        )
        db.session.add(question_answer)
        db.session.commit()
        return question_answer.serialize(), status.HTTP_201_CREATED
    except Exception as e:
	    return(str(e))
