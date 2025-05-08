import json
from flask import Flask, render_template, request
from src.examiners_flow.main import ExaminersFlow, ExaminersBoardCrew

app = Flask(__name__)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get-mocked', methods=['POST'])
def get_mocked():
    module = request.form.get('module')
    topic = request.form.get('topic')
    grade = request.form.get('grade')
    question_count = request.form.get('question_count')
    exam_board = request.form.get('exam_board')
   
    examiners_flow=ExaminersFlow()

    questions=examiners_flow.start_flow(module, topic, grade, question_count, exam_board)
    print(questions)
    return questions


@app.route('/check-mocked', methods=['POST'])
def check_mocked():
    questions = request.form.getlist('questions')
    module = request.form.get('module')
    topic = request.form.get('topic')
    grade = request.form.get('grade')
    question_count = request.form.get('question_count')
    exam_board = request.form.get('exam_board')
    examiners_flow=ExaminersFlow()
    questions=json.dumps(questions)

    feedback=examiners_flow.start_flow(module, topic, grade, question_count, exam_board, questions)
    print(feedback)
    return feedback

app.run(
    debug=True,
    host="0.0.0.0",
    port=80)