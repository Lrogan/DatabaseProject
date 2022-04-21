import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np

cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'Madden41')

#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def showPage(Staff_ID):
    st.title("My Information:")
    staffInfo = run_query('Select Staff_ID,fname,lname,DateOFBirth,Email,Sex, Hours, Salary FROM Librarian WHERE Staff_ID = ' + Staff_ID)
    staffInfo = pd.DataFrame(data = staffInfo, columns = ['ID','First Name', 'Last Name', 'DateOFBirth','Email', 'Sex', 'Hour of work', 'Salary/hour'])
    staffInfo.index = np.arange(1, len(staffInfo) + 1)
    st.dataframe(data = staffInfo)
    
