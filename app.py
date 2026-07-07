import streamlit as st
import os
from PIL import Image
from llm import explain_food_from_image

# 1. 페이지 레이아웃 및 제목 설정
st.set_page_config(page_title="AI Food Analyzer", page_icon="🥗")
st.title("AI Food Analyzer (Ollama Llava)")
st.caption("음식 사진을 올리면 로컬 AI가 직접 보고 영양 분석을 해줍니다.")

# 2. 파일 업로더 컴포넌트
uploaded_file = st.file_uploader("음식 사진을 올려주세요 (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

# 3. 비즈니스 로직 및 분석 수행
if uploaded_file is not None:
    # 화면에 업로드한 이미지 보여주기
    img = Image.open(uploaded_file)
    st.image(img, caption="업로드된 이미지", use_container_width=True)
    
    # 분석 시작 버튼
    if st.button("영양 분석 시작 🔥"):
        with st.spinner("🤖 Ollama(Llava)가 이미지를 분석하는 중입니다..."):
            try:
                print("🔥 이미지 입력 받음")
                
                # Ollama가 읽을 수 있도록 이미지를 임시 파일로 저장
                # Ollama가 읽을 수 있도록 이미지를 임시 파일로 저장 (RGBA -> RGB 변환 포함)
                temp_path = "temp_input.jpg"
                if img.mode == "RGBA":
                    img = img.convert("RGB")
                img.save(temp_path)

                # Ollama(Llava)가 직접 이미지를 보고 분석 및 설명 생성
                result = explain_food_from_image(temp_path)
                print("🤖 Ollama(Llava) 응답 완료")

                # 분석 완료 후 임시 파일 깔끔하게 삭제
                if os.path.exists(temp_path):
                    os.remove(temp_path)

                print("✅ 정상 완료")
                
                # 결과 출력
                st.success("분석 완료!")
                st.markdown(result)

            except Exception as e:
                print("💥 오류 발생:", str(e))
                st.error(f"❌ 오류 발생: {str(e)}")