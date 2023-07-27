import streamlit as st
import pandas as pd 
def main():
    edades=["18 a 24 años","25 a 29 años"]
    ages=["18 to 24","25 to 29"]
    st.title("Predictor de diabetes")
    with st.form(key="form1"):
        edad=st.selectbox("Selecciona tu rango de edad",edades,kwargs=ages)
        submit_button=st.form_submit_button()
    if submit_button:
        st.write("Tu rango de edad seleccionado es:", edad)
if __name__ == "__main__":
    main()
