from django.db import models
from .base_model import BaseModel
from .course import Course
from .course_material import CourseMaterial
from .learner import Learner

class Question(BaseModel):
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
    
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer to {self.question.question_text}"


class Assessment(BaseModel):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_material = models.ForeignKey(CourseMaterial, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=00)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=00)
    
    def __str__(self):
        return f"Assessment for {self.learner.first_name} on {self.course.course_name}"

    def score_update(self):
        
        if self.answer.answer_text == self.question.correct_answer:
            self.score +=1
            self.save()
            return self.score
