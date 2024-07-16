import streamlit as st
import pandas as pd
import requests
import time



#endpoint
api_url = "http://127.0.0.1:8000/api/notes/"
 

 
#functions
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data     = response.json()
    return data
    
 

 
 #Fetch data from our API
data    = fetch_data(api_url)

if data:
    df  = pd.DataFrame(data)
    st.dataframe(df)





