import streamlit as st
import pandas as pd


@st.cache
def load_data():
    df = pd.read_csv("data.csv") # csv
    #df = pd.read_excel("data.excel") #excel
    return df



header = st.beta_container()
dataset = st.beta_container()
medidas = st.beta_container()
painel1 = st.beta_container()
painel2 = st.beta_container()
painel3 = st.beta_container()
painel4 = st.beta_container()
painel5 = st.beta_container()
resultado = st.beta_container()
with header:
    st.title('Bem Vindo ao Análise dos fundos imobiliários')
    st.text('Projeto em Construção...')

with dataset:
    st.header('Preview dos dados')
    df = load_data()
    st.dataframe(df.sample(8))

# with medidas:
#     st.header('Dados Escolhidos')
#     st.text('<- Escolha as medidas ao lado')

with painel1:
    #---------
    painel1.header("Filtre por um Código específico!")
    
    cod_escolhido = painel1.selectbox('Códigos para análise', options=df['cod'].unique().tolist())
    # t1 = st.sidebar.text_input("Component 1 name")
    # s1 = st.sidebar.slider("Component 1 value")
    #---------
    # st.sidebar.markdown("---")
    # #---------
    # st.sidebar.subheader("Component 2")
    # # t2 = st.sidebar.text_input("Component 2 name")
    # s2 = st.sidebar.slider("Component 2")
    #---------
    st.dataframe(df.loc[df['cod']==cod_escolhido])

with painel2:
    painel2.header('Filtre por Vários Códigos!')
    # , default=['ABCP11'] 
    cods_escolhidos = painel2.multiselect("beta_Columns", df['cod'].unique().tolist(), default=['ABCP11'])
    #print(cods_escolhidos)
    painel2.dataframe(df.loc[df['cod'].isin(cods_escolhidos)])
    #painel2.dataframe(df.loc[df['cod']==cod_escolhido])

with painel3:
    painel3.header('Múltiplos Filtros de coluna Dividendo(%) e Cota(R$)')
    painel3.text("Filtros")

    esq,direita = painel3.beta_columns(2)
    dividendo = esq.slider('Valor do Dividendo ATÉ %', min_value =0.0, max_value = df['dy_valor_em_perc'].max()-25, step =0.05)
    cota = direita.slider('Valor da Cota ATÉ R$', min_value =0.0, max_value = df['cota'].median()+90, step =0.20)
    painel3.text("Códigos Filtrados")
    if cota<=5.0:
        painel3.dataframe(df[(df['dy_valor_em_perc']<=dividendo)])  
    else:
        painel3.dataframe(df[(df['dy_valor_em_perc']<=dividendo) & (df['cota']<=cota)])