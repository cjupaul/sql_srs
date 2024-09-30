import streamlit as  st
import pandas as pd
import duckdb

st.write("""
         # SQL SRS
         Spaced Repetition System SQL practice
         """)

option = st.selectbox(
    "What would you like to review?"
    ("Joins","GroupBy","Windows Functions"),
    index=None,
    placeholder="Slect a theme..."
)

st.write("you selected:", option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="entre votre input")
    result = duckdb.query(sql_query).df()
    st.write(f"vous avez rentré la query suivante: + {sql_query}")
    st.dataframe(result)