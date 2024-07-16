import pandas as pd
import requests
import time
import streamlit as st



#endpoint
api_url = "http://127.0.0.1:8000/api/student/"

#functions
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data     = response.json()
    return data

def send_data(name, gender, dateBth):
    gender_value = "0" if gender == "Female" else "1"

    # Convertir el objeto date a una cadena de texto en formato ISO
    dateBth_str = dateBth.strftime('%Y-%m-%d')

    data = {
        "name": name,
        "gender": gender_value,
        'dateBth': dateBth_str
    }

    response = requests.post(api_url, json=data)
    return response

def delete_data(student_ids):
    for student_id in student_ids:
        response = requests.delete(f"{api_url}{student_id}/")
        if response.status_code == 204:
            st.success(f"Student {student_id} deleted")
        else:
            st.error(f"Something went wrong with teacher {student_id}")

def edit_data(student_ids, name, gender, dateBth):
    gender_value = "0" if gender == "Female" else "1"
    dateBth_str  = dateBth.strftime('%Y-%m-%d')

    data = {
        "name": name,
        "gender": gender_value,
        "dateBth" : dateBth_str
    }

    for student_id in student_ids:
        response = requests.put(f"{api_url}{student_id}/", json=data)
        if response.status_code == 200:
            st.success(f"Student {student_id} updated")
        else:
            st.error(f"Something went wrong with student {student_id}")

    response = requests.put(f"{api_url}{student_id}/", json =data)
    return response



 #Fetch data from our API
data  = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)
    st.dataframe(df)



 #Form to collect customer data
name    = st.text_input("Your name")
gender  = st.radio("Select your gender", ['Male', 'Female'])
dateBth = st.date_input("date of birth")



if st.button("Submit"):
    response = send_data(name, gender,dateBth)
    if response.status_code == 201:
        st.success("New studentdata created")
        time.sleep(2)  # Esperar 2 segundos
        st.rerun()
    else:
        st.error("Something went wrong")

def delete_data(student_ids):
    for student_id in student_ids:
        response = requests.delete(f"{api_url}{student_id}/")
        if response.status_code == 204:
            st.success(f"Student {student_id} deleted")
        else:
            st.error(f"Something went wrong with teacher {student_id}")

def edit_data(student_ids, name, gender, dateBth):
    gender_value = "0" if gender == "Female" else "1"
    dateBth_str  = dateBth.strftime('%Y-%m-%d')

    data = {
        "name": name,
        "gender": gender_value,
        "dateBth" : dateBth_str

       
    }

    for student_id in student_ids:
        response = requests.put(f"{api_url}{student_id}/", json=data)
        if response.status_code == 200:
            st.success(f"Student {student_id} updated")
            time.sleep(2)  # Esperar 2 segundos
            st.rerun()
        else:
            st.error(f"Something went wrong with student {student_id}")

# ...

if data:
    df = pd.DataFrame(data)
    # ... (código anterior)

    selected_student_ids = []
    for index, row in df.iterrows():
       checkbox_key = f"checkbox_{row['id']}"
       if st.checkbox(row['name'], key=checkbox_key):
           selected_student_ids.append(row['id'])
    

    if selected_student_ids:
        if st.button("Delete Selected"):
            delete_data(selected_student_ids)

        name     = st.text_input("Your name", key="name_input")
        gender   = st.radio("Select your gender", ['Male', 'Female'], key="gender_input")
        dateBth  = st.date_input("Date")
        if st.button("Edit Selected"):
            dateBth_str = dateBth.strftime('%Y-%m-%d')
            edit_data(selected_student_ids, name, gender, dateBth)
