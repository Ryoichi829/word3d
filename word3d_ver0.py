# ベクトルの３次元表示
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("３次元ベクトル可視化アプリ")

col1, col2 = st.columns(2) 

with col1:

    df = pd.DataFrame({
        'x':[9, 8, 1, 1],
        'y':[2, 3, 9, 8],
        'z':[5, 5, 8, 9]
    })
    df.index = ['チャーハン', 'カレー', '自転車', '車']

    edited_df = st.data_editor(df)

with col2:

    # ベクトルを表すデータを準備
    vectors = []
    for i in range(4):
        vectors.append(go.Scatter3d(
            x=[0, edited_df.iloc[i, 0]],
            y=[0, edited_df.iloc[i, 1]],
            z=[0, edited_df.iloc[i, 2]],
            mode='lines',
            line=dict(width=10),
            name=list(df.index)[i]  # 各ベクトルに名前を付ける
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
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        width=400,
        height=300,
        legend=dict(
            x=-0.6,    # 凡例を左に配置
            y=0.5,    # 凡例を上に配置
            xanchor='left',
            yanchor='middle'
        )
    )

    # プロットをStreamlitで表示
    st.plotly_chart(fig, use_container_width=True)
