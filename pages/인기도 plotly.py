import streamlit as st
import plotly.express as px

# 포켓몬 인기 순위 데이터
pokemon_data = {
    "name": ["개굴닌자", "루카리오", "뮤", "리자몽", "브이젤", "가디안", "음번", "뮤츠", "이브이", "피카츄"],
    "eng_name": ["greninja", "lucario", "mew", "charizard", "buizel", "gardevoir", "noivern", "mewtwo", "eevee", "pikachu"],
    "votes": [140559, 102259, 99077, 93868, 87839, 60496, 59653, 60257, 57462, 48762]
}

# 타이틀
st.title("🔥 포켓몬 인기 Top 10")

# Plotly 시각화
fig = px.bar(
    x=pokemon_data["name"],
    y=pokemon_data["votes"],
    color=pokemon_data["name"],
    text=pokemon_data["votes"],
    labels={"x": "포켓몬", "y": "인기 점수"},
    title="2021년 글로벌 인기 투표 결과"
)
fig.update_layout(showlegend=False)
fig.update_traces(textposition="outside")
st.plotly_chart(fig)

# 포켓몬 이미지 출력
st.subheader("📸 포켓몬 이미지 모음")

for name, eng_name in zip(pokemon_data["name"], pokemon_data["eng_name"]):
    img_url = f"https://img.pokemondb.net/artwork/large/{eng_name}.jpg"
    st.markdown(f"### {name}")
    st.image(img_url, width=200)
