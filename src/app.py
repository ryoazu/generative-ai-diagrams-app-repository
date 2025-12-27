import streamlit as st
import pandas as pd
import numpy as np

# 1. アプリのタイトルを設定
st.title("📊 シンプル統計アプリ")

# 2. サイドバーで設定を変更できるようにする
st.sidebar.header("設定")
data_points = st.sidebar.slider("データ点数を選んでください", 10, 100, 50)
chart_type = st.sidebar.selectbox("グラフの種類", ["折れ線グラフ", "エリアチャート"])

# 3. メインコンテンツ
st.write(f"現在は {data_points} 個のランダムデータを表示しています。")

# ランダムなデータの生成
chart_data = pd.DataFrame(
    np.random.randn(data_points, 2),
    columns=['データA', 'データB']
)

# 4. 条件分岐によるグラフ表示
if chart_type == "折れ線グラフ":
    st.line_chart(chart_data)
else:
    st.area_chart(chart_data)

# 5. データテーブルの表示
if st.checkbox("生データを表示する"):
    st.subheader("生データ一覧")
    st.write(chart_data)

# 6. インタラクティブなメッセージ
name = st.text_input("あなたの名前を入力してください")
if name:
    st.success(f"こんにちは、{name}さん！アプリが正常に動いています。")