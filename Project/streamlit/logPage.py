import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np
import ReaderHome
import os
import page_helper_function

cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'nopeAdmin') 

#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def login(state): 
    #Code for initial title
    loginWelcome = st.empty()
    loginWelcome = st.title("Welcome to Library!") 

    #Empty states for username and password
    userName = st.empty()
    state.userName = userName.text_input(label = "ID")

    password = st.empty()
    state.password = password.text_input(label = "Password", value = '') 

    #state for reader/staff log in button 
    readerLoginButton = st.empty()
    staffLoginButton = st.empty()

    #Actual Buttons
    readerLoginButtonState = readerLoginButton.button(label = 'Login as Reader')
    staffLoginButtonState  = staffLoginButton.button(label = 'Login as Staff')

    if readerLoginButtonState:
        #checking if fields are filled
        if not state.userName or not state.password:
            st.warning("Please fill all fields") 
            
        #checking if password is correct
        else:
            realPassword = run_query('SELECT Passwords FROM Reader WHERE Reader_ID = ' + state.userName )
            id = state.userName
            if state.password == realPassword[0][0]: 
                #setting initial login states back to empty
                loginWelcome = loginWelcome.empty()
                userName = userName.empty()
                password = password.empty()
                readerLoginButton = readerLoginButton.empty()
                staffLoginButton = staffLoginButton.empty() 
                #new page          
                state.login= True 

            else: 
                st.error("Incorrect Username or Password")


    if staffLoginButtonState:
        #checking if fields are filled
        if not state.userName or not state.password:
            st.warning("Please fill all fields") 
            
        #checking if password is correct
        else:
            realPassword = run_query('SELECT Passwords FROM Librarian WHERE Staff_ID = ' + state.userName )
            if state.password == realPassword[0][0]: 

                #setting initial login states back to empty
                loginWelcome = loginWelcome.empty()
                userName = userName.empty()
                password = password.empty()
                readerLoginButton = readerLoginButton.empty()
                staffLoginButton = staffLoginButton.empty()
            else: 
                st.error("Incorrect Username or Password")

