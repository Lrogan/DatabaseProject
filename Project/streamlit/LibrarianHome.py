from tabnanny import check
import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np
import ReaderTitlePage
import readerInfo
import myBooks
import LibrarianInfo
import LibrarianTitlePage
import User_Checkout_Books
import LibrarianCheckIn



cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'nopeAdmin') 


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


def showPage(state): 
    # Create a page dropdown 
    page = st.sidebar.selectbox("Select an option", ["Home", "My Information", "View User CheckOut", "Check In", "Logout"])

    if page == "Home":
        LibrarianTitlePage.showPage(state.userName)
    elif page == "My Information":
        LibrarianInfo.showPage (state.userName)
    elif page == "View User CheckOut":
        User_Checkout_Books.showPage() 
    elif page == "Check In":
        LibrarianCheckIn.showPage()
    elif page == "Logout":
        st.title("Log out")
        st.write("Refresh the Page to Complete Log Out Process")
    
   
    

    

    

