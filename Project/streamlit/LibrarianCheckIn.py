import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np
from datetime import date



cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'nopeAdmin')

#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


#Function to run update queries
def run_query_update(query):
    with cnx.cursor() as cur:
        
        cur.execute(query)
        cnx.commit()
        return cur.fetchone()

def removeCheckedOut(id,ISBN): 
    #getting count of books with this combination 
    count = run_query("SELECT COUNT(*) FROM CheckedOut WHERE Reader_ID = " + str(id) + " and ISBN = " + str(ISBN))
    count = count[0][0]

    if count == 0: 
        st.error("There is no matching Reader ID and ISBN that is checked out.")
    else: 
        run_query_update("DELETE FROM CheckedOut WHERE Reader_ID = " + str(id) + " and ISBN = " + str(ISBN))




def showPage():
    st.title("Check In Book") 

    #User input 
    userID = st.text_input(label = "ID of user", value = '')
    ISBNToCheckIn = st.text_input(label = "ISBN to check in", value = '') 

    if st.button(label = 'Check in'):
        removeCheckedOut(userID,ISBNToCheckIn)
        st.success("Book Successfully Checked In")


    


        












