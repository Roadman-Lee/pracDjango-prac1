# 동일 폴더상(pracapp)의 urls.py의 path('', view.함수이름)의 함수 이름으로 사용자가 사용한 함수를 알려준다.  
from ast import Return
from asyncio.proactor_events import constants
import re
from django.shortcuts import render, HttpResponse, redirect # redirect 사용하기 위해 import
import random # 동적인 웹 어플리케이션을 만들기 위한 random 모듈 import
from django.views.decorators.csrf import csrf_exempt # CSRF 보안방식을 skip해주는 모듈

nextId = 4
topics =[
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'}
]

# def index(request): 
#     return HttpResponse('<h1>Random</h1>'+str(random.random())) # 웹페이지에 들어갈때마다 랜덤으로 바뀔 수 random 메서드 입력
#     # 위의 코드로 인해서 웹 어플리케이션 서버를 왜 만들까에 대한 가치를 확인시켜줌. (웹 서버는 준비된 페이지만 보여줄 수 있기 때문)

def HTMLTemplate(articleTag, id=None): # HTML코드를 재활용하기 위해 함수로 만든다.
    #id=None 은 기본적으로는 없어도 되지만, id 값의 데이터가 들어오면 사용할 수 있다라는 말이다.
    global topics # topics를 index함수안에서만 변수로 쓰고자 global을 붙여서 전역변수로 만든다.
    cuntextUI = '' # 의도한 상세페이지에서만 삭제버튼이 나오는 것이 아니기때문에 변수를 만들어 home에서는 삭제버튼이 나오지 안게하기위한 변수를 만든다.
    # 아이디 값이 있는지 없는지를 통해서 상세보기 페이지에 있는지 없는지를 알 수 있다. ('/'일때 welcome 이 나오기 때문)
    if id != None: # id 값이 있다면 delete 버튼을 만들어줘라! 라는 코드
        cuntextUI = f'''
            <li>
                <form action="/delete/" method="POST">
                    <input type="hidden" name="id" value={id}> 
                    <input type="submit" value="delete">            
                </form>
            </li>
        '''

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
        <ul>
            <li><a href="/create/">create</a></li>
            {cuntextUI}
        </ul>
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
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    # 장고에서는 ajax를 이용해서 데이터를 보내는 것보다, formTag를 이용한 데이터 이동 방식을 쓰기때문에 formTag의 속성들을 잘 알아둘 필요가 있다.
    if request.method == 'GET': # 장고의 request.method를 통해서 get 방식으로 통신할때 다음의 처리를 할 수 있다.
        article = ''' 
            <form action="/create/" method="POST"> 
                <p><input type="test" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))

    elif request.method == 'POST':
        # print(request.POST['title']) # 프린트로 데이터가 잘 넘어오는 지 확인 -> 확인이 되었다면 이 정보를 가공하자!
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextId) # 생성되기 전의 값을 이용해 url을 만들어주고
        nextId = nextId + 1 # id의 값을 증가시켜줘야한다.
        return redirect(url) # redirect 함수는 url 을 받는다.


@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST['id']
        print(request.POST)
        newTopics =[]
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')