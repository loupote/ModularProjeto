def categoria_maior_dif_despesa(relatorioano1, relatorioano2):
    categorias = set(relatorioano1["despesas"].keys()).union(set(relatorioano2["despesas"].keys()))
    categorias.discard("total")

    cat_dif = []
    max_dif = 0

    for cat in categorias:
        valor1 = relatorioano1["despesas"].get(cat, 0)
        valor2 = relatorioano2["despesas"].get(cat, 0)
        dif = valor2 - valor1

        cat_dif.append({
                "categoria": cat,
                "valorAno1": round(valor1, 2),
                "valorAno2": round(valor2, 2),
                "diferenca": round(valor2 - valor1, 2),
            })

        if dif > max_dif:
            max_dif = dif
            cat_maior_dif = {
                "categoria": cat,
                "valorAno1": round(valor1, 2),
                "valorAno2": round(valor2, 2),
                "diferenca": round(valor2 - valor1, 2),
            }

    return cat_dif, cat_maior_dif
