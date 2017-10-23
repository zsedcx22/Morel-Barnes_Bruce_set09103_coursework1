import os
import csv

lastFamily=""
lastGenus=""
looper=0
sharks=[]
x=open("CARCHARHINIFORMES.txt")
y=x.read()
sharks=y.split(",")
l=len(sharks)

while looper<l:
  if sharks[looper]=="Family":
    lastFamily=sharks[looper+1]
    os.makedirs(os.path.dirname('sharks/CARCHARHINIFORMES/{0}/'.format(lastFamily)))
    looper+=2
  elif sharks[looper]=="Genus":
    lastGenus=sharks[looper+1]
    os.makedirs(os.path.dirname('sharks/CARCHARHINIFORMES/{0}/{1}/'.format(lastFamily,lastGenus)))
    looper+=2
  else:
    file=open('sharks/CARCHARHINIFORMES/{0}/{1}/{2}.txt'.format(lastFamily,lastGenus,sharks[looper]),'w')
    file.write('{0},{1}'.format(sharks[looper],sharks[looper+1]))
    looper+=2

