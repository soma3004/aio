import streamlit as st
import pandas as pd

st.title("物理基礎")

st.write("物理基礎の公式:")

options = ['変位','速度','等速直線運動','合成速度','相対速度','加速度','等加速度直線運動','鉛直投げ下ろし','鉛直投げ上げ','自由落下','水平投射']
selection = st.selectbox("表示したい公式を選んでください:",options)
if selection == '変位':
    st.subheader("変位")
    st.write("")
    st.latex(r'\bar{v}=\frac{\Delta x}{\Delta t}')
elif selection == '速度':
    st.subheader("速度")
    st.latex(r'\bar{v}=\frac{x_2-x_1}{t_2-t_1}=\frac{\Delta x}{\Delta t}')
    st.write("　　ｖ：速さ　　ｘ：移動距離　　ｔ：経過時間")
    st.write("単位時間当たりの移動距離")
    st.text("単位：ｍ／ｓ（メートル毎秒）etc")
    
elif selection == '等速直線運動':
    st.subheader("等速直線運動")
    st.latex(r'x=vt')
    st.write("一直線上を一定の速さで進む運動のこと")
elif selection == '合成速度':
    st.subheader("合成速度")
    st.latex(r'\vec{v}=\vec{v_1}+\vec{v_2}')
elif selection == '相対速度':
    st.subheader("相対速度")
    st.latex(r'\vec{v_(ab)}=\vec{v_b}-\vec{v_a}')
elif selection == '加速度':
    st.subheader("加速度")
    st.latex(r'a=\frac{x_2-x_1}{t_2-t_1}')
elif selection == '等加速度直線運動':
    st.subheader("等加速度直線運動")
    st.latex(r'v=v_o+at')
    st.latex(r'x=v_ot+\frac{1}{2}at^2')
    st.latex(r'v^2-v_o^2=2ax')
elif selection == '自由落下':
    st.subheader("自由落下")
    st.latex(r'v=gt')
    st.latex(r'y=\frac{1}{2}gt^2')
    st.latex(r'v^2=2gy')
elif selection == '鉛直投げ下ろし':
    st.subheader("鉛直投げ下ろし")
    st.latex(r'v=v_o+gt')
    st.latex(r'y=v_ot+\frac{1}{2}gt^2')
    st.latex(r'v^2-v_o^2=2gy')
elif selection == '鉛直投げ上げ':
    st.subheader("鉛直投げ上げ")
    st.latex(r'v=v_o-gt')
    st.latex(r'y=v_o-\frac{1}{2}gt^2')
    st.latex(r'v^2-v_o^2=-agy')
elif selection == '水平投射':
    st.write("水平投射")
    st.latex(r'x=v_ot')
    st.latex(r'y=\frac{1}{2}gt^2')




