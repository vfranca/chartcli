from mtcli import conf
from mtcli import __version__
import click

# Importa os comandos
from mtcli.bars import bars
from mtcli.mm import mm
from mtcli.rm import rm


# Cria o grupo de comandos mt
@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Exibe a versao")
def mt(version):
    """Converte graficos do MetaTrader 5 para texto."""
    if version:
        click.echo("mtcli %s" % __version__)
        return 0


# Adiciona os comandos do mt
mt.add_command(bars)
mt.add_command(mm)
mt.add_command(rm)

if __name__ == "__main__":
    mt()
