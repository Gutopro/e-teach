# models/assessment.py
from django.db import models
from .category import Category
from .question import Question
from .learner import Learner
from .course import Course
from .answer import Answer

class Assessment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='assessments')
    due_date = models.DateField()
    questions = models.ManyToManyField(Question, related_name='assessments')
    feedback = models.TextField(blank=True, null=True)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title


    def update_score(self, answer):
        question = answer.question
        if answer.selected_choice == question.correct_answer:
            self.score += 1
            feedback = "Correct answer."
        else:
            feedback = f"Incorrect answer. The correct answer is {question.correct_answer}."
        self.feedback = feedback
        self.save()
        return self.score, feedback
