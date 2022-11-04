"""This is a simple script that takes names of the files from Names.txt and then renames the required files in the format of 1.name"""
import os
f1=open("Names.txt",'r', encoding='utf-8')
count=0
for line in f1:
    count+=1
    old_name=r"fileWithOldName.format"
    new_name=r"{}.{}.format".format(count,line[:-1].replace(":","-").replace('"',"'").replace("/","-")) """File name doesn't support the characters :,",/,\ so replaced them with other characters"""
    print(old_name) """prints the old name"""
    os.rename(old_name, new_name)

