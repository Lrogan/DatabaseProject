import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np
import ReaderTitlePage
import readerInfo
import myBooks
import browseBooks


cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'nopeAdmin') 


#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

#Code to get the name of the user for the welcome title 
def getUsersName(id): 
    fname = run_query('Select fname FROM Reader WHERE Reader_ID = ' + id)
    lname = run_query('Select lname FROM Reader WHERE Reader_ID = ' + id)
    fname = fname[0][0]
    lname = lname[0][0]
    name = str(fname) + " " + str(lname)
    return name


def showPage(state): 
    # Create a page dropdown 
    page = st.sidebar.selectbox("Select an option", ["Home", "My Information", "My Books", "Browse Books", "Logout"]) 

    if page == "Home":
        ReaderTitlePage.showPage(state.userName)
    elif page == "My Information":
        readerInfo.showPage(state.userName)
    elif page == "My Books":
        myBooks.showPage(state.userName) 
    elif page == "Browse Books":
        browseBooks.showPage(state.userName) 
    elif page == "Logout":
        st.title("Logout") 
        st.write("Refresh the Page to Complete Log Out Process")
        

    

    

