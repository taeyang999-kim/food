# app.py
import gradio as gr
import os
from llm import explain_food_from_image

def analyze(img):
    try:
        print("🔥 이미지 입력 받음")
        
        # Ollama가 읽을 수 있도록 이미지를 임시 파일로 저장
        temp_path = "temp_input.jpg"
        img.save(temp_path)

        # Ollama(Llava)가 직접 이미지를 보고 분석 및 설명 생성
        result = explain_food_from_image(temp_path)
        print("🤖 Ollama(Llava) 응답 완료")

        # 분석 완료 후 임시 파일 깔끔하게 삭제
        if os.path.exists(temp_path):
            os.remove(temp_path)

        print("✅ 정상 완료")
        return result

    except Exception as e:
        print("💥 오류 발생:", str(e))
        return f"❌ 오류 발생\n\n{str(e)}"

# 그라디오 UI 설정
demo = gr.Interface(
    fn=analyze,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="AI Food Analyzer (Ollama Llava)",
    description="음식 사진을 올리면 로컬 AI가 직접 보고 영양 분석을 해줍니다."
)

if __name__ == "__main__":
    demo.launch()