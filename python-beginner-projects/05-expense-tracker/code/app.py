import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import datetime

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("💰 Expense Tracker")

# Database setup
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY, date TEXT, category TEXT, amount REAL, description TEXT)''')
conn.commit()

# Add expense
col1, col2, col3, col4 = st.columns(4)
with col1:
    date = st.date_input("Date", datetime.date.today())
with col2:
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
with col3:
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
with col4:
    if st.button("Add Expense"):
        description = st.text_input("Description", key="desc_input")
        cursor.execute("INSERT INTO expenses VALUES (NULL, ?, ?, ?, ?)", (str(date), category, amount, description))
        conn.commit()
        st.success("Expense added!")

# Display expenses
df = pd.read_sql_query("SELECT * FROM expenses", conn)
if not df.empty:
    st.subheader("All Expenses")
    st.dataframe(df, use_container_width=True)
    
    # Visualization
    fig = px.pie(df.groupby('category')['amount'].sum(), values='amount', names=df.groupby('category').groups.keys(), title="Spending by Category")
    st.plotly_chart(fig, use_container_width=True)

conn.close()
