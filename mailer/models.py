from django.db import models

class EmailRecord(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.EmailField()
    cc = models.TextField(blank=True, null=True)
    bcc = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Email to {self.recipient} - {self.subject}"
