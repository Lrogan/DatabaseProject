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


#Code to get the name of the user for the welcome title 
def getUsersName(id): 
    fname = run_query('Select fname FROM Librarian WHERE Staff_ID = ' + id)
    lname = run_query('Select lname FROM Librarian WHERE Staff_ID = ' + id)
    fname = fname[0][0]
    lname = lname[0][0]
    name = str(fname) + " " + str(lname)
    return name

def showPage(id):
    name = getUsersName(id)
    st.title("Hello " + name + "!")
    st.subheader("Welcome to our Library Application") 
    st.write("To navigate the application use the dropdown menu on the left side of the screen.")
