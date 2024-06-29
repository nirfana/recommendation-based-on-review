# Contents of app.py
import eda
import prediction
import streamlit as st

PAGES = {
    "Exploratory Data Analysis": eda,
    "Make Predictions": prediction
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()