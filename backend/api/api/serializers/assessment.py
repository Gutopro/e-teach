from rest_framework import serializers
from ..models.assessment import Assessment, Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['course_material', 'question_text', 'correct_answer']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:model = Answer
    fields = [ 'question', 'answer_text', 'is_correct']

class AssessmentSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Assessment
        fields = ['id','learner', 'course', 'course_material','answers', 'question', 'answer']
