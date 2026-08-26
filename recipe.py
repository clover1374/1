import streamlit as st

# --- App Settings ---
st.set_page_config(page_title="Digital Recipe Kitchen", page_icon="🍳", layout="wide")

# --- Custom Styling for "Shop" Look ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 100px; font-size: 40px; background-color: #f4f0e6; }
    .stButton>button:hover { background-color: #e4e1d9; border: 1px solid #8B4513; }
    .shop-header { text-align: center; background-color: #8B4513; color: white; padding: 15px; border-radius: 10px; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

# --- Recipe Database (Simplified for 30 items) ---
foods = {
    "비빔밥": {"icon": "🥗", "info": "고추장과 나물로 비벼먹는 한식", "recipe": "1. 밥을 짓는다. 2. 각종 나물을 볶는다. 3. 달걀 후라이를 올리고 고추장을 섞는다."},
    "떡볶이": {"icon": "🍡", "info": "매콤달콤한 국민 간식", "recipe": "1. 떡을 불린다. 2. 고추장 육수를 끓인다. 3. 떡과 어묵을 넣고 졸인다."},
    "김밥": {"icon": "🍙", "info": "소풍의 단골 손님", "recipe": "1. 밥에 밑간을 한다. 2. 속재료를 준비한다. 3. 김 위에 밥과 재료를 올리고 말아준다."},
    # ... 여기에 27개를 추가하면 됩니다! (예시로 몇 개 더 추가)
    "피자": {"icon": "🍕", "info": "치즈가 듬뿍 들어간 양식", "recipe": "1. 도우를 편다. 2. 토핑을 올린다. 3. 오븐에 굽는다."},
    "스시": {"icon": "🍣", "info": "신선한 생선 초밥", "recipe": "1. 초대리 밥을 만든다. 2. 생선을 손질한다. 3. 밥 위에 고추냉이와 생선을 올린다."},
}
# 30개를 채우기 위한 더미 데이터 생성
for i in range(1, 26):
    foods[f"요리 {i}"] = {"icon": "🍲", "info": "정성 가득한 요리", "recipe": "레시피가 준비 중입니다."}

# --- Layout ---
st.markdown('<div class="shop-header"><h1>🏠 제미나이의 레시피 상점 (OPEN)</h1></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("🧺 음식이 진열되어 있습니다 (클릭해 보세요)")
    # 6개씩 5줄 = 30개 진열
    grid_cols = st.columns(6)
    for i, (name, data) in enumerate(foods.items()):
        with grid_cols[i % 6]:
            if st.button(data["icon"], key=name):
                st.session_state.selected_food = name

with col_right:
    st.subheader("📜 레시피 보드")
    if "selected_food" in st.session_state:
        selected = st.session_state.selected_food
        st.info(f"선택된 음식: **{selected}**")
        st.write(f"**설명:** {foods[selected]['info']}")
        st.write("---")
        st.write("**[조리 방법]**")
        st.write(foods[selected]["recipe"])
    else:
        st.write("진열대의 음식을 클릭하면 레시피가 나타납니다!")

# --- Status Bar ---
st.sidebar.title("🏪 상점 상태창")
st.sidebar.success("영업 중: 🟢")
st.sidebar.metric("등록된 음식", f"{len(foods)}종")
st.sidebar.write("오늘의 추천: 비빔밥 🥗")
