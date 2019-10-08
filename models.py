from app import db


class Questions_Answers(db.Model):
    __tablename__ = 'questions_answers'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    option1 = db.Column(db.String())
    option2 = db.Column(db.String())
    option3 = db.Column(db.String())
    option4 = db.Column(db.String())
    correct_answer = db.Column(db.Integer)

    def __init__(self, question, option1, option2, option3, option4, correct_answer):
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_answer = correct_answer

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'question': self.question,
            'option1': self.option1,
            'option2': self.option2,
            'option3': self.option3,
            'option4': self.option4,
            'correct_answer': self.correct_answer,
        }
