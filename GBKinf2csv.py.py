#gbk提取信息
import re
import os 
from collections import OrderedDict
import csv
import sys

forall = OrderedDict()

yourdir = sys.argv[1] + "/"#input("dir:")#输出文件夹名字
mylist = os.listdir(yourdir)#批量读取文件名
pattern = re.compile('"(.*)"')
forall["head"] = ["organism","isolation_source","host","country","lat_lon","collection_date","sample_name"]

def select(file,name):
    forall[name] = [0,0,0,0,0,0,0]
    for c in file.readlines():
        if c.find("isolation_source=") != -1:
            #c = c.strip()
            temp = str(pattern.findall(c))
            forall[name][1] = temp
        if c.find("host=") != -1:
            temp = str(pattern.findall(c))
            forall[name][2] = temp
        if c.find("country=") != -1:
            temp = str(pattern.findall(c))
            forall[name][3] = temp
        if c.find("lat_lon=") != -1:
            temp = str(pattern.findall(c))
            forall[name][4] = temp
        if c.find("collection_date=") != -1:
            temp = str(pattern.findall(c))
            forall[name][5] = temp
        if c.find("organism=") != -1:
            temp = str(pattern.findall(c))
            forall[name][0] = temp
    print("i")
            
for i in mylist:
    file=open(yourdir+i,'r')
    select(file,i)
    #print(c)
    #print(i)
    file.close()
    
#outmat = OrderedDict()
data = []
for i in forall.keys():
    #data = [i]
    temp = str(i)
    forall[i][6] = temp
    data.append(forall[i])
    #data = data.join(temp)
    #print(data)
    
with open('outINF.csv', 'w', newline='') as t_file:
    csv_writer = csv.writer(t_file)
    #csv_writer.writerow(outgo)
    for l in data:
       csv_writer.writerow(l)            