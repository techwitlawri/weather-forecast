import streamlit as st


st.title("Weather forecast for the next days")
place= st.text_input("place")
forecast_days= st.slider(min_value= 1, max_value=5, help=
                         'Select days')
