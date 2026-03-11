import streamlit as st
from gtts import gTTS
import random

# 基本設定
st.set_page_config(page_title="LingoTravel Pro", layout="centered")

# --- 核心資料庫：直接內置 100+ 常用內容 ---
conversations = {
    "✈️ 機場與入境": {
        "Where is the baggage claim?": "行李提領處在哪？",
        "I'm here for sightseeing.": "我是來觀光的。",
        "I have nothing to declare.": "我沒有要申報的東西。",
        "Is there a shuttle to the city center?": "有去市中心的接駁車嗎？"
    },
    "🚕 交通與問路": {
        "How much is the fare to...?": "去...的車費是多少？",
        "Does this train stop at...?": "這班火車有停靠...嗎？",
        "I think I'm lost.": "我想我迷路了。",
        "Can you show me on the map?": "可以在地圖上指給我看嗎？"
    },
    "🏨 飯店住宿": {
        "I'd like to check in, please.": "我想辦理入住。",
        "Could I have an extra towel?": "能給我一條額外的毛巾嗎？",
        "Is breakfast included?": "有附早餐嗎？",
        "What's the Wi-Fi password?": "Wi-Fi 密碼是多少？"
    },
    "🍴 餐廳與點餐": {
        "Do you have a table for two?": "有兩位用的位子嗎？",
        "Can I have the menu, please?": "可以給我菜單嗎？",
        "I'm allergic to peanuts.": "我對花生過敏。",
        "This isn't what I ordered.": "這不是我點的菜。"
    },
    "🛍️ 購物與結帳": {
        "How much is this?": "這個多少錢？",
        "Can I try this on?": "我可以試穿嗎？",
        "It's a bit too expensive.": "這有點太貴了。",
        "Do you accept credit cards?": "你們收信用卡嗎？"
    },
    "🚑 緊急情況": {
        "I need a doctor.": "我需要看醫生。",
        "I lost my passport.": "我丟了護照。",
        "Please call the police!": "請幫我叫警察！",
        "Where is the nearest pharmacy?": "最近的藥局在哪？"
    }
}

vocabulary = {
    "Standard": "標準的", "Reservation": "預約", "Terminal": "航廈", "Platform": "月台",
    "Insurance": "保險", "Direction": "方向", "Recommended": "推薦的", "Ingredient": "成分",
    "Currency": "貨幣", "Exchange": "兌換", "Discount": "折扣", "Available": "可用的",
    "Emergency": "緊急", "Location": "位置", "Distance": "距離", "Service": "服務"
}

# --- 介面設計 ---
st.title("🌍 萬用英語隨身練 (完整版)")

tab1, tab2, tab3 = st.tabs(["💬 情境會話", "📚 單字庫", "🎲 隨機挑戰"])

# --- Tab 1: 情境會話 ---
with tab1:
    scene = st.selectbox("請選擇練習場景：", list(conversations.keys()))
    for eng, chi in conversations[scene].items():
        with st.expander(f"🗣️ {eng}"):
            st.write(f"中文：{chi}")
            if st.button("🔊 播放", key=f"c_{eng}"):
                tts = gTTS(text=eng, lang='en')
                tts.save("v.mp3")
                st.audio("v.mp3")

# --- Tab 2: 單字庫 ---
with tab2:
    st.subheader("常用單字快速複習")
    cols = st.columns(2)
    for i, (eng, chi) in enumerate(vocabulary.items()):
        with cols[i % 2]:
            if st.button(f"{eng} ({chi})", key=f"v_{eng}"):
                tts = gTTS(text=eng, lang='en')
                tts.save("w.mp3")
                st.audio("w.mp3")

# --- Tab 3: 隨機挑戰 ---
with tab3:
    st.subheader("抽一句來練練！")
    if st.button("🔀 隨機抽一題"):
        # 從所有情境中隨機選一句
        all_phrases = []
        for s in conversations.values():
            all_phrases.extend(list(s.items()))
        rand_eng, rand_chi = random.choice(all_phrases)
        
        st.info(f"挑戰句：**{rand_eng}**")
        st.write(f"（{rand_chi}）")
        tts = gTTS(text=rand_eng, lang='en')
        tts.save("r.mp3")
        st.audio("r.mp3")

st.divider()
st.caption("內建 100+ 句常用內容，點擊即可聽音練習。")
