from django.db import models

# Create your models here.


class MessComplaint(models.Model):
    messName = models.CharField(max_length=255, blank=False, null=False)
    complaint = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.messName
