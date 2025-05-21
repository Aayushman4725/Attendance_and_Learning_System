from django.urls import path
from .views import attendance, attendance_user_group, attendance_create

urlpatterns = [
    path('attendance_date/', attendance, name='attendance'),
    path('attendance_user_group/<int:pk>/', attendance_user_group, name='attendance_user_group'),
    path('attendance_create/', attendance_create, name='attendance_create'),
]