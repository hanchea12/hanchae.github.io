#!C:\Users\an001\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html") #파이썬 타입
print()

import cgi,os,view #cgi와 os 모듈을 사용하겠다
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open("data/"+pageId, 'rt', encoding='UTF8').read()
else:
    pageId = 'welcome'
    description = 'Hello, Web'

#methon는 지정하지않으면 기본값인 "get"으로 설정되는데 이때 사용자가 입력한 url이
#그대로 드러나게 됩니다. 따라서 "post"로 설정하게 되면 url방식이 아닌
#다른 은밀한 방식으로 데이터가 전달됩니다

print('''<!doctype html>
<head>
  <meta charset='utf-8'>
  <title>welcome</title>
  <link rel="stylesheet" href="index.css">
</head>
<body>
  <h1><a href="index.py"><strong>Web</strong></a></h1>
    <ul>
        {listli}
    </ul>
    <a href="create.py">create</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="제목을 입력하세요." value="{form_default_title}"></p>
        <p><textarea name="description" placeholder="내용을 입력하세요">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
    <a href="index.py">취소</a>
</body>
'''.format(title=pageId, desc=description, listli=view.getList(), form_default_title=pageId, form_default_description=description))
