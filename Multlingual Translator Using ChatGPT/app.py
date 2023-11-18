from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)

# OpenAI API 키 설정
load_dotenv()
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])   # '/translate' 경로에 대한 POST 요청을 처리하는 translate 함수를 정의
def translate():  # 번역 함수 
    source_text = request.form['source_text']    #번역할 텍스트(source_text) html에서 받아오기
    target_language = request.form['target_language']  #대상 언어(target_language) html에서 받아오기 
    # OpenAI API를 사용하여 번역
    response = client.completions.create(
        model="text-davinci-003",  # 업데이트된 모델 사용
        prompt=f"Translate the following text to {target_language}: '{source_text}'",
        max_tokens=150
    )

    # JSON 형식으로 변환
    json_response = json.dumps(response, default=lambda o: o.__dict__, indent=2)

    # 결과 출력
    # print(json_response)
    response_dict = json.loads(json_response)
    translated_text = response_dict['choices'][0]['text'].strip()
    print(f"{translated_text}")

    return render_template('index.html', source_text=source_text, target_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
