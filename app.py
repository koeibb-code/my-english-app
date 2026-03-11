import streamlit as st
from gtts import gTTS
import random

# 基本設定
st.set_page_config(page_title="LingoTravel", layout="centered")

# --- 資料庫：情境會話 ---
conversations = {
    "✈️ 機場/交通": {
        "Where is the boarding gate?": "登機門在哪裡？",
        "I'd like to book a window seat.": "我想訂靠窗的位子。",
        "How often does the shuttle bus run?": "接駁車多久一班？"
    },
    "🛍️ 購物/殺價": {
        "Is there any discount?": "有折扣嗎？",
        "Can I try this on?": "我可以試穿嗎？",
        "I'll take it.": "我要買這個。"
    },
    "🍕 餐廳點餐": {
        "Table for two, please.": "兩位，謝謝。",
        "What is the specialty of the house?": "你們的招牌菜是什麼？",
        "No cilantro, please.": "請不要加香菜。"
    }
}

# --- 資料庫：單字背誦 ---
vocabulary = {
    "Departure": "出發/離境",
    "Reservation": "預約/訂位",
    "Recommendation": "推薦",
    "Ingredient": "成分/配料",
    "Destination": "目的地",
    "Atmosphere": "氣氛",
    "Discount": "折扣"
}

# --- 介面設計 ---
st.title("🌟 旅遊英語隨身練")

# 使用 Tab 標籤頁切換
tab1, tab2 = st.tabs(["💬 情境對話練習", "📚 必背旅遊單字"])

# --- Tab 1: 情境對話 ---
with tab1:
    scene = st.selectbox("選擇練習場景：", list(conversations.keys()))
    st.write("---")
    for eng, chi in conversations[scene].items():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.info(f"**{eng}**")
            with st.expander("看中文意思"):
                st.write(chi)
        with col2:
            if st.button("🔊", key=f"conv_{eng}"):
                tts = gTTS(text=eng, lang='en')
                tts.save("v.mp3")
                st.audio("v.mp3")

# --- Tab 2: 單字背誦 ---
with tab2:
    st.subheader("💡 旅遊生活常用字卡")
    if 'v_idx' not in st.session_state:
        st.session_state.v_idx = 0
    
    words = list(vocabulary.keys())
    current_word = words[st.session_state.v_idx]
    
    # 顯示字卡
    st.markdown(f"""
    <div style="background-color: white; padding: 40px; border-radius: 15px; border: 2px solid #f0f2f6; text-align: center; margin-bottom: 20px;">
        <h1 style="color: #1E3A8A;">{current_word}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🔊 聽讀音"):
            tts = gTTS(text=current_word, lang='en')
            tts.save("w.mp3")
            st.audio("w.mp3")
    with c2:
        if st.button("👀 看意思"):
            st.success(f"意思：{vocabulary[current_word]}")
    with c3:
        if st.button("➡️ 下一個"):
            st.session_state.v_idx = (st.session_state.v_idx + 1) % len(words)
            st.rerun()

st.divider()
st.caption("今天也要加油喔！")
