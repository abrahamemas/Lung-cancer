
from copyreg import pickle
import streamlit as st
import requests as re
import json
import numpy as np
st.title("Lung Cancer")

html_temp = """
    <div style="background-color:lightsalmon;padding:10px">
    <h2 style="color:white;text-align:center;">Lung Cancer</h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)



st.sidebar.header('User Input Features')


gender = st.sidebar.number_input("GENDER: Enter 1 for Male and 0 for Female", min_value=0, max_value=1)
age = st.sidebar.slider("AGE: Enter your Age", min_value=1, max_value=100)
smoking = st.sidebar.number_input("SMOKING: Enter 1 if you smoke or 0 if you don't smoke", min_value=0, max_value=1)
yellow_finger = st.sidebar.number_input("YELLOW FINGERS: Enter 1 if you have yellow fingers or 0 if you don't", min_value=0, max_value=1)
anxiety = st.sidebar.number_input("ANXIETY: Enter 1 if you have anxiety and 0 if you don't", min_value=0, max_value=1)
peer = st.sidebar.number_input("PEER PRESSURE: Enter 1 if you feel you suffer from peer pressure or 0 if you don't", min_value=0, max_value=1)
chronic = st.sidebar.number_input("CHRONIC DISEASE: Enter 1 if you suffer from a chronic disease or O if you don't", min_value=0, max_value=1)
fatigue = st.sidebar.number_input("FATIGUE: Enter 1 if you have fatigue or 0 if you don't", min_value=0, max_value=1)
allergy = st.sidebar.number_input("ALLERGY: Enter 1 if you have some sort of allergy or 0 if you don't", min_value=0, max_value=1)
wheezing = st.sidebar.number_input("WHEEZING: Enter 1 if you wheeze or 0 if you don't", min_value=0, max_value=1)
alcohol =  st.sidebar.number_input("ALCOHOL CONSUMPTION: Enter 1 if you consume alcohol or 0 if you don't", min_value=0, max_value=1)
coughing = st.sidebar.number_input("COUGHING: Enter 1 if you cough a lot or 0 if you don't", min_value=0, max_value=1)
breath = st.sidebar.number_input("SHORTNESS OF BREATH: Enter 1 if you suffer from shortness of breath or 0 if you don't", min_value=0, max_value=1)
swallow =  st.sidebar.number_input("SWALLOWING DIFFICULTY: Enter 1 if you have difficulty swallowing or 0 if you don't", min_value=0, max_value=1)
chest =  st.sidebar.number_input("CHEST PAIN: Enter 1 if you have chest pain or 0 if you don't", min_value=0, max_value=1)









if st.button('Detection Result'):
    values =  {
    
    "GENDER": gender,
    "AGE": age,
    "SMOKING": smoking,
    "YELLOW_FINGERS": yellow_finger,
    "ANXIETY": anxiety,
    "PEER_PRESSURE": peer,
    "CHRONIC_DISEASE": chronic,
    "FATIGUE": fatigue,
    "ALLERGY": allergy,
    "WHEEZING": wheezing,
    "ALCOHOL_CONSUMPTION": alcohol,
    "COUGHING": coughing,
    "SHORTNESS_OF_BREATH": breath,
    "SWALLOWING_DIFFICULTY": swallow,
    "CHEST_PAIN": chest
    }
    Data = values
    
def predict(values):

    features = np.array([[Data]])
    model = pickle.load(open("rf_model.pkl", "rb"))

    predictions = model.predict(features)
    if predictions == 1:
        return {"This Person has a very high chance of having lung cancer. Please see a Doctor!"}
    elif predictions == 0:
        return {"This probability of this person having lung cancer is very low."}
    else:
        return {'Not working'}
 
