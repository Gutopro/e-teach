from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
#from rest_framework.permissions import IsAdminUser
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

from api.utils.jwt_utils import get_user_from_request

from ..models.assessment import Assessment
from ..models.question import Question
from ..models.answer import Answer
from ..models.learner import Learner
from ..models.admin import Admin
from ..serializers.assessment import AssessmentSerializer

@cache_page(60 * 15)
@api_view(['POST'])
#@permission_classes([IsAdminUser])
def create_assessment(request):
    """ creates an assessment """
    if request.method == 'POST':
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {"message": "Assessment created successfully", "data": serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)
        response = { "message": "Something went wrong", "error": serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
class AssessmentViewSet(viewsets.ViewSet):
    """list assessments"""
    def list(self, request):
        queryset = Assessment.objects.all()
        serializer = AssessmentSerializer(queryset, many=True)
        return Response(serializer.data)
