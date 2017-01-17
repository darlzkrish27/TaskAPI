from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20) #oopss :)  #we can extend length :)
    comment = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
    likers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='likers', blank=True)

    def __str__(self):
        return  "%s" % self.task_name
    
