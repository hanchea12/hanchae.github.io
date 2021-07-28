#!C:\Users\an001\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html") #파이썬 타입
print()

import cgi,os,sys,io,view,html_sanitizer #cgi와 os 모듈을 사용하겠다
sanitizer = html_sanitizer.Sanitizer()

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

form = cgi.FieldStorage()

if 'id' in form:
    title = pageId = form["id"].value
    description = open("data/"+pageId, 'rt', encoding='UTF8').read()

    #보안
    #description = description.replace('<', '&lt;') #'<' 문자는 웹페이지에서 나타나는 문자로 변경
    #description = description.replace('>', '&gt;') #'&lt;', '&gt;' 는 웹페이지에서 <, >로 약속

    title = sanitizer.sanitize(title) #다운받은 모듈 사용법은 파이썬 홈페이지
    description = sanitizer.sanitize(description)

    update_link = "<a href='update.py?id={}'>수정</a>".format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="삭제">
        </form>
    '''.format(pageId)
else:
    title = pageId = 'welcome'
    description = '어서오시죠, 저의 위대한 실습페이지를 이제부터 소개해 드리도록 하죠'
    update_link = ""
    delete_action = ""

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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
  <a href="create.py">글 작성</a>
</body>
'''.format(title=title, desc=description,
    listli=view.getList(), update_link=update_link,
    delete_action=delete_action))
