import streamlit as st
import pandas as pd 
def main():
    st.title("Predictor de diabetes")
    with st.form(key="form1"):
        firstname=st.text_input("Firstname")
        lastname=st.text_input("Lastname")
        dubidubiduba=st.date_input("Dubidubidubiwa")

        submit_button=st.form_submit_button()
if __name__ == "__main__":
    main()
