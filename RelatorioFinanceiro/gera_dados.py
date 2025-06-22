from numpy import random
from datetime import datetime

categorias = ['Moradia', 'Alimentação', 'Transporte', 'Saúde', 'Educação', 'Lazer', 'Guardar', 'Salario', 'Outros']
tipos = ['receita', 'despesa']

def gerar_lancamentos(quantidade=30, anos=(2020, 2024)):
    """
    Generates a list of random financial records (lancamentos).

    Parameters
    ----------
    quantidade : int
        Number of records to generate.
    anos : tuple of int
        Range of years to use for random dates (inclusive).

    Returns
    -------
    list of dict
        List containing randomly generated financial records.
    """

    lancamentos = []

    for _ in range(quantidade):
        ano = random.randint(anos[0], anos[1])
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)  # avoid invalid dates
        tipo = random.choice(tipos)
        valor = round(random.uniform(1000, 5000), 2) if tipo == 'receita' else round(random.uniform(10, 500), 2)
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

    return lancamentos