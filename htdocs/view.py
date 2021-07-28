import os, html_sanitizer

def getList():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data') #'data'의 디렉토리를 리스트로 변환한다
    listli = '' #변수 삽입 (꼭 listli가 아니여도 됨)
    for list in files: #반복문 활용
        list = sanitizer.sanitize(list)
        listli = listli + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=list)
    return listli
