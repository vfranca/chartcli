# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click
from mtcli.csv_data import get_data
from mtcli import views as _view
from mtcli.pa import helpers as helper
from mtcli.pa.pa_bar import Bar
from mtcli.pa.pa_one_bar import OneBar
from mtcli.pa.pa_two_bars import TwoBars
from mtcli.conf import csv_path, digits as d


# Cria o comando bars
@click.command()
@click.argument("symbol")
@click.option("--view", "-v", help="Formato de exibição")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", type=int, default=40, help="Quantidade de barras")
@click.option("--date", "-d", default="", help="Data (para day trade)")
def bars(symbol, view, period, count, date):
    """Exibe uma lista de barras."""
    # Arquivo CSV das cotações
    csv_file = csv_path + symbol + period + ".csv"
    # Importa os dados CSV
    list_rates = get_data(csv_file)
    # Restringe a N últimas barras
    list_rates = list_rates[-count:]
    # Converte a lista para dicionário
    dict_rates = {}
    for i in range(len(list_rates)):
        dict_rates[list_rates[i][0]] = list_rates[i][1:]
    # Prepara a string de exibição no formato mínimo
    view_min = "%s %.{0}f %.{1}f %.{2}f".format(d, d, d)
    # Prepara a string de exibição no formato ranges
    view_ranges = "%s %.{0}f".format(d)
    # Prepara a string de exibição no formato fechamentos
    view_closes = "%.{0}f".format(d)
    # Prepara a string de exibição no formato variações percentuais
    view_percentuais = "%.2f%%"
    # Prepara a string de exibição no formato completo
    view_full = "%s %s %s %s %.{0}f %.{1}f %.{2}fM%.{3}f".format(d, d, d, d)
    # Exibe as barras no formato mínimo
    if view and view.lower() == "ch":
        for v in dict_rates.values():
            click.echo(
                view_min % ("asc".upper(), float(v[1]), float(v[2]), float(v[3]))
            )
        return 0
    # Exibe as barras no formato ranges
    if view and view.lower() == "r":
        for v in dict_rates.values():
            click.echo(view_ranges % ("asc".upper(), float(v[1]) - float(v[2])))
        return 0
    # Exibe as barras no formato completo
    for v in dict_rates.values():
        click.echo(
            view_full
            % (
                "asc".upper(),
                "cp".upper(),
                "verde90".upper(),
                "g200".upper(),
                float(v[1]),
                float(v[2]),
                float(v[3]),
                18.34,
            )
        )


if __name__ == "__main__":
    bars()
