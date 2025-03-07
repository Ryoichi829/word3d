# ベクトルの３次元表示
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("３次元ベクトル可視化アプリ")

df = pd.DataFrame({
    'チャーハン':[9, 2, 5],
    'カレー':[8, 3, 5],
    '自転車':[1, 9, 8],
    '車'    :[1, 8, 9]
})
df.index = ['X', 'Y', 'Z']

edited_df = st.data_editor(df)

if st.button('可視化する'):
    # ベクトルを表すデータを準備
    vectors = []
    for i in range(4):
        vectors.append(go.Scatter3d(
            x=[0, edited_df.iloc[0, i]],
            y=[0, edited_df.iloc[1, i]],
            z=[0, edited_df.iloc[2, i]],
            mode='lines',
            line=dict(width=10),
            name=list(df.columns)[i]  # 各ベクトルに名前を付ける
        ))

    # 3次元ベクトル（矢印含む）プロットを作成
    fig = go.Figure(data=vectors)

    # レイアウトを設定
    fig.update_layout(
        title={
            'text': "3次元ベクトル図",
            'x': 0.5
        },
        scene=dict(
            xaxis=dict(title='X軸', backgroundcolor="rgb(200, 200, 230)"),
            yaxis=dict(title='Y軸', backgroundcolor="rgb(230, 200, 230)"),
            zaxis=dict(title='Z軸', backgroundcolor="rgb(230, 230, 200)"),
            camera=dict(eye=dict(x=1.25, y=1.25, z=1.25))
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        width=800,
        height=600
    )

    # プロットをStreamlitで表示
    st.plotly_chart(fig)

    # 内積を表すデータを準備
    matrix = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            matrix[i, j] = edited_df.iloc[0, i] * edited_df.iloc[0, j] \
                         + edited_df.iloc[1, i] * edited_df.iloc[1, j] \
                         + edited_df.iloc[2, i] * edited_df.iloc[2, j]

    # LaTeX数式
    dot_product = r'内積（$$\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2 + a_3b_3$$）'
    st.markdown(dot_product)

    df_inner_product = pd.DataFrame(matrix, 
                      columns=['チャーハン', 'カレー', '自転車', '車'],
                      index=['チャーハン', 'カレー', '自転車', '車'])
    st.dataframe(df_inner_product)
