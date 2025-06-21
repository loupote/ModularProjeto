from gera_relat_utils import *
from gera_comp_utils import *


def gerarRelatorioFinanceiro(periodo, console=False):
    data_inicio = periodo.get("data_inicio")
    data_fim = periodo.get("data_final")

    # Erro 400: se as datas forem incoerentes
    if data_inicio > data_fim:
        return {"Status": 400, "Content": "Período inválido."}
    

    lancamentos_periodo = [
        l for l in lancamentos
        if validarLancamento(l) and data_inicio <= l["data"] < data_fim
    ]

    # Erro 404: se nao tiver lancamento neste periodo
    if not lancamentos_periodo:
        return {"Status": 404, "Content": "Nenhum lançamento encontrado"}

    saldo_inicial = calcularSaldoAntes(data_inicio)
    receitas_por_cat, soma_receitas_periodo = agruparPorCategoria(lancamentos_periodo, "receita")
    despesas_por_cat, soma_despesas_periodo = agruparPorCategoria(lancamentos_periodo, "despesa")
    saldo_final = saldo_inicial + soma_receitas_periodo - soma_despesas_periodo
    variacao = saldo_final - saldo_inicial

    relatorio = {
        "periodo": {
            "inicio": data_inicio.strftime("%Y-%m-%d"),
            "fim": data_fim.strftime("%Y-%m-%d")},
        "saldoInicial": round(saldo_inicial, 2),
        "receitas": {"total": round(soma_receitas_periodo, 2), **receitas_por_cat},
        "despesas": {"total": round(soma_despesas_periodo, 2), **despesas_por_cat},
        "saldoFinal": round(saldo_final, 2),
        "variacao": round(variacao, 2)
    }


    # Imprime o relatório no console
    if console == True:
        print("\nRELATÓRIO FINANCEIRO:")
        pprint(relatorio, sort_dicts=False)
        gerarGraficoPizzaDespesas(relatorio)

    return {"Status": 200, "Content": relatorio}






def gerarComparativo(ano1, ano2, console = False):
    periodo_ano1 = {
        "data_inicio": datetime(ano1, 1, 1),
        "data_final": datetime(ano1+1, 1, 1)
    }
    periodo_ano2 = {
        "data_inicio": datetime(ano2, 1, 1),
        "data_final": datetime(ano2+1, 1, 1)
    }
    res1 = gerarRelatorioFinanceiro(periodo_ano1)
    res2 = gerarRelatorioFinanceiro(periodo_ano2)

    if (res1["Status"] == 400) or (res2["Status"] == 400):
        return {"Status": 400, "Content": "Período inválido."}
    if (res1["Status"] == 404) or (res2["Status"] == 404):
        return {"Status": 404, "Content": "Nenhum lançamento encontrado"}
    
    relatorioano1 = res1["Content"]
    relatorioano2 = res2["Content"]

    diferenca_receitas = relatorioano2["receitas"]["total"] - relatorioano1["receitas"]["total"]
    diferenca_despesas = relatorioano2["despesas"]["total"] - relatorioano1["despesas"]["total"]
    diferenca_saldoFinal = relatorioano2["saldoFinal"] - relatorioano1["saldoFinal"]

    gastos_por_categoria, cat_mais_gastos = maiorCategoria(relatorioano1, relatorioano2)

    resumo = (
    f"Em {ano2}, as receitas variaram em {round(diferenca_receitas, 2)}, "
    f"despesas em {round(diferenca_despesas, 2)} e o saldo final mudou em {round(diferenca_saldoFinal, 2)}.\n"
    f"A categoria com a maior aumentaçao de gastos vem da categoria '{cat_mais_gastos['categoria']}': {cat_mais_gastos['valorAno1']} durante o ano {ano1} contra {cat_mais_gastos['valorAno2']} em {ano2}"
    f"(+{cat_mais_gastos['diferenca']}).\n"
    "As categorias onde os gastos aumentaram são:\n"
    )
    
    for item in gastos_por_categoria:
        if item['diferenca'] > 0:
            resumo += f" - {item['categoria']}: +{item['diferenca']}\n"
    
    resumo += f"As categorias onde os gastos baixaram são:\n"
    for item in gastos_por_categoria:
        if item['diferenca'] < 0:
            resumo += f" - {item['categoria']}: {item['diferenca']}\n"


    comparativo = {
        "ano1": { "receitas": relatorioano1["receitas"],  "despesas": relatorioano1["despesas"], "saldoFinal": relatorioano1["saldoFinal"]},
        "ano2": { "receitas": relatorioano2["receitas"],  "despesas": relatorioano2["despesas"], "saldoFinal": relatorioano2["saldoFinal"]},
        "diferencas": { "receitas": diferenca_receitas, "despesas": diferenca_despesas, "saldoFinal": diferenca_saldoFinal},
        ## categoriaComMaiorDiferenca: [  { categoria: string, valorPeriodo1: int, valorPeriodo2: int, diferenca: int}],
        "resumo": resumo,
    
    }

    # Imprime o relatório no console
    if console == True:
        print("\nCOMPARATIVO FINANCEIRO:")
        pprint(comparativo, sort_dicts=False)

    return { "Success": 200, "Content": comparativo}

