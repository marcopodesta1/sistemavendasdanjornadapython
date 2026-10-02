import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")
vendedores = ["Ana", "Bruno", "Carla"]
produtos = ["Notebook", "Celular", "Fone"]


st.write("# Sistemas de Vendas")

# seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", vendedores)
produto =  st.sidebar.selectbox("Produto", produtos)
quantidade = st.sidebar.number_input("Quantidade",min_value=0, step=1 )
valor = st.sidebar.number_input("Valor", min_value=0)
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# lógica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # 122 linhas
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada!")

# seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# seção Dashborard
st.write("## Dashboard")

# Card/Métrica -> Faturamento tatoal
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento:,.2f}".replace(",", "X")
                                                       .replace(".", ",")
                                                       .replace("X", "."))

# Gráfico de Barra
grafico1 = px.bar(tabela_vendas,
                  x="vendedor",
                  y="valor",
                  color="produto")
st.plotly_chart(grafico1)

# gráfico de Pizza
grafico2 = px.pie(tabela_vendas,
                  names="produto",
                  values="valor",
                  hole = 0.5)
st.plotly_chart(grafico2)
