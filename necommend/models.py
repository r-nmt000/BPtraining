from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=200)
 
class Category(models.Model):
  name = models.CharField(max_length=200)

class Neco(models.Model):
  img = models.CharField(max_length=200)
  likes = models.IntegerField()
  category = models.ForeignKey(Category)
  tags = models.ManyToManyField(Tag)

