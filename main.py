import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value= 1, max_value=5, 
                 help= "Select the number of forecasted days")
option= st.selectbox("select date to view",
                      ("Temperature", "Sky")) 
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-10","2022-26-10","2022-27-10"]
    temperature= [10, 11, 15]   
#  connecting the temperature with the widget
    temperature= [days * i for i in temperature]
    return  dates,temperature

d, t = get_data(days)
# importing plotly, adding graphy
figure = px.line(x= d, y= t, labels={"x":"Date","y": "Temperature (C)"})
st.plotly_chart(figure)

 
