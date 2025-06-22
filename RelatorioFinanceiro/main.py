from Projeto.RelatorioFinanceiro.gera_utils import *
from gera_dados import *


if __name__ == "__main__":
    periodo = {
        "data_inicio": datetime(2020, 1, 1),
        "data_final": datetime(2023, 1, 1)
    }

    meus_lancamentos = gerar_lancamentos()

    gerar_relatorio_financeiro(meus_lancamentos, periodo, True)

    gerar_comparativo(meus_lancamentos, 2022, 2024, True)