import streamlit as st

# MBTI와 추천 직업 데이터
mbti_jobs = {
    "ISTJ": ["회계사", "군인", "행정 공무원"],
    "ISFJ": ["간호사", "초등교사", "사회복지사"],
    "INFJ": ["상담사", "심리학자", "작가"],
    "INTJ": ["전략기획가", "데이터 과학자", "엔지니어"],
    "ISTP": ["파일럿", "수리공", "응급구조사"],
    "ISFP": ["디자이너", "요리사", "예술가"],
    "INFP": ["시인", "컨텐츠 크리에이터", "인문학 연구자"],
    "INTP": ["연구원", "이론물리학자", "프로그래머"],
    "ESTP": ["기업가", "마케팅 전문가", "소방관"],
    "ESFP": ["배우", "가수", "이벤트 플래너"],
    "ENFP": ["홍보 전문가", "작가", "여행가이드"],
    "ENTP": ["벤처 창업가", "기획자", "광고 디렉터"],
    "ESTJ": ["경영 관리자", "프로젝트 매니저", "경찰"],
    "ESFJ": ["간호사", "상담교사", "호텔 매니저"],
    "ENFJ": ["리더십 코치", "교육 컨설턴트", "사회운동가"],
    "ENTJ": ["CEO", "경영 컨설턴트", "변호사"]
}

# 앱 제목
st.title("🔍 MBTI 기반 직업 추천기")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"💼 {selected_mbti}에게 어울리는 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
