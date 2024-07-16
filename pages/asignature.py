import streamlit as st
import pandas as pd
import requests
import time



#endpoint
api_url = "http://127.0.0.1:8000/api/asignature/"

#functions
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data     = response.json()
    return data

def send_data(nameAsignature, timeperClass):

    data = {
        'nameAsignature':nameAsignature,
        'timeperClass':timeperClass,
            }
    response = requests.post(api_url, json=data)
    return response

def delete_data(asignature_id):
    response = requests.delete(f"{api_url}{asignature_id}/")
    return response



def edit_data(asignature_id, nameAsignature, timeperClass):
    data = {
        'nameAsignature':nameAsignature,
        'timeperClass':timeperClass,
            
    }

    response = requests.put(f"{api_url}{asignature_id}/", json =data)
    return response




 #Fetch data from our API
data    = fetch_data(api_url)

if data:
    df  = pd.DataFrame(data)
    st.dataframe(df)



 #Form to collect customer data
nameAsignature = st.text_input("Asignature")
timeperClass   = st.number_input("Timer per Class")



if st.button("Submit"):
    response = send_data(nameAsignature, timeperClass)
    if response.status_code == 201:
        st.success("New asignaturedata created")
        time.sleep(2)  
        st.rerun()
    else:
        st.error("Something went wrong")


def delete_data(asignature_ids):
    for asignature_id in asignature_ids:
        response = requests.delete(f"{api_url}{asignature_id}/")
        if response.status_code == 204:
            st.success(f"Asignature {asignature_id} deleted")
            time.sleep(2) 
            st.rerun()
        else:
            st.error(f"Something went wrong with asignature {asignature_id}")

def edit_data(asignature_ids,nameAsignature, timeperClass):
    data = {
        'nameAsignature':nameAsignature,
        'timeperClass':timeperClass,
            
    }

    for asignature_id in asignature_ids:
        response = requests.put(f"{api_url}{asignature_id}/", json=data)
        if response.status_code == 200:
            st.success(f"Asignature {asignature_id} updated")
            time.sleep(2)  
            st.rerun()
        else:
            st.error(f"Something went wrong with asignature {asignature_id}")

# ...

if data:
    df = pd.DataFrame(data)

    # ...

    selected_asignature_ids = []
    widget_id               = (id for id in range(1, 100_00))
    for index, row in df.iterrows():
       if st.checkbox(row['nameAsignature'], key=next(widget_id)):
        selected_asignature_ids.append(row['id'])

    

    if selected_asignature_ids:
        if st.button("Delete Selected"):
            delete_data(selected_asignature_ids)

        nameAsignature = st.text_input("Asignature", key= "nameAsignature")
        timeperClass   = st.number_input("Timer per Class", key="timeperClass")

        
        if st.button("Edit Selected"):
            edit_data(selected_asignature_ids, nameAsignature, timeperClass)

