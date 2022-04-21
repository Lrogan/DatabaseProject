import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np
from datetime import date, timedelta


cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'Madden41')

#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

#Function Definition to get usesr
def getUsersBooks(id): 
    userBooks = run_query('Select Book.Title, Book.ISBN, Author.fName, Author.lName, CheckedOut.DueDate FROM Reader,Book,CheckedOut,Writes,Author WHERE  Book.ISBN = CheckedOut.ISBN and Author.Author_ID = Writes.Author_ID and Reader.Reader_ID = CheckedOut.Reader_ID and Book.ISBN = Writes.ISBN and Reader.Reader_ID = ' + id) 
    return userBooks

def isOverdue(id): 
    overDueCount = run_query('Select COUNT(*) FROM CheckedOut WHERE checkedOut.DueDate < CURDATE() and Reader_ID = ' + id)
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
   

                            

def showPage(id):
    st.title("Books I have checked out:")
    userBooks = getUsersBooks(id)
    userBooks = pd.DataFrame(data = userBooks, columns = ['Book Title', 'ISBN','Author First Name', 'Author Last Name', 'Due Date'])
    userBooks.index = np.arange(1, len(userBooks) + 1)
    st.dataframe(data = userBooks) 

    overDueCount = isOverdue(id) 

    if overDueCount[0][0] != 0:
        st.warning("YOU HAVE " + str(overDueCount[0][0]) + " OVERDUE BOOKS!")
        amountDue = getCurrentBalanceOwed(id, overDueCount[0][0])
        st.error("You currently owe $" + str(amountDue))

        



    
