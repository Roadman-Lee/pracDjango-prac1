# 동일 폴더상(pracapp)의 urls.py의 path('', view.함수이름)의 함수 이름으로 사용자가 사용한 함수를 알려준다.  
from ast import Return
import re
from django.shortcuts import render, HttpResponse
import random # 동적인 웹 어플리케이션을 만들기 위한 random 모듈 import

# def index(request): 
#     return HttpResponse('<h1>Random</h1>'+str(random.random())) # 웹페이지에 들어갈때마다 랜덤으로 바뀔 수 random 메서드 입력
#     # 위의 코드로 인해서 웹 어플리케이션 서버를 왜 만들까에 대한 가치를 확인시켜줌. (웹 서버는 준비된 페이지만 보여줄 수 있기 때문)
topics =[
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'}
]

def HTMLTemplate(articleTag): # HTML코드를 재활용하기 위해 함수로 만든다.
    global topics # topics를 index함수안에서만 변수로 쓰고자 global을 붙여서 전역변수로 만든다.
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        print(topic)
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic["id"] == int(id): # read 함수로 받는 argument인 id가 string이기 때문에 topics의 id의 타입과 같게하기 위해서 int로 형변환 시켜준다.
            article = f"<h2>{topic['title']}</h2>{topic['body']}"
    return HttpResponse(HTMLTemplate(article))


def create(request):
    return HttpResponse('create')


    