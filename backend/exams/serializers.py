from rest_framework.serializers import ModelSerializer
from .models import Exam

class ExamSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id_exam', 'exam_date', 'exam_type', 'exam_notes', 'exam_result']

