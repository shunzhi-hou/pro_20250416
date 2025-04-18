import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("IRIS品種預測")
#載入模型
knn = joblib.load("model/KNN.joblib")
Log = joblib.load("model/LogR.joblib")
rf = joblib.load("model/RF.joblib")
svm = joblib.load("model/svm.joblib")  
#布置左側元件
m = st.sidebar.selectbox("請選擇模型:",
                         ("KNN",
                         "LogisticRegression",
                         "RandomForestClassifier",
                         "SVM"))
if m == "KNN" :
    model = knn
elif m == "LogisticRegression":
    model = Log
elif m == "RandomForestClassifier":
    model = rf
elif m== "SVM":
    model = svm
#布置右測元件
df = pd.read_csv("iris.csv")
se1 = st.slider("### 花萼的長度(cm)",
                float(df["sepal.length"].min()),
                float(df["sepal.length"].max()),
                float(df["sepal.length"].mean()))
se2 = st.slider("### 花萼的寬度(cm)",
                float(df["sepal.width"].min()),
                float(df["sepal.width"].max()),
                float(df["sepal.width"].mean()))
se3 = st.slider("### 花瓣的長度(cm)",
                float(df["petal.length"].min()),
                float(df["petal.length"].max()),
                float(df["petal.length"].mean()))
se4 = st.slider("### 花瓣的寬度(cm)",
                float(df["petal.width"].min()),
                float(df["petal.width"].max()),
                float(df["petal.width"].mean()))
st.image("iris.png")

#進行預測
labels = ["Setosa","Versicolor","Virginica"]
if st.button("進行預測"):
    X = [[se1,se2,se3,se4]]
    y_pred = model.predict(X)
    st.write(y_pred)
    st.write("預測品種",labels[y_pred[0]])
