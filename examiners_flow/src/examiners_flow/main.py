#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from .crews.examiners_crew.examiners_crew import ExaminersCrew

from .crews.examiners_board_crew.examiners_board_crew import ExaminersBoardCrew

class ExaminersState(BaseModel):
    module: str=""
    topic: str=""
    grade: str=""
    questions: str=""
    question_count: str=""
    exam_board: str=""
    check: bool = False
    answers: str = ""
 
class ExaminersFlow(Flow[ExaminersState]):

    @start()
    def generate_questions(self):
        print("Generating mock exam")
        if self.state.check == True:
            result = (
                ExaminersBoardCrew()
                .crew()
                .kickoff({
                    "module": self.state.module,
                    "topic":self.state.topic,
                    "grade": self.state.grade,
                    "exam_board": self.state.exam_board,
                    "questions": self.state.questions
                    })
            )
        else:
          
            result = (
                ExaminersCrew()
                .crew()
                .kickoff({
                    "module": self.state.module,
                    "topic":self.state.topic,
                    "grade": self.state.grade,
                    "question_count": self.state.question_count,
                    "exam_board": self.state.exam_board,
                    })
        )
        result = result.raw.replace("```json","")
        result = result.replace("```", "")


        return result
            
    def start_flow(self, module, topic, grade, question_count, exam_board, questions=None):
      if questions != None:
          self.state.check=True
          self.state.questions=questions
      self.state.module=module
      self.state.topic=topic
      self.state.grade=grade
      self.state.question_count=question_count
      self.state.exam_board=exam_board
      return self.kickoff()
   

def kickoff():
    
    examiners_flow = ExaminersFlow()
    examiners_flow.kickoff()


def plot():
    examiners_flow = ExaminersFlow()
    examiners_flow.plot()


if __name__ == "__main__":
    kickoff()
