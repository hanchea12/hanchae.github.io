#!C:\Users\an001\AppData\Local\Programs\Python\Python39\python.exe

import cgi
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+title, 'wt', encoding='UTF8')
opened_file.write(description)

#Location 이 주소로 이동해! 라는 함수

#Redirection
print("Location: index.py?id="+title)
print()
