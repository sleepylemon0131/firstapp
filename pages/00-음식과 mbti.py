import streamlit as st

# MBTI별 음식 추천 데이터
mbti_foods = {
    "ISTJ": ["된장찌개", "돈가스", "잡채"],
    "ISFJ": ["김밥", "유부초밥", "떡볶이"],
    "INFJ": ["비건 샐러드", "아보카도 샌드위치", "그릭 요거트"],
    "INTJ": ["스테이크", "트러플 파스타", "카레"],
    "ISTP": ["라멘", "햄버거", "닭강정"],
    "ISFP": ["마카롱", "크로플", "딸기 케이크"],
    "INFP": ["허브차", "오믈렛", "토마토 스파게티"],
    "INTP": ["불고기", "냉면", "고등어조림"],
    "ESTP": ["치킨", "족발", "삼겹살"],
    "ESFP": ["떡볶이", "핫도그", "타코"],
    "ENFP": ["초밥", "리조또", "팬케이크"],
    "ENTP": ["치즈버거", "부리또", "새우튀김"],
    "ESTJ": ["백반 정식", "갈비찜", "오징어볶음"],
    "ESFJ": ["김치찌개", "주먹밥", "계란말이"],
    "ENFJ": ["샐러드볼", "스무디", "닭가슴살 도시락"],
    "ENTJ": ["양꼬치", "마라탕", "랍스터 파스타"]
}

# 앱 제목
st.title("🍱 MBTI 음식 추천기")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_foods.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"🍽 {selected_mbti}에게 어울리는 음식")
    for food in mbti_foods[selected_mbti]:
        st.write(f"- {food}")
