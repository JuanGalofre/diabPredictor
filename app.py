from flask import Flask, render_template , redirect
from flask_wtf import FlaskForm
from wtforms import SelectField , RadioField , BooleanField, FloatField , SubmitField
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model

app = Flask(__name__)
app.config["SECRET_KEY"]='17a2042599b56ab3c172d9bd'

def predict_diabetes(form_data):
    # Load the trained model
    model = load_model('./diabetes_model.h5')

    mapping = {
        'Age': {'18 to 24': 1, '25 to 29': 2, '30 to 34': 3.0, '35 to 39': 4, '40 to 44': 5, '45 to 49': 6, '50 to 54': 7, '55 to 59': 8, '60 to 64': 9, '65 to 69': 10, '70 to 74': 11, '75 to 79': 12, '80 or more': 13},
        'Education': {'Never attended school only kindergarten': 1, 'Elementary School': 2, 'High School (Not Graduated)': 3, 'High School (Graduated)': 4, 'College or Technical School (Not Graduated)': 5, 'College Graduate or More': 6},
        'Income': {'Less than 10K': 1, '10K to 16K': 2, '17K to 22K': 3, '23K to 28K': 4, '29K to 35K': 5, '36K to 48K': 6, '49K to 61K': 7, '62K to 75K': 8},
        'Sex': {'Female': 0, 'Male': 1},
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

edades=[('18 to 24', '18 a 24 años'), ('25 to 29', '25 a 29 años'), ('30 to 34', '30 a 34 años'), ('35 to 39', '35 a 39 años'), ('40 to 44', '40 a 44 años'), ('45 to 49', '45 a 49 años'), ('50 to 54', '50 a 54 años'), ('55 to 59', '55 a 59 años'), ('60 to 64', '60 a 64 años'), ('65 to 69', '65 a 69 años'), ('70 to 74', '70 a 74 años'), ('75 to 79', '75 a 79 años'), ('80 or more', '80 años o más')]
nivelesEducativos=[('Never attended school only kindergarten', 'Preescolar'), ('Elementary School', 'Escuela primaria'), ('High School (Not Graduated)', 'Escuela secundaria (no graduado)'), ('High School (Graduated)', 'Escuela secundaria (graduado)'), ('College or Technical School (Not Graduated)', 'Universidad o escuela técnica (no graduado)'), ('College Graduate or More', 'Graduado universitario o más')]
rangoIngresos=[('Less than 10K', 'Menos de $10,000'), ('10K to 16K', '$10,000 a $16,000'), ('17K to 22K', '$17,000 a $22,000'), ('23K to 28K', '$23,000 a $28,000'), ('29K to 35K', '$29,000 a $35,000'), ('36K to 48K', '$36,000 a $48,000'), ('49K to 61K', '$49,000 a $61,000'), ('62K to 75K', '$62,000 a $75,000')]
sexos=[("Female","Mujer"),("Male","Hombre")]
class RegisterForm(FlaskForm):
    edad=SelectField("Selecciona tu grupo de edad:",choices=edades,render_kw={"style":"display:block"})
    nivelEducativo=SelectField("¿Cuál es tu nivel educativo?",choices=nivelesEducativos,render_kw={"style":"display:block"})
    ingresos=SelectField("¿Cuál es tu rango de ingreso anual? USD",choices=rangoIngresos,render_kw={"style":"display:block"})
    genero=RadioField("Sexo",choices=sexos,render_kw={"style":"display:inline"})
    bmi=FloatField(" Ingresa tu índice de masa corporal (BMI).",render_kw={"style":"display:block"})
    coberturaMedica=BooleanField("¿Tienes cobertura médica?",render_kw={"style":"display:block"})
    costoCobertura=BooleanField("¿Tuviste alguna vez problemas para obtener atención médica debido al costo?",render_kw={"style":"display:block"})
    colesterolCheck=BooleanField("¿Te has realizado un chequeo de colesterol en el último año?",render_kw={"style":"display:block"})
    fumador=BooleanField("¿Eres fumador?",render_kw={"style":"display:block"})
    acv=BooleanField("¿Has tenido un accidente cerebrovascular?",render_kw={"style":"display:block"})
    actividadFisica=BooleanField("¿Has hecho ejercicio fisico en los ultimos 30 dias ?",render_kw={"style":"display:block"})
    frutas=BooleanField("¿Consumes frutas regularmente? (1 taza diaria)",render_kw={"style":"display:block"}) 
    verduras=BooleanField("¿Consumes verduras regularmente? (1 taza diaria)",render_kw={"style":"display:block"})
    alcohol=BooleanField("¿Tienes un consumo excesivo de alcohol? (más de 7 copas a la semana)",render_kw={"style":"display:block"})
    tension=BooleanField("¿Tienes presión arterial alta?",render_kw={"style":"display:block"})
    colesterol=BooleanField("¿Tienes colesterol alto?",render_kw={"style":"display:block"})
    enfermedadesCardiacas=BooleanField("¿Has tenido alguna vez enfermedades cardíacas o ataques al corazón?",render_kw={"style":"display:block"})
    submit=SubmitField("Evaluar mi condición de salud ")

@app.route('/answer')
def answer():
    return render_template("answer.html")

@app.route('/',methods=['GET', 'POST'])
def main_page():
    form=RegisterForm()
    if form.validate_on_submit():
        form_data={
        'Age': [form.edad.data],
        'Education': [form.nivelEducativo.data],
        'Income': [form.ingresos.data],
        'Sex': [form.genero.data],
        'NoDocbcCost': [form.costoCobertura.data],
        'AnyHealthcare': [form.coberturaMedica.data],
        'CholCheck': [form.colesterolCheck.data],
        'Smoker': [form.fumador.data],
        'Stroke': [form.acv.data],
        'PhysActivity': [form.actividadFisica.data],
        'Fruits': [form.frutas.data],
        'Veggies': [form.verduras.data],
        'HvyAlcoholConsump': [form.alcohol.data],
        'HighBP': [form.tension.data],
        'HighChol': [form.colesterol.data],
        'BMI': [form.bmi.data],
        'HeartDiseaseorAttack': [form.enfermedadesCardiacas.data]}
        result, state = predict_diabetes(form_data)
        print(result)
        print(f'State: {state}')
        results=[result,state]
        return render_template("answer.html",data=results)

    return render_template("home.html",form=form)
