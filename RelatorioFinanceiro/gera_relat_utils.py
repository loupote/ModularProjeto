from datetime import datetime
from pprint import pprint #Pata um pretty print no console

import matplotlib.pyplot as plt #Para a geracao de diagrama circular

from gera_dados import tipos, categorias



def calcular_saldo_antes(lancamentos, data_inicio):
    saldo = 0.0
    for l in lancamentos:
        if validar_lancamento(l) and l["data"] < data_inicio:
            if l["tipo"] == "receita":
                saldo += l["valor"]
            elif l["tipo"] == "despesa":
                saldo -= l["valor"]
    return saldo


def validar_lancamento(lancamento):
    return (
        lancamento.get("tipo") in tipos and
        lancamento.get("categoria") in categorias and
        isinstance(lancamento.get("valor"), (float, int)) and
        isinstance(lancamento.get("data"), datetime)
    )


def agrupar_por_categoria(lancs, tipo):
    categorias = {}
    total = 0.0
    for l in lancs:
        if l["tipo"] == tipo:
            cat = l["categoria"]
            categorias[cat] = categorias.get(cat, 0.0) + l["valor"]
            total += l["valor"]
    return categorias, total


def gerar_grafico_pizza_despesas(relatorio):
    despesas = relatorio["despesas"]
    categorias = [k for k in despesas if k != "total"]
    valores = [despesas[k] for k in categorias]

    if not categorias:
        print("Nenhuma despesa para exibir.")
        return

    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
    plt.title("Distribuição de Despesas por Categoria")
    plt.axis('equal')  # para deixar o círculo "perfeito"
    plt.tight_layout()
    plt.show()
