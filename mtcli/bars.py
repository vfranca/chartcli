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
    # ASC 35.00 30.00 32.50
    view_min = "%s %.{0}f %.{1}f %.{2}f".format(d, d, d)
    # Prepara a string de exibição no formato ranges
    # ASC 5.00
    view_ranges = "%s %.{0}f".format(d)
    # Prepara a string de exibição no formato fechamentos
    # 32.50
    view_closes = "%.{0}f".format(d)
    # Prepara a string de exibição no formato variações percentuais
    # ASC 1.50%
    view_percentuais = "%s %.2f%%"
    # Prepara a string de exibição no formato completo
    # ASC CP VERDE75 G2.5 BOTTOM20 35.00 30.00 32.00M32.50 5.00 2.50%
    view_full = "%s %s %s%i %s %s %.{0}f %.{1}f %.{2}fM%.{3}f".format(d, d, d, d)
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
        # Define os preços de abertura, máxima, mínima e fechamento
        o, h, l, c = float(v[0]), float(v[1]), float(v[2]), float(v[3])
        # Calcula o range do corpo
        range_body = c - o
        # Define a tendência da barra
        trend_bar = "doji"
        if range_body > 0:
            trend_bar = "verde"
        if range_body < 0:
            trend_bar = "vermelho"
        # Calcula o range da barra
        range_bar = h - l
        # Calcula o percentual de corpo
        percentual_body = abs(range_body) / range_bar * 100
        # Verifica se é uma barra de rompimento
        breakout = ""
        if percentual_body >= 60:
            breakout = "BO"
        click.echo(
            view_full
            % (
                "asc".upper(),
                breakout.upper(),
                trend_bar.upper(),
                percentual_body,
                "g200".upper(),
                "BOTTOM10".upper(),
                h,
                l,
                c,
                18.34,
            )
        )


if __name__ == "__main__":
    bars()
