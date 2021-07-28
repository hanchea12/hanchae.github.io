#!C:\Users\an001\AppData\Local\Programs\Python\Python39\python.exe

import cgi, os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+pageId, 'wt', encoding='UTF8')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

#Location 이 주소로 이동해! 라는 함수

#Redirection
print("Location: index.py?id="+title)
print()
