#!/usr/bin/env python
import os
import sys
from django.http import HttpResponse

def main():
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BPtraining.settings")
  import csv
  from necommend.models import Neco,Tag,Category

  try:
    csvWriter = csv.writer(open('toRtoaster.csv','ab'))
    # val = 0
    # for num in range(1, 5):
    #  listData = []
    #  val = num
    #  listData.append(val)         
    #  for loop in range(0, 5):
    #    val = val * 10 + num
    #    listData.append(val)
    #    csvWriter.writerow(listData)
    for neco in Neco.objects.all():
      listData = []
      listData.append(neco.id)
      listData.append(neco.img)
      listData.append(neco.category)
      listData.append(neco.explain)
      csvWriter.writerow(listData)
  except Exception as e:
    print e.message

if __name__ == '__main__':
	main()
