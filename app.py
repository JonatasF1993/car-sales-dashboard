import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho do aplicativo
st.header('Dashboard de Vendas de Carros Usados 🇺🇸🚘')

# Lendo os dados do arquivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Caixa de seleção para criar histograma
build_hist = st.checkbox('Criar histograma')

if build_hist:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros...')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para criar gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão: preço x quilometragem...')
    fig = px.scatter(car_data, x="odometer", y="price", color="type",
                     title="Preço vs Quilometragem dos veículos")
    st.plotly_chart(fig, use_container_width=True)
