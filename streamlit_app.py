import streamlit as st
import pandas as pd
import random


formulas = [
    r'\bar{v}=\frac{\Delta x}{\Delta t}'
    r"$a^2 + b^2 = c^2$",
    r"$\int_{a}^{b} x^2 \, dx$"
]
selected_formula = st.selectbox(
    "数式を選んでください",
    options=formulas
)
st.latex(selected_formula)

st.title("物理基礎")



st.write("物理基礎の公式:")

st.write("変位")
st.latex(r'\bar{v}=\frac{\Delta x}{\Delta t}')


st.write("速度")
st.latex(r'\bar{v}=\frac{x_2-x_1}{t_2-t_1}=\frac{\Delta x}{\Delta t}')


st.write("等速直線運動")
st.latex(r'x=vt')


st.write("合成速度")
st.latex(r'\vec{v}=\vec{v_1}+\vec{v_2}')


st.write("相対速度")
st.latex(r'\vec{v_(ab)}=\vec{v_b}-\vec{v_a}')


st.write("加速度")
st.latex(r'a=\frac{x_2-x_1}{t_2-t_1}')


st.write("等加速度直線運動")
st.latex(r'v=v_o+at')
st.latex(r'x=v_ot+\frac{1}{2}at^2')
st.latex(r'v^2-v_o^2=2ax')


st.write("自由落下")
st.latex(r'v=gt')
st.latex(r'y=\frac{1}{2}gt^2')
st.latex(r'v^2=2gy')


st.write("鉛直投げ下ろし")
st.latex(r'v=v_o+gt')
st.latex(r'y=v_ot+\frac{1}{2}gt^2')
st.latex(r'v^2-v_o^2=2gy')


st.write("鉛直投げ上げ")
st.latex(r'v=v_o-gt')
st.latex(r'y=v_o-\frac{1}{2}gt^2')
st.latex(r'v^2-v_o^2=-agy')


st.write("水平投射")
st.latex(r'x=v_ot')
st.latex(r'y=\frac{1}{2}gt^2')


st.write("三角比")
st.latex(r'sin\theta=\frac{a}{c}')
st.latex(r'cos\theta=\frac{b}{c}')
st.latex(r'sin30°=\frac{1}{2}')
st.latex(r'sin45°=\frac{√2}{2}')
st.latex(r'sin60°=\frac{√3}{2}')
st.latex(r'cos30°=\frac{√3}{2}')
st.latex(r'cos45°=\frac{√2}{2}')
st.latex(r'cos60°=\frac{1}{2}')
st.latex(r'')
st.latex(r'')

st.write(10^-24)

st.title("単位の変換")
selected_item=st.selectbox("",[
                           "長さ","時間","質量","面積","体積","時速","分速","秒速","密度","圧力","仕事","仕事率","電流","SI接頭語"])


def generate_problem():
    a = random.randint(1,9)
    b = random.randint(1,9)
    return a,b

if 'current_problem' not in st.sessuin_state:
    st.session_state.current_problem = generate_problem()
    st.session_state.user_answer = None
    st.session_state.corrent_answer = st.session_state.current_problem[0]
    st.session_state.result_message = None


a,b = st.session_state.current_problem
st.write(f"問題:{a} × {b} = ?")
user_answer = st.number_input("答えを入力してください",min_value=0,step=1)
if st.button("回答を確認"):
    st.session_state.user_answer = user_answer
    if user_answer == st.session_state.correct_answer:
        st.success("正解です！")
    else:
        st.error(f"不正解です。正しい答えは{st.session_state.correct_answer}です。")

    st.session_state.current_problem = generate_problem()
    st.session_state.correct_answer = st.session_state.current_problem[0]*st.session_state.current_problem[1]

if st.session_state.result_message:
    st.write(st.session_state.result_message)

if st.button("再挑戦"):
    st.session_state.current_problem = generate_problem()
    st.session_state.current_answer = st.session_state.current_problem[0]*st.session_state.current_problem[1]
    st.session_state.result_message = None
    st.session_state.user_answer = None

if st.button("リセット"):
    st.session_state.current_problem = generate_problem()
    st.session_state.corrent_answer = st.session_state.current_problem[0] * st.session_state.current_problem[1]
    st.session_state.result_message = None
    st.session_state.user_answer = None

