import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

# Gemini API 설정 (Streamlit Cloud 환경의 Secrets 혹은 로컬의 .env 파일 읽기)
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("⚠️ GEMINI_API_KEY가 설정되지 않았습니다.")

def explain_food_from_image(image_path):
    try:
        print("🚀 Gemini 멀티모달 분석 시작...")
        
        # 1. 이미지 열기
        img = Image.open(image_path)
        
        # 2. 고성능 멀티모달 모델 설정
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # 3. 프롬프트 작성
        prompt = """
당신은 영양학 전문가이자 한국 음식 전문가입니다. 
제공된 이미지를 직접 분석하여, 해당 음식에 대한 영양 분석 및 레시피 보고서를 '자연스러운 한국어'로 작성하세요.

[작성할 항목]
1. 음식 이름 (한국어 및 영어 병기)
2. 간단한 설명 (라면 등 면 요리라면 면과 국물의 특징 포함)
3. 예상 칼로리 (kcal) 및 영양성분 (탄수화물, 단백질, 지방, 나트륨 추정치)
4. 간단한 레시피
5. 건강하게 먹는 팁 (나트륨 줄이기 등)

⚠️ [중요 요구사항]
- 답변은 장황한 인사말이나 서론을 제외하고, 군더더기 없이 핵심만 요약해서 간결하게 작성해 주세요. 
- 사용자가 읽기 편하도록 마크다운 서식을 활용해 깔끔하게 응답하세요.
- 이미지에 없는 가상의 음식을 지어내지 말고, 시각적 증거에 기반해 정확하게 추정하세요.
"""

        # 4. Gemini 호출
        response = model.generate_content([prompt, img])
        print("✅ Gemini 응답 완료")
        
        return response.text

    except Exception as e:
        return f"Gemini 실행 중 오류 발생: {e}"