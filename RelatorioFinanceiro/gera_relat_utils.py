from datetime import datetime
from pprint import pprint #Pata um pretty print no console

import matplotlib.pyplot as plt #Para a geracao de diagrama circular

import random


categorias = ['Moradia', 'Alimentação', 'Transporte', 'Saúde', 'Educação', 'Lazer', 'Guardar', 'Salario', 'Outros']
tipos = ['receita', 'despesa']

lancamentos = []

for _ in range(30):
    ano = random.randint(2020, 2024)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)  # para evitar erros com dias inválidos
    tipo = random.choice(tipos)
    
    # Para receita, valores maiores; para despesa, valores menores (apenas sugestão)
    if tipo == 'receita':
        valor = round(random.uniform(1000, 5000), 2)
    else:
        valor = round(random.uniform(10, 500), 2)
    
    categoria = random.choice(categorias)
    descricao = f"Lançamento {tipo} - {categoria}"
    
    lancamento = {
        "descricao": descricao,
        "valor": valor,
        "data": datetime(ano, mes, dia),
        "tipo": tipo,
        "categoria": categoria
    }
    
    lancamentos.append(lancamento)



def calcularSaldoAntes(data_inicio):
    saldo = 0.0
    for l in lancamentos:
        if validarLancamento(l) and l["data"] < data_inicio:
            if l["tipo"] == "receita":
                saldo += l["valor"]
            elif l["tipo"] == "despesa":
                saldo -= l["valor"]
    return saldo


def validarLancamento(lancamento):
    return (
        lancamento.get("tipo") in tipos and
        lancamento.get("categoria") in categorias and
        isinstance(lancamento.get("valor"), (float, int)) and
        isinstance(lancamento.get("data"), datetime)
    )


def agruparPorCategoria(lancs, tipo):
    categorias = {}
    total = 0.0
    for l in lancs:
        if l["tipo"] == tipo:
            cat = l["categoria"]
            categorias[cat] = categorias.get(cat, 0.0) + l["valor"]
            total += l["valor"]
    return categorias, total


def gerarGraficoPizzaDespesas(relatorio):
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
