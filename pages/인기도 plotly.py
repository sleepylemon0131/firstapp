import streamlit as st
import plotly.express as px

# 포켓몬 인기 데이터
pokemon_data = {
    "이름": ["개굴닌자", "루카리오", "뮤", "리자몽", "브이젤", "가디안", "음번", "뮤츠", "이브이", "피카츄"],
    "인기 점수": [140559, 102259, 99077, 93868, 87839, 60496, 59653, 60257, 57462, 48762]
}

# 타이틀
st.title("🔥 포켓몬 인기 Top 10 (Plotly 시각화)")

# Plotly 막대 그래프
fig = px.bar(
    x=pokemon_data["이름"],
    y=pokemon_data["인기 점수"],
    color=pokemon_data["이름"],
    text=pokemon_data["인기 점수"],
    title="포켓몬 인기 투표 결과",
    labels={"x": "포켓몬 이름", "y": "인기 점수"}
)

fig.update_layout(showlegend=False)
fig.update_traces(textposition="outside")

# Streamlit에 출력
st.plotly_chart(fig)
