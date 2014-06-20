from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name
 
class Category(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name

class Neco(models.Model):
  img = models.CharField(max_length=200)
  likes = models.IntegerField()
  category = models.ForeignKey(Category)
  tags = models.ManyToManyField(Tag)
  explain = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.explain
