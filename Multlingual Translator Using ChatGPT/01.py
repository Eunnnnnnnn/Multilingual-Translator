from flask import Flask   #Flask 패키지에서 Flask 클래스를 가져오는 코드
import random       #파이썬의 내장 패키지인 random을 가져오는 코드
 
app = Flask(__name__)   # Flask 웹 애플리케이션 인스턴스를 생성하는 코드
                        #__name__ 인자: 애플리케이션의 시작점 알림
 
 
@app.route('/')     #라우트 데코레이터, 웹 브라우저에서 해당 서버의 루트 주소('/')를 방문하면 다음에 정의된 index 함수가 실행
def index():
    return 'vghhfg'    #반환된 문자열은 웹 브라우저에 표시

 
app.run(debug=True)  #디버그 모드에서는 에러가 발생하면 자세한 정보가 웹 페이지에 표시되고, 코드가 변경되면 자동으로 서버가 재시작