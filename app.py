import streamlit as st
import pandas as pd 
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model

def predict_diabetes(form_data):
    # Load the trained model
    model = load_model('./diabetes_model.h5')

    mapping = {
        'Age': {"18 a 24 años":1,"25 a 29 años":2,"30 a 34 años":3,'35 a 39 años':4, '40 a 44 años':5,'45 a 49 años':6,'50 a 54 años':7,'55 a 59 años':8,'60 a 64 años':9,'65 a 69 años':10,'70 a 74 años':11,'75 a 79 años':12,'80 años o más':13},
        'Education': {'Preescolar':1, 'Escuela primaria':2, 'Escuela secundaria (no graduado)':3,'Escuela secundaria (graduado)':4, 'Universidad o escuela técnica (no graduado)':5, 'Graduado universitario o más':6},
        'Income': {'Menos de $10,000':1,  '$10,000 a $16,000':2,  '$17,000 a $22,000':3,  '$23,000 a $28,000':4,  '$29,000 a $35,000':5,  '$36,000 a $48,000':6, '$49,000 a $61,000':7, '$62,000 a $75,000':8},
        'Sex': {'Mujer': 0, 'Hombre': 1},
        'NoDocbcCost': {False: 0, True: 1},
        'AnyHealthcare': {False: 0, True: 1},
        'CholCheck': {False: 0, True: 1},
        'Smoker': {False: 0, True: 1},
        'Stroke': {False: 0, True: 1},
        'PhysActivity': {False: 0, True: 1},
        'Fruits': {False: 0, True: 1},
        'Veggies': {False: 0, True: 1},
        'HvyAlcoholConsump': {False: 0, True: 1},
        'HighBP': {False: 0, True: 1},
        'HighChol': {False: 0, True: 1},
        'BMI': {25.0: 0},
        'HeartDiseaseorAttack': {False: 0, True: 1}
    }

    # Convertir los datos del formulario en un DataFrame
    form_df = pd.DataFrame(form_data)

    # Codificar las características categóricas del formulario
    def map_values(column_name, value):
        return mapping[column_name][value] if value in mapping[column_name] else value

    form_encoded = form_df.apply(lambda column: column.apply(lambda x: map_values(column.name, x)))



    # Escalar las características del formulario usando el mismo scaler que se usó en el entrenamiento
    scaler = StandardScaler()
    form_scaled = scaler.fit_transform(form_encoded)

    # Realizar la predicción usando el modelo entrenado
    predictions = model.predict(form_scaled)

    # Table of probabilities
    probabilities = pd.DataFrame(predictions, columns=['No diabetes', 'Prediabetes', 'Diabetes'])

    # Get the state
    state = probabilities.idxmax(axis=1).values[0]
    return probabilities, state


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
        bmi=st.number_input("Ingresa porfavor tu Indice de masa corporal",value=00.0)
        coberturaMedica=st.checkbox("¿Tienes cobertura médica?")
        costoCobertura=st.checkbox("¿Tuviste alguna vez problemas para obtener atención médica debido al costo?")
        colesterolCheck=st.checkbox("¿Te has realizado un chequeo de colesterol en el último año?")
        fumador=st.checkbox("¿Eres fumador?")
        acv=st.checkbox("¿Has tenido un accidente cerebrovascular?")
        actividadFisica=st.checkbox("¿Has hecho ejercicio fisico en los ultimos 30 dias ?")
        frutas=st.checkbox("¿Consumes frutas regularmente? (1 taza diaria)") 
        verduras=st.checkbox("¿Consumes verduras regularmente? (1 taza diaria)")
        alcohol=st.checkbox("¿Tienes un consumo excesivo de alcohol? (más de 7 copas a la semana)")
        tension=st.checkbox("¿Tienes presión arterial alta?")
        colesterol=st.checkbox("¿Tienes colesterol alto?")
        enfermedadesCardiacas=st.checkbox("¿Has tenido alguna vez enfermedades cardíacas o ataques al corazón?")
        
        submit_button=st.form_submit_button()


    
    if submit_button:
        form_data={
        'Age': edad,
        'Education': nivelEducativo,
        'Income': ingresos,
        'Sex': sexo,
        'NoDocbcCost': costoCobertura,
        'AnyHealthcare': coberturaMedica,
        'CholCheck': colesterolCheck,
        'Smoker': fumador,
        'Stroke': acv,
        'PhysActivity': actividadFisica,
        'Fruits': frutas,
        'Veggies':verduras,
        'HvyAlcoholConsump':alcohol,
        'HighBP': tension,
        'HighChol': colesterol,
        'BMI': bmi,
        'HeartDiseaseorAttack': enfermedadesCardiacas}
        result, state = predict_diabetes(form_data)
        st.write(result)


if __name__ == "__main__":
    main()
