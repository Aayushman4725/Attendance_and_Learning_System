from rest_framework import serializers
from authenticate.models import CustomUser
from .models import Department, Group, UserGroup, Schedule, Attendance


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['id']
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ['id']
        
class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'
        read_only_fields = ['id']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ['id']
        
class AttendanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    date = serializers.DateField()
    check_in = serializers.TimeField(required=False)
    status = serializers.ChoiceField(choices=[('present', 'Present'), ('absent', 'Absent'), ('leave', 'Leave'), ('late', 'Late')])
    note = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id']