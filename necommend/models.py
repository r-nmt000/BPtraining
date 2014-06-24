from django.db import models
import doctest
# Create your models here.
class Tag(models.Model):
  """
  #create instance
  >>> t1 = Tag(name="white")

  >>> t2 = Tag(name="black")

  #call __unicode__()
  >>> t1
  <Tag: white>
  >>> t2
  <Tag: black>
  """

  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name
 
class Category(models.Model):
  """
  #create instance
  >>> c1 = Category(name="cat")
  >>> c2 = Category(name="human")

  #call __unicode__()
  >>> c1
  <Category: cat>
  >>> c2
  <Category: human>
  """

  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name

class Neco(models.Model):
  """
  #create category and tag instance
  >>> c1 = Category(name="cat")
  >>> c2 = Category(name="human")
  >>> t1 = Tag(name="white")
  >>> t2 = Tag(name="black")
  >>> t3 = Tag(name="big")
 
  #create instance
  >>> n1 = Neco(img="001.jpg",likes=0,explain="big white cat")
  >>> n2 = Neco(img="002.jpg",likes=0,category=c1)
  
  #call __unicode__()
  >>> n1
  <Neco: big white cat>
  >>> n2
  <Neco: >

  #get category of cat
  >>> n2.category
  <Category: cat>
  """

  img = models.CharField(max_length=200)
  likes = models.IntegerField()
  category = models.ForeignKey(Category)
  tags = models.ManyToManyField(Tag)
  explain = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.explain
