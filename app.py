import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados

st.header("Dashboard de Análise de Veículos")

if st.button("Criar Histograma"):
    st.write("Criando um histograma para a coluna 'odometer'")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.button("Criar Gráfico de Dispersão"):
    st.write("Criando gráfico de dispersão entre odometer e price")
    fig = px.scatter(car_data, x="odometer", y="price", color="model_year")
    st.plotly_chart(fig, use_container_width=True)

