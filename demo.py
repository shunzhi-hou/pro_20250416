

import numpy as np
import pandas as pd
import streamlit as st

#文字輸出
st.title("demo1213") 
st.header("123") 
st.text("text")
st.write("Write")
st.write("# 1")
st.write("## 2")
st.write("### 3")

a = np.array([1,2,2,3,4])
st.write(a)
b = pd.DataFrame({"name":["jj","cc","vv"]})
st.write(b)
st.table(b)

#核取方塊
st.write("核取方塊checkbox")
ck = st.checkbox("是否睡了?")
if ck:
    st.text("1")
else:
    st.text("否")
ck2 = st.checkbox("是否醒了?")
if ck2:
    st.text("1")
else:
    st.text("否")

#選項按鈕
st.write("選項按鈕radio")
rb = st.radio("取向:",["f","m","no"])
st.info(rb)
rb2 = st.radio("取向:",["f","m","no"],key="rb2")
st.info(rb2)

#下拉式選單
st.write("下拉式選單selectbox")
sb = st.selectbox("請選擇口味:",["辣",'甜',"苦",'鹹'])
st.info(sb)

#按鈕
st.write("按鈕")
def show():
    st.text("111110")
btn = st.button("按下")
if btn:
    show()

#滑桿
st.write("滑桿")
num = st.slider("請設定k=?",11,22,step=2)
st.info(num)

#側邊攔
st.write("側邊攔sidebar")
st.sidebar.write("#### 側邊攔 ")
st.sidebar.write("下拉式選單selectbox")
sb2 = st.sidebar.selectbox("請選擇口味:",["辣",'甜',"苦",'鹹'],key="sb2")
st.sidebar.info(sb2)

#分欄
st.write("分欄")
cols = st.columns(4)
with cols[0]:
    n1 = st.number_input("數字1",key = "n1")
with cols[1]:
    n2 = st.number_input("數字2",key = "n2")
with cols[2]:
    n3 = st.number_input("數字3",key = "n3")
with cols[3]:
    n4 = st.number_input("數字4",key = "n4")

sum = n1+n2+n3+n4
st.info(sum)

#上傳檔案
st.write("上傳檔案(csv)")
file = st.file_uploader("請選擇csv檔")
if file is not None:
    df = pd.read_csv(file) 
    st.write(df.head(10))
    

