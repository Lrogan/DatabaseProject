import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np 
from datetime import date, timedelta


cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'nopeAdmin')

#Function definition to run read quieries
def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

#Function to 
def run_query_update(query):
    with cnx.cursor() as cur:
        
        cur.execute(query)
        cnx.commit()
        return cur.fetchone()

#Function to run query that gets books
def getBooks(): 
    books = run_query('SELECT Title, fname, lname, PageCount, Book.ISBN, Copies FROM Book, Author, Writes WHERE Book.ISBN = Writes.ISBN and Writes.Author_ID = Author.Author_ID;' ) 
    return books

#gets the amount of copies checked out 
def getCopies(ISBN): 
    amount = run_query('SELECT COUNT(*) FROM CheckedOut WHERE ISBN = ' + "'" + str(ISBN) + "'") 
    amount = amount[0][0]
    return amount

#get the total amount of copies that are in a book
def getTotalCopies(ISBN): 
    amount = run_query('SELECT Copies FROM Book WHERE ISBN = ' + "'" + str(ISBN) + "'") 
    amount = amount[0][0]
    return amount

def checkoutBook(id, ISBN, duedate, dailyFee): 
    #st.write("INSERT INTO CheckedOut(" + str(id) +"," + str(ISBN) + "," + "'" + str(duedate) +"'" +","+ str(dailyFee) + ")")
    run_query_update("INSERT INTO CheckedOut VALUES (" + str(id) +"," + str(ISBN) + "," + "'" + str(duedate) +"'" +","+ str(dailyFee) + ")")

def showPage(id):
    st.title("Books in Library:")

    #Get Dataframe for books 
    books = getBooks()
    books = pd.DataFrame(data = books, columns = ['Book Title', 'Author First Name','Author Last Name', 'pages', 'ISBN', 'Copies'])
    books.index = np.arange(1, len(books) + 1)
    st.dataframe(data = books) 


    st.title("Checkout Book:")
    ISBNToCheck = st.text_input(label = "ISBN to check out", value = '')
    if st.button(label = 'CheckOut'):

        #get amount of books able to be checked out
        amountCheckedOut = getCopies(ISBNToCheck)
        amountTotalCopies = getTotalCopies(ISBNToCheck)
        amountLeft = amountTotalCopies - amountCheckedOut


        if amountLeft == 0: 
            st.error("All copies of selected book have been checked out")
        else: 
            #calculating due date 
            today = date.today()
            dueDate = today + timedelta(days=10)
            checkoutBook(id, ISBNToCheck, dueDate, 10)
            st.success("Book Checked Out Successfully")


            







   





