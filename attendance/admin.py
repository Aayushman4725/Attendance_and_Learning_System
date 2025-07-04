from django.contrib import admin
from .models import Department, Group, UserGroup, Schedule, Attendance,Course
# Register your models here.
admin.site.register(Department)
admin.site.register(Group)  
# admin.site.register(UserGroup)
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Course)

@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('user',)  # So you can pick users in a widget