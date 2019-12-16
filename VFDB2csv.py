#vfdbתcsv
import os 
from collections import OrderedDict
import csv
import sys

forall = OrderedDict()

yourdir = sys.argv[1] + "/"#input("dir:")#����ļ�������
mylist = os.listdir(yourdir)#������ȡ�ļ���

def select(file,name):
    forall[name] = []
    for c in file.readlines():
        if c.find("...") != -1 and c.find("gb") != -1:
            #c = c.strip()
            temp = c.split()
            temp1 = temp[1]
            forall[name].append(temp1)
    print("i")

            #�жϴ��ں���
def exist():
    for k in forall[i]:
        if j == k:
            temp = 1
            break
        else:temp = 0
    return temp
            
        
for i in mylist:
    file=open(yourdir+i,'r')
    select(file,i)
    #print(c)
    #print(i)
    file.close()

for i in forall.keys():
    forall_name = []
    forall_name.append(i)
outgo = forall[forall_name[0]]
for j in range(len(forall_name)):
    outgo = list(set(outgo).union(forall[forall_name[j]]))
    #print(outgo)

outmat = OrderedDict()
data = []
for i in forall.keys():
    outmat[i] = []
    for j in outgo:
        ex = exist()
        outmat[i].append(ex)
    outmat[i].append(i)
    data.append(outmat[i])
    
with open('outVFDB.csv', 'w', newline='') as t_file:
    csv_writer = csv.writer(t_file)
    csv_writer.writerow(outgo)
    for l in data:
       csv_writer.writerow(l)