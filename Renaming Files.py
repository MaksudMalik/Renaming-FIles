#This is a simple script that takes names of the files from Names.txt and then renames the required files in the format of serialno.name.format
import os
f1=open(r"D:\.....\Content Table.txt",'r', encoding='utf-8') #Opening the Content Table file
count=0
for line in f1:
    count+=1
    old_name=r"D:\.....\lesson{}.mp4".format(count)
    new_name=r"D:\.....\{}.{}.mp4".format(count,line[:-1].replace(":","-").replace('"',"'").replace("/","-")) #File name doesn't support the characters :,",/,\ so replaced them with other characters
    os.rename(old_name, new_name)
    print("{} is renamed to{}".format(old_name, new_name)) #prints the old name
