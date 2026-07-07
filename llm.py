import ollama

def explain_food_from_image(image_path):
    # 1차: Llava에게 영어로 명확하게 이미지 분석을 요청 (환각 최소화)
    vision_prompt = """
    You are an expert food analyzer.
    Describe the food in the provided image by following this format:
    1. Predicted Food Name
    2. Description of the food
    3. Main Ingredients
    4. Estimated Cooking Method

    Be concise and accurate based on visual evidence.
    """

    try:
        print("1차: Llava 이미지 분석 중...")
        vision_response = ollama.chat(
            model="llava",
            messages=[
                {
                    "role": "user",
                    "content": vision_prompt,
                    "images": [image_path],
                }
            ],
        )

        vision_result = vision_response["message"]["content"]
        print(f"Llava 분석 완료 (영어):\n{vision_result}\n")

        # 2차: Gemma가 영어 분석본을 바탕으로 한글 최종 리포트 작성
        nutrition_prompt = f"""
당신은 영양학 전문가이자 한국 음식 전문가입니다. 
아래의 이미지 분석 결과(영어)를 바탕으로, 해당 음식에 대한 영양 분석 및 레시피 보고서를 '자연스러운 한국어'로 작성하세요.

[이미지 분석 결과]
{vision_result}

[작성할 항목]
1. 음식 이름 (한국어 및 영어 병기)
2. 간단한 설명 (라면 등 면 요리라면 면과 국물의 특징 포함)
3. 예상 칼로리 (kcal) 및 영양성분 (탄수화물, 단백질, 지방, 나트륨 추정치)
4. 간단한 레시피
5. 건강하게 먹는 팁 (나트륨 줄이기 등)

⚠️ [중요 요구사항]
- 답변은 장황한 인사말이나 서론을 제외하고, 군더더기 없이 핵심만 요약해서 간결하게 작성해 주세요. 
- 불필요한 미사여구를 줄여야 출력 속도가 빨라집니다.
- 사용자가 읽기 편하도록 마크다운 서식을 활용해 깔끔하게 응답하세요.
"""

        print("2차: Gemma 영양 분석 및 번역 중...")
        nutrition_response = ollama.chat(
            model="gemma4:e4b",
            messages=[{"role": "user", "content": nutrition_prompt}],
        )

        nutrition_result = nutrition_response["message"]["content"]

        # 최종 결과 반환
        return f"""==============================
📊 AI 음식 분석 결과
==============================

{nutrition_result}
"""

    except Exception as e:
        return f"Ollama 실행 중 오류 발생: {e}"