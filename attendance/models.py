from django.db import models
from django.conf import settings
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50, choices=[('academic', 'Academic'), ('administrative', 'Administrative')])
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subgroups')
    
    def __str__(self):
        return self.name
    
class UserGroup(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_groups')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.group.name
    
class Schedule(models.Model):
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    grace_period_minutes = models.IntegerField(default=15)
    
    def __str__(self):
        return self.group.name

class Attendance(models.Model):
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('present', 'Present'), ('absent', 'Absent'), ('leave', 'Leave'), ('late', 'Late')])
    note = models.TextField(blank=True)
    
    def __str__(self):
        user = getattr(self.user_group.user, "username", "Unknown")
        course = getattr(self.user_group.course, "name", "Unknown")
        group = getattr(self.user_group.group, "name", "Unknown")
        check_in = getattr(self, "check_in", "Unknown")
        return f"{user} - {course} - {group} - {self.date}- {check_in} - {self.status}"
