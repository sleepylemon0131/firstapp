import streamlit as st
import folium
from streamlit_folium import st_folium

# 포켓몬 데이터 + 이미지 URL 추가
pokemon_data = [
    {"name": "피카츄", "eng": "pikachu", "type": "전기", "description": "귀여운 전기쥐 포켓몬", "lat": 37.55, "lon": 126.98},
    {"name": "리자몽", "eng": "charizard", "type": "불꽃/비행", "description": "화염을 내뿜는 용", "lat": 35.18, "lon": 129.07},
    {"name": "뮤", "eng": "mew", "type": "에스퍼", "description": "전설의 포켓몬", "lat": 37.45, "lon": 127.14},
    {"name": "이브이", "eng": "eevee", "type": "노멀", "description": "진화의 가능성이 무한한 포켓몬", "lat": 36.35, "lon": 127.38},
    {"name": "뮤츠", "eng": "mewtwo", "type": "에스퍼", "description": "강력한 유전자 포켓몬", "lat": 37.57, "lon": 126.99},
    {"name": "개굴닌자", "eng": "greninja", "type": "물/악", "description": "닌자형 물 포켓몬", "lat": 35.87, "lon": 128.60},
    {"name": "루카리오", "eng": "lucario", "type": "격투/강철", "description": "파동을 느끼는 포켓몬", "lat": 37.34, "lon": 126.73},
    {"name": "팬텀", "eng": "gengar", "type": "고스트/독", "description": "어둠의 골목을 떠도는 포켓몬", "lat": 35.13, "lon": 126.91},
    {"name": "고라파덕", "eng": "psyduck", "type": "물", "description": "두통이 심하면 폭발적인 힘을 내는 포켓몬", "lat": 33.45, "lon": 126.57},
    {"name": "거다이맥스 피카츄", "eng": "pikachu", "type": "전기", "description": "특별한 거다이맥스 포켓몬", "lat": 37.51, "lon": 127.03}
]

# Streamlit 제목
st.title("🗺️ 인기 Top10 포켓몬 지도 (사진 포함)")

# Folium 지도
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 마커에 포켓몬 사진 포함
for p in pokemon_data:
    image_url = f"https://img.pokemondb.net/artwork/large/{p['eng']}.jpg"
    popup_html = f"""
    <div style="width:200px">
        <h4>{p['name']}</h4>
        <p><b>타입:</b> {p['type']}</p>
        <p>{p['description']}</p>
        <img src="{image_url}" width="150">
    </div>
    """
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

# Streamlit에서 지도 출력
st_folium(m, width=700, height=500)
