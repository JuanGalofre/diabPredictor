import streamlit as st
import pandas as pd 
def main():
    edades=["18 a 24 años","25 a 29 años","30 a 34 años",'35 a 39 años', '40 a 44 años','45 a 49 años','50 a 54 años','55 a 59 años','60 a 64 años','65 a 69 años','70 a 74 años','75 a 79 años','80 años o más']
    nivelesEducativos=['Preescolar', 'Escuela primaria', 'Escuela secundaria (no graduado)','Escuela secundaria (graduado)', 'Universidad o escuela técnica (no graduado)', 'Graduado universitario o más']
    rangoIngresos=['Menos de $10,000',  '$10,000 a $16,000',  '$17,000 a $22,000',  '$23,000 a $28,000',  '$29,000 a $35,000',  '$36,000 a $48,000', '$49,000 a $61,000', '$62,000 a $75,000']
    sexos=["Mujer","Hombre"]
    st.title("Predictor de diabetes")
    with st.form(key="form1"):
        edad=st.selectbox("Selecciona tu rango de edad",edades)
        nivelEducativo=st.selectbox("¿Cuál es tu nivel educativo?",nivelesEducativos)
        ingresos=st.selectbox("¿Cuál es tu rango de ingreso anual? en USD",rangoIngresos)
        sexo=st.selectbox("Indica tu sexo",sexos)
        submit_button=st.form_submit_button()
    if submit_button:
        st.write("Tu rango de edad seleccionado es:", edad)
if __name__ == "__main__":
    main()
