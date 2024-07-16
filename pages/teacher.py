import streamlit as st
import pandas as pd
import requests
import time




#endpoint
api_url = "http://127.0.0.1:8000/api/teacher/"

#functions
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data     = response.json()
    return data

def send_data(name, gender, phoneNumber, emailAddreess, salary):
    gender_value = "0" if gender == "Female" else "1"


    data = {
        "name": name,
        "gender": gender_value,
        'phoneNumber':phoneNumber,
        'emailAddress':emailAddreess,
        'salary':salary,
                
    }

    response = requests.post(api_url, json=data)
    return response

def delete_data(teacher_id):
    response = requests.delete(f"{api_url}{teacher_id}/")
    return response

def edit_data(teacher_id ,name, gender, phoneNumber, emailAddreess, salary):
    gender_value = "0" if gender == "Female" else "1"
    data = {
        "name": name,
        "gender": gender_value,
        'phoneNumber':phoneNumber,
        'emailAddress':emailAddreess,
        'salary':salary,
                
    }


    response = requests.put(f"{api_url}{teacher_id}/", json =data)
    return response




st.title("Analytics Dashboard")
st.write("v.0.0.1")


#Fetch data from our API
data  = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)
    st.dataframe(df)



 #Form to collect customer data
name         = st.text_input("Your name")
gender       = st.radio("Select your gender", ['Male', 'Female'])
phoneNumber  = st.number_input("Phone Number")
emailAddress = st.text_input("Email Address")
salary       = st.number_input("Salary")


if st.button("Submit"):
    response = send_data(name, gender,phoneNumber, emailAddress, salary)
    if response.status_code == 201:
        st.success("New teacherdata created")
        time.sleep(2)  # Esperar 2 segundos
        st.rerun()
    else:
        st.error("Something went wrong")


    

def delete_data(teacher_ids):
    for teacher_id in teacher_ids:
        response = requests.delete(f"{api_url}{teacher_id}/")
        if response.status_code == 204:
            st.success(f"Teacher {teacher_id} deleted")
            time.sleep(2) 
            st.rerun()
        else:
            st.error(f"Something went wrong with teacher {teacher_id}")

def edit_data(teacher_ids, name, gender, phoneNumber, emailAddress, salary):
    gender_value = "0" if gender == "Female" else "1"

    data = {
        "name": name,
        "gender": gender_value,
        'phoneNumber':phoneNumber,
        'emailAddress':emailAddress,
        'salary':salary,
                
    }



    for teacher_id in teacher_ids:
        response = requests.put(f"{api_url}{teacher_id}/", json=data)
        if response.status_code == 200:
            st.success(f"Teacher {teacher_id} updated")
            time.sleep(2) 
            st.rerun()
        else:
            st.error(f"Something went wrong with teacher {teacher_id}")

# ...

if data:
    df = pd.DataFrame(data)

    # ...

    selected_teacher_ids = []
    widget_id = (id for id in range(1, 100_00))
    for index, row in df.iterrows():
       if st.checkbox(row['name'], key=next(widget_id)):
        selected_teacher_ids.append(row['id'])

    

    if selected_teacher_ids:
        if st.button("Delete Selected"):
            delete_data(selected_teacher_ids)

        name         = st.text_input("Your name", key="nameTeacher")
        gender       = st.radio("Select your gender", ['Male', 'Female'], key="gender_input")
        phoneNumber  = st.number_input("Phone Number", key="phoneTeacher")
        emailAddress = st.text_input("Email Address", key="emailTeacher")
        salary       = st.number_input("Salary", key= "salaryTeacher")

        if st.button("Edit Selected"):
            edit_data(selected_teacher_ids, name, gender, phoneNumber, emailAddress, salary)
