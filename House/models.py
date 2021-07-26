from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

#create your models here

class Post(models.Model):
    id =models.AutoField
    title = models.CharField(max_length=50,default="")
    description = models.CharField(max_length=300,default="")
    area= models.IntegerField(default=0)
    location= models.CharField(max_length=100, default="")
    price= models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted= models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)


    def __unicode__(self):
        return self.title 

    def get_absolute_url(self):  
        return reverse('post-detail', kwargs={'pk': self.pk})