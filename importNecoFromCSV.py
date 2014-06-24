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
    if Category.objects.all():
      print "table has category"
      c1 = Category.objects.get(name="cat")
      c2 = Category.objects.get(name="human")
    else:
      print "tabla does not have category"
      c1 = Category(name="cat")
      c2 = Category(name="human")
      c1.save()
      c2.save()

    #create tags
    if not( Tag.objects.all()):
      for t in tagReader:
        tag = Tag()
        tag.name = t[1]
        print tag
        tag.save()

    #create necos
    if not (Neco.objects.all()):
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

  except Exception as e:
    print e.message
  #   

  #  

if __name__ == '__main__':
	main()
