#!/usr/bin/env python
import os
import sys

def main():
  
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BPtraining.settings")
  import csv
  from necommend.models import Neco,Tag,Category

  Tag.objects.all().delete()
  Neco.objects.all().delete()

if __name__ == '__main__':
	main()
