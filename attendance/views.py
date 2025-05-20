# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Attendance
from .serializers import AttendanceSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def attendance(request):
    if request.method == 'GET':
        attendance_data = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)