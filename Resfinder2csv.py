#resfinder转csv
import os 
from collections import OrderedDict
import csv
import sys

forall = OrderedDict()

yourdir = sys.argv[1] + "/"#input("dir:")#输出文件夹名字
mylist = os.listdir(yourdir)#批量读取文件名

def select(file):
    for c in file.readlines():
        #c = c.strip()
        if len(c) > 70 and len(c) < 170:
            if c.find("No hit found")  == -1:
                if c.find("run_info")  == -1:
                    if c.find("HSP_length") != -1:
                        c = c.strip(":")
                        c = c.replace("{","")
                        c = c.replace("'","")
                        c = c.replace('"',"")
                        temp = c.find("HSP_length")
                        c = c[:temp-2]
                        c = c.split()
                        last = c[-1]
                        forall[i].append(last)
    print("i")
#判断存在函数
def exist():
    temp = 0
    for k in forall[i]:
        if j == k:
            temp = 1
            break
        else:temp = 0
    return temp

for i in mylist:
    file=open(yourdir+i,'r')
    forall[i] =[]
    select(file)
    #print(forall)
    file.close()
    
forall_name = []
for i in forall.keys():
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
   
     ##print(data)
with open('outResfinder.csv', 'w', newline='') as t_file:
    csv_writer = csv.writer(t_file)
    csv_writer.writerow(outgo)
    for l in data:
       csv_writer.writerow(l)
    
