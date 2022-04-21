import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np
from datetime import date



cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'Madden41')

#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def getUsersBooks(UserIDtoCheck):
    userBooks = run_query('Select Book.Title, Book.ISBN, Author.fName, Author.lName, CheckedOut.DueDate FROM Reader,Book,CheckedOut,Writes,Author WHERE  Book.ISBN = CheckedOut.ISBN and Author.Author_ID = Writes.Author_ID and Reader.Reader_ID = CheckedOut.Reader_ID and Book.ISBN = Writes.ISBN and Reader.Reader_ID = ' + UserIDtoCheck)
    return userBooks

def isOverdue(UserIDtoCheck):
    overDueCount = run_query('Select COUNT(*) FROM CheckedOut WHERE checkedOut.DueDate < CURDATE() and Reader_ID = ' + UserIDtoCheck)
    return overDueCount 

def getCurrentBalanceOwed(id, amountBooksoverDue):
    overDueInfo = run_query('Select DueDate, DailyFee FROM CheckedOut WHERE checkedOut.DueDate < CURDATE() and Reader_ID = ' + id)
    today = date.today()
  

    amountDue  = 0

    for i in range(0, amountBooksoverDue):
        timePassed = today -overDueInfo[i][0]
        timePassed = timePassed.total_seconds() / 86400
        amountDue += timePassed * overDueInfo[i][1]

    
    return amountDue

                            

def showPage():
    st.title("User's Books")
    UserIDtoCheck = st.text_input(label = "UserID", value = '')
    if st.button(label = 'Search'):
        if UserIDtoCheck == '':
            st.title ("Enter User's ID")
            
        else:
            st.title("Books User have checked out:")
            userBooks = getUsersBooks(UserIDtoCheck)
            userBooks = pd.DataFrame(data = userBooks, columns = ['Book Title', 'ISBN','Author First Name', 'Author Last Name', 'Due Date'])
            userBooks.index = np.arange(1, len(userBooks) + 1)
            st.dataframe(data = userBooks)

            overDueCount = isOverdue(UserIDtoCheck)

            if overDueCount[0][0] != 0:
                st.warning("USER HAS " + str(overDueCount[0][0]) + " OVERDUE BOOKS!")
                amountDue= getCurrentBalanceOwed(UserIDtoCheck, overDueCount[0][0])
                st.error("User owes $" + str(amountDue))

                



    
