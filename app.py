import streamlit as st
import pandas as pd 
def main():
    edades=["18 a 24 años"]
    ages=["18 to 24"]
    st.title("Predictor de diabetes")
    with st.form(key="form1"):
        firstname=st.selectbox("Selecciona tu rango de edad",edades,kwargs=ages)
        lastname=st.text_input("Lastname")
        dubidubiduba=st.date_input("Dubidubidubiwa")

        submit_button=st.form_submit_button()
if __name__ == "__main__":
    main()
