import streamlit as st

# --- 頁面基本設定 ---
st.set_page_config(page_title="GPT 模擬面試官", page_icon="🎤", layout="centered")

# --- 標題 ---
st.title("🎤 GPT 模擬面試官 Interview Bot")
st.markdown("用 GPT 幫你練習面試問題，並即時給予評價與建議。")

# --- 輸入職缺 ---
st.markdown("---")
job_title = st.text_input("🔎 請輸入想要模擬的職位（例如：資料科學家、後端工程師）")
start_button = st.button("🚀 開始模擬")

# --- 啟動模擬 ---
if start_button and job_title:
    # 🔥 這裡應該是呼叫 GPT API 的地方，暫時用假的
    questions = [
        f"1. 請簡述你如何處理 {job_title} 職位中遇到的資料缺失問題？",
        f"2. 在 {job_title} 的工作中，怎麼設計系統來處理高併發請求？",
        f"3. 你覺得成為優秀的 {job_title} 最重要的技能是什麼？"
    ]

    st.session_state.questions = questions
    st.session_state.current_idx = 0
    st.session_state.answers = []

# --- 顯示問題 & 收回答 ---
if "questions" in st.session_state:
    st.markdown("---")
    question = st.session_state.questions[st.session_state.current_idx]
    st.subheader(f"📋 面試問題 {st.session_state.current_idx + 1}")
    st.markdown(f"**{question}**")

    user_answer = st.text_area("📝 請輸入你的回答", key=f"answer_{st.session_state.current_idx}")
    submit_button = st.button("📨 送出回答")

    if submit_button:
        # 🔥 這裡應該要呼叫 GPT API 進行評分，目前用假資料
        fake_scores = {
            "邏輯力": 4,
            "技術理解": 5,
            "表達能力": 3,
            "總結建議": "回答內容邏輯清楚，但可以舉更多實際案例來強化說服力。"
        }

        # 顯示評分區塊
        st.markdown("---")
        st.markdown(
            f"""
            <div style="background-color: #E8F0FE; padding: 20px; border-radius: 10px;">
                <h4>🎯 本題評分</h4>
                <ul>
                    <li><b>邏輯力：</b> {fake_scores['邏輯力']} 分</li>
                    <li><b>技術理解：</b> {fake_scores['技術理解']} 分</li>
                    <li><b>表達能力：</b> {fake_scores['表達能力']} 分</li>
                </ul>
                <p><b>總結建議：</b>{fake_scores['總結建議']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 保存回答
        st.session_state.answers.append({
            "question": question,
            "answer": user_answer,
            "score": fake_scores
        })

        # 前往下一題或結束
        st.session_state.current_idx += 1

        if st.session_state.current_idx >= len(st.session_state.questions):
            st.success("✅ 已完成所有問題！感謝你的作答！")
            # 顯示整體總結可以在這邊加
