import streamlit as st
import numpy as np
import pandas as pd
import math
import requests
from dataclasses import dataclass

# Configurações da página
st.set_page_config(page_title="Construção de Algoritmos e Programação", layout="centered")

# Título principal
st.title("Construção de Algoritmos e Programação")
st.write("Escolha um tema na barra lateral para ver explicações simples e exemplos práticos.")


# ==================================================
# MENU LATERAL
# ==================================================
menu = st.sidebar.radio(
    "Escolha um tema:",
    (
        "Decisão e Repetição",
        "Vetores e Matrizes",
        "Funções e Bibliotecas",
        "Registros",
        "Arquivos em Disco",
        "Recursividade",
        "Complexidade de Tempo (Big O)",
        "Consulta ao Dólar (API)"
    )
)


# ==================================================
# TEMA 1 — DECISÃO E REPETIÇÃO
# ==================================================
if menu == "Decisão e Repetição":
    st.header("Tema 1: Decisão e Repetição")

    entrada = st.text_input("Digite números separados por vírgula:", "1,2,3,4,10")

    if st.button("Processar"):
        try:
            nums = [int(x.strip()) for x in entrada.split(",")]
            pares = [n for n in nums if n % 2 == 0]
            soma = sum(nums)

            st.write("📌 **Números digitados:**", nums)
            st.write("🔢 **Números pares:**", pares)
            st.write("➕ **Soma total:**", soma)

        except:
            st.error("Erro: verifique os números digitados.")

    with st.expander("📄 Documentação do Tema 1"):
        st.markdown("""
        **Objetivo:** Mostrar o uso básico de *decisão* e *repetição*.  
        - `if n % 2 == 0:` identifica pares  
        - `for` percorre os valores
        """)


# ==================================================
# TEMA 2 — VETORES E MATRIZES
# ==================================================
elif menu == "Vetores e Matrizes":
    st.header("Tema 2: Vetores e Matrizes")

    n = st.slider("Tamanho do vetor e matriz:", 1, 10, 5)

    if st.button("Gerar"):
        vetor = np.arange(1, n+1)
        matriz = np.arange(1, n*n + 1).reshape(n, n)

        st.write("📌 **Vetor:**", vetor.tolist())
        st.write("📊 **Matriz:**")
        st.dataframe(pd.DataFrame(matriz))
        st.write("➕ Soma do vetor:", int(vetor.sum()))
        st.write("📈 Soma das colunas:", matriz.sum(axis=0).tolist())

    with st.expander("📄 Documentação"):
        st.markdown("""
        **Vetores:** listas de 1 dimensão  
        **Matrizes:** tabelas com linhas e colunas  
        """)


# ==================================================
# TEMA 3 — FUNÇÕES E BIBLIOTECAS
# ==================================================
elif menu == "Funções e Bibliotecas":
    st.header("Tema 3: Funções e Bibliotecas")

    celsius = st.number_input("Temperatura em Celsius:", value=25.0)

    def c_to_f(c):
        return (c * 9/5) + 32

    def f_to_c(f):
        return (f - 32) * 5/9

    if st.button("Converter para Fahrenheit"):
        st.success(f"{celsius} °C = {c_to_f(celsius):.2f} °F")
        st.write("Raiz quadrada do valor absoluto (usando `math`):")
        st.write(math.sqrt(abs(celsius)))

    with st.expander("📄 Documentação"):
        st.markdown("""
        Funções permitem reaproveitar código.  
        Bibliotecas trazem funções prontas (como `math`).
        """)


# ==================================================
# TEMA 4 — REGISTROS (DATACLASS)
# ==================================================
elif menu == "Registros":
    st.header("Tema 4: Registros (Dataclass)")

    @dataclass
    class Estudante:
        nome: str
        idade: int
        curso: str

    nome = st.text_input("Nome:", "Ana")
    idade = st.number_input("Idade:", 0, 120, 18)
    curso = st.text_input("Curso:", "Sistemas")

    if st.button("Criar Registro"):
        aluno = Estudante(nome, int(idade), curso)
        st.success("Registro criado:")
        st.write(aluno)

    with st.expander("📄 Documentação"):
        st.markdown("""
        **Dataclass** é usada para criar registros de forma simples.
        """)


# ==================================================
# TEMA 5 — ARQUIVOS EM DISCO
# ==================================================
elif menu == "Arquivos em Disco":
    st.header("Tema 5: Arquivos em Disco")

    texto = st.text_area("Conteúdo do arquivo:", "Exemplo de texto.")
    nome_arq = st.text_input("Nome do arquivo:", "arquivo.txt")

    if st.button("Salvar"):
        try:
            with open(nome_arq, "w", encoding="utf-8") as f:
                f.write(texto)
            st.success("Arquivo salvo!")
        except Exception as e:
            st.error(str(e))

    if st.button("Ler"):
        try:
            with open(nome_arq, "r", encoding="utf-8") as f:
                st.code(f.read())
        except Exception as e:
            st.error(str(e))

    with st.expander("📄 Documentação"):
        st.markdown("""
        Exemplos de leitura e escrita usando `open()`.
        """)


# ==================================================
# TEMA 6 — RECURSIVIDADE
# ==================================================
elif menu == "Recursividade":
    st.header("Tema 6: Recursividade")

    def fatorial_rec(n):
        if n <= 1:
            return 1
        return n * fatorial_rec(n - 1)

    def fatorial_iter(n):
        res = 1
        for i in range(2, n+1):
            res *= i
        return res

    n = st.number_input("Digite n:", 0, 20, 5)

    if st.button("Calcular"):
        st.write("🔁 Fatorial Recursivo:", fatorial_rec(n))
        st.write("➡️ Fatorial Iterativo:", fatorial_iter(n))

    with st.expander("📄 Documentação"):
        st.markdown("""
        Recursão = função chamando ela mesma.  
        """)


# ==================================================
# TEMA 7 — COMPLEXIDADE (BIG O)
# ==================================================
elif menu == "Complexidade de Tempo (Big O)":
    st.header("Tema 7: Complexidade de Tempo (Big O)")

    st.markdown("""
    - **O(1)** → tempo constante  
    - **O(n)** → cresce linearmente  
    - **O(n²)** → cresce rapidamente  
    """)

    n = st.slider("Valor de n:", 1, 2000, 500)

    def o1(n): return 1
    def on(n): return n
    def on2(n): return n*n

    if st.button("Testar"):
        st.write("O(1):", o1(n))
        st.write("O(n):", on(n))

        if n <= 200:
            st.write("O(n²):", on2(n))
        else:
            st.warning("n muito grande! Usando n=200.")
            st.write("O(n²):", on2(200))

    with st.expander("📄 Documentação"):
        st.markdown("""
        Big O mede como o tempo cresce conforme a entrada aumenta.
        """)


# ==================================================
# TEMA 8 — API DO DÓLAR
# ==================================================
elif menu == "Consulta ao Dólar (API)":
    st.header("Tema 8: Consulta ao Dólar (API)")

    data = st.text_input("Digite a data (MMDDYYYY):", "01012024")

    def consultar(data):
        try:
            url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@data)?@data='{data}'&$format=json"
            r = requests.get(url).json()
            return r["value"][0]["cotacaoVenda"]
        except:
            return None

    if st.button("Consultar"):
        resp = consultar(data)
        if resp:
            st.success(f"Cotação no dia {data}: R$ {resp}")
        else:
            st.error("Erro ao consultar (data inválida, feriado ou fim de semana).")

    with st.expander("📄 Documentação"):
        st.markdown("""
        Exemplo de acesso a API oficial do Banco Central usando `requests`.
        """)


# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("Atividade Acadêmica — Construção de Algoritmos e Programação")
st.sidebar.write("Thiago Francisco – Sistemas de Informação – UNASP")
