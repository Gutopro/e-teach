from django.db import models
from .learner import Learner
from .question import Question

ANSWER_CHOICES = [
    ("choice_1", "Answer_1"),
    ("choice_2", "Answer_2"),
    ("choice_3", "Answer_3"),
    ("choice_4", "Answer_4"),
    ("choice_5", "Answer_5"),
    ("choice_6", "Answer_6"),
]

class Answer(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, related_name='answers', default=1)  # Use default value
    selected_choice = models.CharField(max_length=50, choices=ANSWER_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.learner.first_name} - {self.question.question_text}"
