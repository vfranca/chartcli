# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click
from mtcli.csv_data import Rates


# Cria o comando ma
@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", type=int, default=40, help="Quantidade de barras")
@click.option("--method", "-m", default="", help="")
@click.option("--date", "-d", default="", help="Data (para day trade)")
def ma(symbol, period, count, method, date):
    """Exibe o histórico de médias móveis."""
    # Arquivo CSV contendo as médias móveis
    # csv_file = conf.csv_path + symbol + period + "-MA.csv"
    # Importa as médias móveis
    # rates = Rates(csv_file)
    click.echo("moving average")


if __name__ == "__main__":
    ma()