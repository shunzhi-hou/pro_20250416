import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt



st.title("IRIS樣本資訊")
st.write("### 樣本數: 150筆 X 4個特徵 ,共三種分類")
df = pd.read_csv("iris.csv")
st.write("### 前十筆內容")
st.write(df.head(10))
mapping = {"Setosa":0,"Versicolor":1,"Virginica":2}
color = ["red","green","blue"]

tab1, tab2 = st.tabs(["依花萼長寬","依花瓣長寬"])

with tab1:
    fig, ax = plt.subplots()
    for i,j in mapping.items():
        subset = df[df["variety"]==i]
        ax.scatter(subset["sepal.length"],
                    subset["sepal.width"],
                    label = i)
    ax.set_xlabel("sepal.length")
    ax.set_ylabel("sepal.width")
    ax.legend()
    st.pyplot(fig)
with tab2:
    fig2, ax2 = plt.subplots()
    for i,j in mapping.items():
        subset = df[df["variety"]==i]
        ax2.scatter(subset["petal.length"],
                    subset["petal.width"],
                    label = i)
    ax2.set_xlabel("petal.length")
    ax2.set_ylabel("petal.width")
    ax2.legend()
    st.pyplot(fig2)

# with tab1:
#     fig, ax = plt.subplots()
#     for i,j in mapping.items():
#         subset = df[df[df["variety"]==i]]
#         ax.scatter(subset["sepal.length"],
#                    subset["sepal.width"])
#     ax.set_xlabel("speal.length")
#     ax.set_ylabel("speal.width")
#     ax.legend()
#     st.pyplot(fig)