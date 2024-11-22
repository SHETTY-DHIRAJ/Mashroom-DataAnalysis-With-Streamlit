import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, PrecisionRecallDisplay
from sklearn.metrics import precision_score, recall_score

def main():
    st.title("Binary Classification Web App")
    st.sidebar.title("Sidebar")
    st.markdown("Are your mushrooms edible or poisonous? 🍄 Let's find out.")
    
    @st.cache_data(persist= True)
    def load_data():
        data= pd.read_csv("mushrooms.csv")

        label= LabelEncoder()

        for col in data.columns:
            data[col]= label.fit_transform(data[col])
        return data
    
    df= load_data()

    if st.sidebar.checkbox("Show raw dataset", False):
        st.subheader("Mushrooms DataSet (Classification)")
        st.write(df)
        st.markdown("This [data set](https://archive.ics.uci.edu/ml/datasets/Mushroom) includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms "
        "in the Agaricus and Lepiota Family (pp. 500-525). Each species is identified as definitely edible, definitely poisonous, "
        "or of unknown edibility and not recommended.")

    @st.cache_data(persist= True)
    def split(df):
        y= df.type
        x= df.drop(columns= ["type"])
        x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state= 0)
        return x_train, x_test, y_train, y_test

    def plot_metrics(metrics_list):
        if "Confusion Matrix" in metrics_list:
            st.subheader("Confusion Matrix")
            # Generate the confusion matrix figure
            fig, ax = plt.subplots()
            ConfusionMatrixDisplay.from_estimator(model, x_test, y_test, display_labels= class_names, ax= ax)
            st.pyplot(fig)
        
        if "ROC Curve" in metrics_list:
            st.subheader("ROC Curve")
            fig, ax = plt.subplots()
            RocCurveDisplay.from_estimator(model, x_test, y_test, ax= ax)
            st.pyplot(fig)

        if "Precision-Recall Curve" in metrics_list:
            st.subheader("Precision-Recall Curve")
            fig, ax = plt.subplots()
            PrecisionRecallDisplay.from_estimator(model, x_test, y_test, ax= ax)
            st.pyplot(fig)

    x_train, x_test, y_train, y_test= split(df)
    class_names= ["edible", "poisonous"]

    st.sidebar.subheader("Choose Classifier")
    classifier= st.sidebar.selectbox("Classifier", ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

    if classifier== "Support Vector Machine (SVM)":
        st.sidebar.subheader("Model Hyperparameters")
        C= st.sidebar.number_input("C (Regularization Parameter)", 0.01, 10.0, step= 0.01, key= "C_SVM")
        kernel= st.sidebar.radio("Kernel", ("rbf", "linear"), key= "kernel")
        gamma= st.sidebar.radio("Gamma (Kernal Coefficient)", ("scale", "auto"), key= "gamma")

        metrics= st.sidebar.multiselect("What metrics to plot?", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))

        if st.sidebar.button("Classify", key= "classify"):
            st.subheader("Support Vector Machine (SVM) Results")
            model= SVC(C= C, kernel= kernel, gamma= gamma)
            model.fit(x_train, y_train)
            accuracy= model.score(x_test, y_test)
            y_pred= model.predict(x_test)
            st.write("Accuracy: ", round(accuracy, 2))
            st.write("Precision: ", round(precision_score(y_test, y_pred, labels= class_names), 2))
            st.write("Recall: ", round(recall_score(y_test, y_pred, labels= class_names), 2))
            plot_metrics(metrics)
        
    if classifier== "Logistic Regression":
        st.sidebar.subheader("Model Hyperparameters")
        C= st.sidebar.number_input("C (Regularization Parameter)", 0.01, 10.0, step= 0.01, key= "C_LR")
        max_iter= st.sidebar.slider("Maximum number of iterations", 100, 500, key= "max_iter")

        metrics= st.sidebar.multiselect("What metrics to plot?", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))

        if st.sidebar.button("Classify", key= "classify"):
            st.subheader("Logistic Regression Results")
            model= LogisticRegression(C= C, max_iter= max_iter)
            model.fit(x_train, y_train)
            accuracy= model.score(x_test, y_test)
            y_pred= model.predict(x_test)
            st.write("Accuracy: ", round(accuracy, 2))
            st.write("Precision: ", round(precision_score(y_test, y_pred, labels= class_names), 2))
            st.write("Recall: ", round(recall_score(y_test, y_pred, labels= class_names), 2))
            plot_metrics(metrics)
    
    if classifier== "Random Forest":
        st.sidebar.subheader("Model Hyperparameters")
        n_estimators= st.sidebar.number_input("The number of trees in the forest", 100, 5000, step= 10, key= "n_estimators")
        max_depth= st.sidebar.number_input("The maximum depth of the tree", 1, 20, step= 1, key= "max_depth")
        bootstrap= st.sidebar.radio("Bootstrap samples while building trees", (True, False), key= "bootstrap")
        metrics= st.sidebar.multiselect("What metrics to plot?", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))

        if st.sidebar.button("Classify", key= "classify"):
            st.subheader("Random Forest Results")
            model= RandomForestClassifier(n_estimators= n_estimators, max_depth= max_depth, bootstrap= bootstrap, n_jobs= -1)
            model.fit(x_train, y_train)
            accuracy= model.score(x_test, y_test)
            y_pred= model.predict(x_test)
            st.write("Accuracy: ", round(accuracy, 2))
            st.write("Precision: ", round(precision_score(y_test, y_pred, labels= class_names), 2))
            st.write("Recall: ", round(recall_score(y_test, y_pred, labels= class_names), 2))
            plot_metrics(metrics)

if __name__ == '__main__':
    main()