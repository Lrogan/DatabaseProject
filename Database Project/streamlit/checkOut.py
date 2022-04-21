import streamlit as st 
import mysql.connector
import pandas as pd
import numpy as np

cnx = mysql.connector.connect(user='root', database='Library Management System', password = 'Madden41')

def showPage(id): 
    st.write("Hello!")