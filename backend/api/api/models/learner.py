from django.db import models
from .base_model import BaseModel
from .course import Course

class Learner(BaseModel):
    """ Learner user definition"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField()
    courses = models.ManyToManyField(Course)