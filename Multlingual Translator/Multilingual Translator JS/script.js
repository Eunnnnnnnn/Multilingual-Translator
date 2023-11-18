// Multilingual Translator With ChatGPT CSS/script.js
// 실제 작동X 코드 작성 후 연결시킬 예정

document.addEventListener('DOMContentLoaded', function () {
    var targetTextElement = document.getElementById('target_text');
    var sourceTextElement = document.getElementById('source_text');

    if (targetTextElement && sourceTextElement) {
        var formElement = sourceTextElement.form;

        if (formElement) {
            formElement.addEventListener('submit', function (event) {
                event.preventDefault();

                var sourceText = sourceTextElement.value;
                var targetLanguage = document.getElementById('target_language').value;

                // OpenAI API 호출
                getTranslation(sourceText, targetLanguage)
                    .then(function (translatedText) {
                        targetTextElement.value = translatedText;
                    })
                    .catch(function (error) {
                        console.error('Error fetching translation:', error);
                    });
            });
        }
    }
});

// OpenAI API 호출 함수
function getTranslation(sourceText, targetLanguage) {
    // OpenAI API 엔드포인트와 API 키 설정
    var apiUrl = '/translate';  // 여기에 실제 API 엔드포인트를 넣어주세요.
    var apiKey = 'OpenAI_KEY';  // 여기에 실제 OpenAI API 키를 넣어주세요.

    // OpenAI API 호출
    return fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + apiKey,
        },
        body: JSON.stringify({
            source_text: sourceText,
            target_language: targetLanguage,
        }),
    })
    .then(function (response) {
        if (!response.ok) {
            throw new Error('Failed to fetch translation');
        }
        return response.json();
    })
    .then(function (data) {
        return data.translated_text;
    });
}
