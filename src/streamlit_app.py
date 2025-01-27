

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from pickle import load

# Cargar el modelo previamente entrenado
@st.cache_resource
def cargar_modelo():
    return load(open("../models/modelo_Rlineal.sav", "rb"))

modelo = cargar_modelo()

# Configuración de la app
st.title("Calculadora de Prima de Seguro Médico")
st.write("Ingrese los datos del paciente para calcular el costo estimado de su seguro médico.")

# Inputs del usuario
edad = st.slider("Edad", min_value=18, max_value=100, value=30, step=1)
imc = st.number_input("Índice de Masa Corporal (IMC)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
hijos = st.slider("Número de hijos", min_value=0, max_value=10, value=0, step=1)
fumador = st.selectbox("¿Es fumador?", options=["Sí", "No"])

# Conversión de variables categóricas
fumador_fact = 1 if fumador == "Sí" else 0


# Preparar los datos para el modelo
entrada_usuario = np.array([[edad, imc, hijos, fumador_fact]])

# Realizar la predicción
if st.button("Calcular Prima"):
    prima = modelo.predict(entrada_usuario)
    st.success(f"El costo estimado del seguro es: ${prima[0]:,.2f}")