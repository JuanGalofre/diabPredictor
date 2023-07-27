import streamlit as st
import pandas as pd 
def main():
    edades=edades=[('18 to 24', '18 a 24 años'), ('25 to 29', '25 a 29 años'), ('30 to 34', '30 a 34 años'), ('35 to 39', '35 a 39 años'), ('40 to 44', '40 a 44 años'), ('45 to 49', '45 a 49 años'), ('50 to 54', '50 a 54 años'), ('55 to 59', '55 a 59 años'), ('60 to 64', '60 a 64 años'), ('65 to 69', '65 a 69 años'), ('70 to 74', '70 a 74 años'), ('75 to 79', '75 a 79 años'), ('80 or more', '80 años o más')]
    st.title("Predictor de diabetes")
    with st.form(key="form1"):
        firstname=st.selectbox("Selecciona tu rango de edad",edades)
        lastname=st.text_input("Lastname")
        dubidubiduba=st.date_input("Dubidubidubiwa")

        submit_button=st.form_submit_button()
if __name__ == "__main__":
    main()
