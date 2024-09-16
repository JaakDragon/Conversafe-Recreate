from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid

class Notification(models.Model):
    # Notification Types
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    url = models.CharField(max_length=255)
    uniqueID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', 'is_read'])
        ]

    def __str__(self):
        return f"Notification to {self.user.username}: {self.title}"

    def mark_as_read(self):
        self.is_read = True
        self.save()


