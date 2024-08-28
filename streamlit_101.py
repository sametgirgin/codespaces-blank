import streamlit as st

st.title("Can you see my Portfolio!!!")

# Import matplotlib.pyplot with alias plt
import pandas as pd
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/kzavrazhnyi/pythonthefirst/master/avocados_2016.csv')

avocados_2016 = load_data()

st.header("1-Inspect the dataset")
st.write("'st.data_editor' allow us to display and edit the dataset")

st.data_editor(avocados_2016)

st.bar_chart(avocados_2016.isna().sum())
