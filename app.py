import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Dashboard da XXIII Semana de Tecnologia Fatec Mauá",
    page_icon="📊",
    layout="wide",    #deixa página formato largo
)

# --- Carregamento dos dados ---
df = pd.read_csv("https://raw.githubusercontent.com/profzappa/StecnologiaMaua/refs/heads/main/arquivoMacroCompleto49.csv")

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

# Filtro de ATIVIDADES


datas_disponiveis = sorted(df['Data_Atividade'].unique())
datas_selecionados = st.sidebar.multiselect("Selecione a data", datas_disponiveis, default=datas_disponiveis)

# --- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
##criou componente visual dos filtros, agora, aplicar os filtros, pegando tudo o que o usuário
##selecionou

df_filtrado = df[
    (df['Data_Atividade'].isin(datas_selecionados)) 
    
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Atividades")
st.markdown("Explore a quantidade de participantes da Semana de Tecnologia. Utilize os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas gerais")

if not df_filtrado.empty:
    
   total_registros = df_filtrado.shape[0]
#    tipo_mais_frequente = df_filtrado["type"].mode()[0]
   #total_atividades = df_filtrado['Código'].unique()
   activity_counts = df_filtrado['Código'].nunique()
else:
    total_registros = 0
    activity_counts=0

#col1 = st.columns(1)
col1,col2 = st.columns(2)

#st.metric("Total de participantes", f"{activity_counts:,}")
col1.metric("Total de Certificados", total_registros)
col2.metric("Quantidade de Atividades", activity_counts)

st.markdown("---")

# --- Análises Visuais com Plotly ---
st.subheader("Gráfico")  ##subtitulos

#col_graf1, col_graf2 = st.columns(2)   ##2 colunas, um do lado do outro
#col_graf1 = st.columns(1) 
#with col_graf1:
if not df_filtrado.empty:
        # Count the occurrences of each category
        #category_counts = df_filtrado['Categoria'].value_counts().reset_index()
        #category_counts.columns = ['Categoria', 'Count']
        shift_counts = df_filtrado['Turno'].value_counts().reset_index()
        shift_counts.columns = ['Turno', 'Count']
        #grafico_categoria= px.pie(
        #    category_counts,
        #    names='Categoria',
        #    values='Count',
        #    title='Distribuição por Categoria',
        #    labels={'Categoria': 'Categoria ', 'Count': 'qtde'}
        #)
        grafico_turno = px.bar(
            shift_counts,  
            x='Turno',
            y='Count',
            title='Distribuição de participantes por Turno',
            labels={'Turno': 'Turno', 'Count': 'participantes'},
            color='Turno'
        )
        grafico_turno.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_turno, use_container_width=True)

        #grafico_categoria.update_traces(textinfo='percent+label')
        #grafico_categoria.update_layout(title_x=0.1)
        #st.plotly_chart(grafico_categoria, use_container_width=True)

else:
        st.warning("Nenhum dado para exibir no gráfico de turnos.")


#with col_graf2:
#    if not df_filtrado.empty:
#        # Count the occurrences of each period
#        period_counts = df_filtrado['Período'].value_counts().reset_index()
#        period_counts.columns = ['Periodo', 'Count']

# Create the bar chart
#        grafico_periodo= px.bar(
#           period_counts,
#            x='Periodo',
#            y='Count',
#            title='Distribuição por Período',
#            labels={'Periodo': 'Periodo ', 'Count': 'qtde'}
#        )
#        grafico_periodo.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
#        st.plotly_chart(grafico_periodo, use_container_width=True)

        
#    else:
#        st.warning("Nenhum dado para exibir no gráfico de distribuição por períodos.")

#col_graf3, col_graf4 = st.columns(2)

#with col_graf3:
#    if not df_filtrado.empty:
#        course_counts = df_filtrado['Curso'].value_counts().reset_index()
#        course_counts.columns = ['Curso', 'Count']

#        grafico_cursos = px.bar(
#           course_counts,
#           x='Count',
#            y='Curso',
#            orientation='h',
#            title="Distribuição por Curso",
#            labels={'Count': 'qtde', 'Curso': 'Curso '}
            #labels={'Count': 'Qtde alunos', 'Curso': ''}
#        )
#        grafico_cursos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
#        st.plotly_chart(grafico_cursos, use_container_width=True)
#   else:
#       st.warning("Nenhum dado para exibir no gráfico de cursos.")

#with col_graf4:
#    if not df_filtrado.empty:
        # Count the occurrences of each semester
#        semester_counts = df_filtrado['Semestre'].value_counts().reset_index()
#        semester_counts.columns = ['Semestre', 'Count']
        # Create the bar chart
#        grafico_semestre= px.bar(
#            semester_counts,
#            x='Semestre',
#            y='Count',
#            title='Distribuição por Semestre',
#            labels={'Semestre': 'Semestre ', 'Count': 'qtde'}
#        )
#        grafico_semestre.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
#        st.plotly_chart(grafico_semestre, use_container_width=True)

        
#   else:
#       st.warning("Nenhum dado para exibir no gráfico de distribuição por semestres.")


# --- Tabela de Dados Detalhados ---
#st.subheader("Dados Detalhados")
#st.dataframe(df_filtrado)
