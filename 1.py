# ファイル名：app.py とかにして保存してね

import streamlit as st

# --- 初期設定 ---
st.set_page_config(page_title="キャラ育成アプリ", page_icon="🏃")

# --- キャラの初期体力 ---
if 'hp' not in st.session_state:
    st.session_state.hp = 100  # 体力満タンからスタート

# --- 画面タイトル ---
st.title("🏃‍♀️運動してないとキャラが死ぬアプリ")

# --- 歩数の入力 ---
steps = st.number_input("今日の歩数を入力してね！", min_value=0, step=1)

# --- 計算ボタン ---
if st.button("体力計算！"):
    # 歩数が少ないとダメージ
    if steps >= 5000:
        damage = 0  # たくさん歩いたらダメージなし
    elif steps >= 3000:
        damage = 10
    elif steps >= 1000:
        damage = 30
    else:
        damage = 50  # ほとんど動かなかったら大ダメージ

    # 体力を減らす
    st.session_state.hp = max(0, st.session_state.hp - damage)

# --- キャラの状態表示 ---
st.subheader("🧡キャラの体力")
st.progress(st.session_state.hp)

# --- 死亡判定 ---
if st.session_state.hp == 0:
    st.error("💀 キャラが死んでしまった……")

