import streamlit as st
from contrato import Vendas

from pydantic import ValidationError

def main():

    st.title("Sistema de CRM e Vendas da ZapFlow")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Campo para selecionar a data em que a venda foi realizada.")
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada")
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda realizada.")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos vendidos.")
    produto = st.selectbox("Campo de seleção para escolher o produto vendido.", ["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])
    
    if st.button("Salvar e exibir dados"):
        try:
            venda = Vendas(
                email=email,
                data=data,
                hora=hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            st.write("Informações: ")
            st.write(venda)
        except ValidationError as e:
            st.error(f"Erro encontrado: {e}")

if __name__ == '__main__':
    main()