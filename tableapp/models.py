from django.db import models
from django.utils import timezone
from tableapp.choices import DAY_CHOICE

# Create your models here.
class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    day = models.CharField(choices=DAY_CHOICE, default='월요일',  max_length=3,)
    fromTime = models.TimeField(auto_now=False, auto_now_add=False,null=True)
    toTime = models.TimeField(auto_now=False, auto_now_add=False,null=True)
    color = models.CharField(max_length=10, default='#236aff')



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content

    