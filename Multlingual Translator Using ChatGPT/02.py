from flask import Flask
 
app = Flask(__name__) 


# 1. 웰컴 메시지 전달하고 싶을 때 
@app.route('/')
def index():
    return 'Welcome'
 
#2. 생성 웹 페이지를 만들었다면? 아래와 같이 적당히 이름 지정 (페이지 만들기 전에는 http://localhost:5000/create -> page not found) 
@app.route('/create/')
def create():
    return 'Create'
 
#3. 작성한 글의 상세 페이지를 보고 싶을 때 ex. 글 번호  http://localhost:5000/read/1 일때...  
@app.route('/read/1/')
def read():
    return 'Read 1'

#4. 그런데 만약 글 번호를 2, 3, 4, .... 로 바꾸면 어떻게 해야할까? 
# 여기서 바뀌는 값이 무엇인지 찾아보자. -> 글번호임 
@app.route('/read/<id:int>/')    # URL 패턴 정의 <id:int> :동적 요소, 실제 URL에서 이 부분이 임의의 정수로 대체
def read(id):    # read 함수, 라우트 데코레이터에 의해 '/read/<id:int>/' URL로 들어오는 요청을 처리
    print(id)       # 출력
    return 'Read '+id   #클라이언트(웹 브라우저 등)에게 응답을 보내는 코드
 
 
app.run(debug=True)