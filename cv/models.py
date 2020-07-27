from django.conf import settings
from django.db import models
from django.utils import timezone


class Listing(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    partname = models.CharField(max_length=100)
    part = models.CharField(max_length=50)
    achievement = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.partname

    def get_part(self):
        return self.part