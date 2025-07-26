from django.db import models

# Create your models here.


class TargetUser(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class EmailEvent(models.Model):
    EVENT_CHOICES = (
        ('open', 'Opened Email'),
        ('click', 'Clicked Link'),
        ('input', 'Entered Credentials'),
    )
    user = models.ForeignKey(TargetUser, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.event_type} - {self.timestamp}"

class CapturedCredential(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.password}"
