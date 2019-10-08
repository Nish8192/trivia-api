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

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getAllQuestions")
def get_all_questions():
    try:
        questions_answers = Questions_Answers.query.all()
        return jsonify([e.serialize() for e in questions_answers]), status.HTTP_200_OK
    except Exception as e:
	    return(str(e))

@app.route("/addQuestion")
def add_question():
    question = request.args.get('question')
    option1 = request.args.get('option1')
    option2 = request.args.get('option2')
    option3 = request.args.get('option3')
    option4 = request.args.get('option4')
    correct_answer = request.args.get('correct_answer')
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
        return "Question and answers added. id={}".format(question_answer.id)
    except Exception as e:
	    return(str(e))
