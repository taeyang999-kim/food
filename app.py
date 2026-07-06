# app.py
import gradio as gr
from predict import predict_food
from llm import explain_food

def analyze(img):
    label, conf = predict_food(img)
    explanation = explain_food(label)

    return f"""
🍽️ 예측 음식: {label}
📊 정확도: {conf:.2f}

---

📖 AI 설명:

{explanation}
"""

demo = gr.Interface(
    fn=analyze,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="AI Food Analyzer (CNN + Gemini)",
    description="음식 사진을 올리면 딥러닝이 분석하고 AI가 설명해줍니다."
)

demo.launch()