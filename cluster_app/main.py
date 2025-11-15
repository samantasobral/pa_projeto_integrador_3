import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

st.header('Acompanhamento do Comportamento de Compras dos Clientes')

df = pd.read_csv('data/cluster_customer.csv')

st.sidebar.header('Filtros')
clusters_options = df['cluster'].unique() 
selected_clusters = st.sidebar.multiselect('Clusters', clusters_options)

if not selected_clusters:
    selected_clusters = clusters_options

df = df[df['cluster'].isin(selected_clusters)]

#Quantidade de clientes por cluster
clientes_por_grupo = df['cluster'].value_counts().reset_index()
clientes_por_grupo.columns = ['Clusters', 'Quantidade de Clientes']
fig1 = px.bar(clientes_por_grupo, x ='Clusters', y ='Quantidade de Clientes', title = 'Quantidade de Clientes por Grupo')

#Média de Faturamento por Cluster
faturamento_por_grupo = df.groupby('cluster')['sales'].mean().reset_index()
faturamento_por_grupo.columns = ['Clusters', 'Faturamento Médio']
fig2 = px.bar(faturamento_por_grupo, x ='Clusters', y ='Faturamento Médio', title = 'Faturamento Médio por Grupo')

#Idade Média por Grupo
idade_por_grupo = df.groupby('cluster')['age'].mean().reset_index()
idade_por_grupo.columns = ['Clusters', 'Idade Média']
fig3 = px.bar(idade_por_grupo, x ='Clusters', y ='Idade Média', title = 'Idade Média por Grupo')

#Renda Média por Grupo
renda_por_grupo = df.groupby('cluster')['hh_income'].mean().reset_index()
renda_por_grupo.columns = ['Clusters', 'Renda Média']
fig4 = px.bar(renda_por_grupo, x ='Clusters', y ='Renda Média', title = 'Renda Média por Grupo')

#Quantidade de categorias por Grupo
cat_por_grupo = df.groupby('cluster')['unique_categories_bought'].mean().reset_index()
cat_por_grupo.columns = ['Clusters', 'Média das Categorias Únicas']
fig5 = px.bar(cat_por_grupo, x ='Clusters', y ='Média das Categorias Únicas', title = 'Média das Categorias Únicas por Grupo')

#Quantidade de tipo de pagamentos por Grupo
pag_por_grupo = df.groupby('cluster')['unique_payments_used'].mean().reset_index()
pag_por_grupo.columns = ['Clusters', 'Média de Tipos de Pagamento Usados']
fig6 = px.bar(pag_por_grupo, x ='Clusters', y ='Média de Tipos de Pagamento Usados', title = 'Média de Tipos de Pagamento Usados por Grupo')

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)
    st.plotly_chart(fig6, use_container_width=True)

color_pallete = px.colors.qualitative.Set3

fig = px.scatter(
    df,
    x = 'embedding_x',
    y ='embedding_y',
    color = 'cluster',
    size = 'sales',
    color_continuous_scale='Viridis',
    title = 'Análise dos Clusters'
)

fig.update_layout(height=800, width=1000)

st.plotly_chart(fig, use_container_width=True)