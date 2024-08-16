from django.contrib import admin
from .models.admin import Admin
from .models.course import Course
from .models.course_material import CourseMaterial
from .models.learner import Learner
from .models.assessment import Assessment
from .models.question import Question
from .models.answer import Answer

admin.site.register([Admin, Course, Learner, CourseMaterial,Assessment, Question, Answer])
