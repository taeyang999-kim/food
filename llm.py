# llm.py
import google.generativeai as genai
import os

# API 키 설정 (.env 사용 가능)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def explain_food(food_name):
    prompt = f"""
너는 음식 전문가야.

음식: {food_name}

다음 형식으로 한국어로 설명해줘:

1. 음식 설명
2. 예상 칼로리
3. 탄수화물 / 단백질 / 지방 / 나트륨 (대략값)
4. 레시피 (간단히)
5. 건강 팁
"""

    response = model.generate_content(prompt)
    return response.text