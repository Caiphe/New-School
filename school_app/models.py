from django.db import models
from PIL import Image
from django.contrib.auth.models import User


# News Model
class NewsModel(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  news_title = models.CharField(max_length=200, null=False)
  news_details = models.TextField()
  news_image = models.ImageField()
  
  class Meta:
    verbose_name_plural = "News & Events"
  
  def __str__(self):
    return self.news_title
  
  
class StudentModel(models.Model):
  user    = models.ForeignKey(User, on_delete=models.CASCADE)
  name    = models.CharField(max_length=200)
  surname = models.CharField(max_length=200)
  contact = models.CharField(max_length=200)
  age     = models.IntegerField()
  address = models.TextField(max_length=500)
            
  
  
  
  


