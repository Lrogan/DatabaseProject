import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np

cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'nopeAdmin')

#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def showPage(readerId): 
    st.title("My Information:")
    userInfo = run_query('Select Reader_ID,fname,lname,DateOFBirth,Email,Sex FROM Reader WHERE Reader_ID = ' + readerId) 
    userInfo = pd.DataFrame(data = userInfo, columns = ['ID','First Name', 'Last Name', 'DateOFBirth',
                                                         'Email', 'Sex'])
    userInfo.index = np.arange(1, len(userInfo) + 1)
    st.dataframe(data = userInfo) 
    