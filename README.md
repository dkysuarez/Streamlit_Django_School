# School Management System

This project is a school management system that utilizes Django as the backend framework and Streamlit for the frontend. Its goal is to manage the school's database, allowing users to add, delete, and edit information related to subjects, grades, students, and teachers.

## Key Features:

### Data Models:

- **Subject**: Represents the subjects taught at the school. Each subject has a name and a description.
- **Grade (Note)**: Stores student grades for each subject. Grades can be added, edited, or deleted by the administrator.
- **Student**: Contains information about students, including their name, date of birth, and address.
- **Teacher**: Records details of teachers, such as their name, specialization, and contact information.

### Functionality:

- **Add Data**: Users can input new records for subjects, students, and teachers.
- **Edit Information**: Allows modification of existing details, such as updating grades or changing a student's address.
- **Delete Records**: The administrator can remove subjects, students, or teachers as needed.
- **Restricted Note Access**: Only the administrator has permission to add, edit, or delete grades.

### Technologies Used:

- **Django**: Python framework for the backend. Provides a robust structure for handling business logic, authentication, and database access.
- **Streamlit**: Python library for creating interactive web applications. Used to build a user-friendly and visually appealing interface.

### User Roles:

- **Administrator**: Has full access to the system and can manage all data.
- **Standard Users**: Can view information but cannot modify grades.

---

# Setting Up Streamlit and Django Services

To get your Streamlit and Django services up and running, follow these steps:

1. **Streamlit**:

   - Open a terminal or command prompt.
   - Navigate to the directory where your `app.py` file is located.
   - Execute the following command to start the Streamlit application:
     ```
     streamlit run app.py
     ```
   - This will launch the Streamlit user interface in your web browser.

2. **Django**:

   - Open another terminal or command prompt.
   - Navigate to the root directory of your Django project (where the `manage.py` file is located).
   - Run the following command to start the Django development server:
     ```
     python manage.py runserver
     ```
   - This will start the Django server at `http://127.0.0.1:8000/`.

   ## Requirements

   streamlit
   pandas
   requests
   time
   django
