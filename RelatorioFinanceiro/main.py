from main_func import *

if __name__ == "__main__":
    periodo = {
        "data_inicio": datetime(2020, 1, 1),
        "data_final": datetime(2023, 1, 1)
    }

    gerarRelatorioFinanceiro(periodo, True)

    gerarComparativo(2022, 2024, True)