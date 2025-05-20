from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
from attendance.models import Department
from django.core.exceptions import ValidationError

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(_("Username"), max_length=100, unique=True)
    email = models.EmailField(_("Email"), unique=True)
    role = models.CharField(max_length=20, choices=[('student', 'Student'), ('teacher','Teacher'), ('admin', 'Admin'), ('employee', 'Employee')], default='student')
    department = models.ForeignKey(Department,blank=True, null= True, on_delete = models.SET_NULL)
    roll_number = models.CharField(max_length=20, blank=True, null=True, unique=True)

    # comment = models.TextField(_("Comment"), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','role']  # Add 'username' to REQUIRED_FIELDS
    
    def clean(self):
        super().clean()
        if self.role == 'student' and not self.roll_number:
            raise ValidationError({'roll_number': 'Roll number is required for students.'})
        
    objects = CustomUserManager()

    def __str__(self):
        return self.username

# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     comment_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_negative = models.BooleanField(default=False)
#     needs_review = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Comment by {self.user.username} on {self.blog.title}"

    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='images/profile_picture/default.jpg', upload_to='images/profile_picture')
    phone_number = models.CharField(("Phone Number"), max_length=15, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username