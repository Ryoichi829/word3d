# ベクトルの３次元表示
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("３次元ベクトル可視化アプリ")

col1, col2 = st.columns(2) 

with col1:

    df = pd.DataFrame({
        'x軸':[9, 8, 1, 2],
        'y軸':[8, 8, 9, 8],
        'z軸':[7, 6, 8, 9]
    })
    df.index = ['インスタ', 'X', '自転車', '車']

    edited_df = st.data_editor(df)

with col2:

    # 色をベクトルごとに固定で定義
    colors = ["red", "blue", "green", "orange"]
    # ベクトルを表すデータを準備
    vectors = []
    cones = []
    for i in range(4):
        x=edited_df.iloc[i, 0]
        y=edited_df.iloc[i, 1]
        z=edited_df.iloc[i, 2]
        color=colors[i]
        # ベクトル本体（原点ー＞先端）
        vectors.append(go.Scatter3d(
            x=[0, x],
            y=[0, y],
            z=[0, z],
            mode='lines',
            line=dict(width=6, color=color),
            name=list(df.index)[i]  # 各ベクトルに名前を付ける
        ))
        # 矢印の先端（コーン）
        cones.append(go.Cone(
            x=[x],
            y=[y],
            z=[z],
            u=[x],
            v=[y],
            w=[z],
            sizemode='absolute',
            sizeref=1.2,
            colorscale=[[0, color], [1, color]],
            showscale=False
        ))
    
    # 3次元ベクトル（矢印含む）プロットを作成
    fig = go.Figure(data=vectors+cones)

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
