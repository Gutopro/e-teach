from django.db import models
from .category import Category

ANSWER_CHOICES = {
    "choice_1": "Answer_1",
    "choice_2": "Answer_2",
    "choice_3": "Answer_3",
    "choice_4": "Answer_4",
    "choice_5": "Answer_5",
    "choice_6": "Answer_6",
    }
class Question(models.Model):
    question_text = models.CharField(max_length=255, unique=True)
    correct_answer = models.CharField(max_length=50, choices=ANSWER_CHOICES)
    difficulty_level = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question_text
