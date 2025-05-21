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
    user_name = serializers.CharField(source = 'user.username', read_only=True)
    user_group = serializers.PrimaryKeyRelatedField(queryset=UserGroup.objects.all())
    group_name = serializers.CharField(source = 'user_group.group.name', read_only=True)
    course_name = serializers.CharField(source = 'user_group.course.name', read_only=True)
    date = serializers.DateField(read_only=True)
    check_in = serializers.DateTimeField(read_only=True)
    status = serializers.ChoiceField(choices=[('present', 'Present'), ('absent', 'Absent'), ('leave', 'Leave'), ('late', 'Late')])
    note = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id']
    
    def validate(self, attrs):
        user = attrs.get('user')
        user_group = attrs.get('user_group')
        
        if user and user_group and not user_group.user.filter(id = user.id).exists():
            raise serializers.ValidationError("User does not belong to this group.")
        return attrs