import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("""
# Heart disease Prediction App
""")

st.sidebar.header('User Input Features')



# Collects user input features into dataframe

def user_input_features():
    age = st.sidebar.number_input('Enter your age: ')

    sex  = st.sidebar.selectbox('Sex',(0,1))
    cp = st.sidebar.selectbox('Chest pain type',(0,1,2,3))
    tres = st.sidebar.number_input('Resting blood pressure: ')
    chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
    fbs = st.sidebar.selectbox('Fasting blood sugar',(0,1))
    res = st.sidebar.number_input('Resting electrocardiographic results: ')
    tha = st.sidebar.number_input('Maximum heart rate achieved: ')
    exa = st.sidebar.selectbox('Exercise induced angina: ',(0,1))
    old = st.sidebar.number_input('oldpeak ')
    slope = st.sidebar.number_input('he slope of the peak exercise ST segmen: ')
    

    data = {'age': age,
            'sex': sex, 
            'cp': cp,
            'trestbps':tres,
            'chol': chol,
            'fbs': fbs,
            'restecg': res,
            'thalach':tha,
            'exang':exa,
            'oldpeak':old,
            'slope':slope,
                }
    features = pd.DataFrame(data, index=[0])
    return features

def user_features():

    input_df = user_input_features()
    heart_dataset = pd.read_csv('C:/Users/edenl/Desktop/file_rouge/notebook/original_data/clean_heart_failure_data.csv')

    heart_dataset = heart_dataset.drop(columns=['HeartDisease'])

    df = pd.concat([input_df,heart_dataset],axis=0)

    df = pd.get_dummies(df, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope'])

    df = df[:1] # Selects only the first row (the user input data)

    st.write(input_df)
# Reads in saved classification model
user_features()

def predicting():
    
    df = pd.read_csv('C:/Users/edenl/Desktop/file_rouge/notebook/original_data/clean_heart_failure_data.csv')
    df = df.iloc[:, :11].values
    load_clf = pickle.load(open('C:/Users/edenl/Desktop/file_rouge/pickle_model/heart.pickle', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)

    #
    st.subheader('Prediction')
    st.write(prediction)
    t = st.button('Prediction')
    st.write(t)
    if t : 
        st.write(prediction_proba)
    
    

    #st.subheader('Prediction Probability')
    #st.write(prediction_proba)
predicting()