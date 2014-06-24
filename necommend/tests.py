from django.test import TestCase
from necommend.models import Neco,Tag,Category
from necommend import models
import doctest
# Create your tests here.

#doctest
def load_doctests(loader, tests, ignore):
  tests.addTests(doctest.DocTestSuite(models))
  return tests

def load_unittests(loader, tests, ignore):
  tests.addTests(doctest.DocTestSuite())
  return tests

class TagTestCase(TestCase):

  def setUp(self):
    self.t1 = Tag(name="white")
    self.t2 = Tag(name="big")

  def testName(self):
    self.assertEquals(self.t1.name,'white' )
    self.assertEquals(self.t2.name, 'big')

class CategoryTestCase(TestCase):

  def setUp(self):
    self.c1 = Category(name="cat")
    self.c2 = Category(name="human")

  def testName(self):
    self.assertEquals(self.c1.name,'cat' )
    self.assertEquals(self.c2.name, 'human')


class NecoTestCase(TestCase):

  def setUp(self):
    self.t1 = Tag(name="white")
    self.t2 = Tag(name="big")
    self.c1 = Category(name="cat")
    self.c2 = Category(name="human")
    self.n1 = Neco(img="001.jpg",likes=0,explain="big white cat")
    self.n2 = Neco(img="002.jpg",likes=0,category=self.c1)

  def testImg(self):
    self.assertEquals(self.n1.img,'001.jpg' )
    self.assertEquals(self.n2.img, '002.jpg')
  def testLikes(self):
    self.assertEquals(self.n1.likes,0 )
    self.assertEquals(self.n2.likes,0 )
  def testExplain(self):
    self.assertEquals(self.n1.explain,'big white cat' )
    self.assertEquals(self.n2.explain, '')
  def testCategory(self):
    # self.assertEquals(self.n1.category,"Neco has no Category." )
    self.assertEquals(self.n2.category,self.c1) 

