#!/usr/bin/env python
import os
import sys

def main():
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BPtraining.settings")
  import csv
  from necommend.models import Neco,Tag,Category

  try:
    catReader = csv.reader(open("necommend/csv/neco.csv"))
    tagReader = csv.reader(open("necommend/csv/tag.csv"))
    # c1 = Category(name="cat")
    # c2 = Category(name="human")
    c1 = Category.objects.get(name="cat")
    c2 = Category.objects.get(name="human")
    print c1
    print c2
    # c1.save()
    # c2.save()

    for t in tagReader:
      tag = Tag()
      tag.name = t[1]
      print tag
      tag.save()

     
    for i,n in enumerate(catReader):
      neco = Neco()
      neco.img = n[0]
      neco.likes = int(n[1])
      neco.explain = n[2]
      #save category
      if n[3] == c1.name:
        neco.category_id = c1.id
      elif n[3] == c2.name:
        neco.category_id = c2.id
      
      neco.save()
      print i
  
      #retrieve tags from cat.csv
      for j,t in enumerate(n):
        if j < 4:
          continue
        tag = Tag.objects.get(name=t)
        neco.tags.add(tag)
        print tag
  
      # print neco
      # neco.save()
      # print neco.category
  
    # for n in Neco.objects.all():
    #   print n.img
    #   tag = Tag.objects.get(name=
  except Exception as e:
    print e.message
    

  #  

if __name__ == '__main__':
	main()
