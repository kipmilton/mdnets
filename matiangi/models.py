from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TranscriptionTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='transcription_tasks/')
    task_status = models.CharField(max_length=50, choices=[('completed', 'Completed'), ('pending', 'Pending')])
    earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for {self.user.username} - {self.task_status}"