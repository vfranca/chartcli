# -*- coding: utf-8 -*-
import click
from mtcli import indicator
from mtcli.mtcli import controller
from mtcli.fib import Fib
from mtcli.mt5_facade import MT5Facade
from mtcli.conf import (
    ORDER_ERROR,
    PRICE_CURRENT_ERROR,
    POSITION_MODIFIED_SUCCESS,
    POSITION_MODIFIED_ERROR,
)


@click.group()
def cli():
    """Console de scripts para MTCLI."""
    pass


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="daily", help="Tempo gráfico")
@click.option("--view", "-v", help="Formato de exibição")
@click.option("--count", "-c", type=int, default=40, help="Quantidade de barras")
@click.option("--date", "-d", help="Data (para day trade)")
def bars(symbol, period, view, count, date):
    """Listagem das barras do gráfico."""
    views = controller(symbol, period, view, date, count)
    for view in views:
        click.echo(view)
    return 0


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=20, help="Quantidade de períodos abrangidos no cálculo"
)
def sma(symbol, period, count):
    """Média móvel aritmética."""
    click.echo(indicator.sma.get_sma(symbol, period, count))


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=20, help="Quantidade de períodos abrangidos no cálculo"
)
def ema(symbol, period, count):
    """ Média móvel exponencial."""
    click.echo(indicator.ema.get_ema(symbol, period, count))


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=14, help="Quantidade de períodos abrangidos no cálculo"
)
def atr(symbol, period, count):
    """Range médio."""
    click.echo(indicator.atr.get_atr(symbol, period, count))


@click.command()
@click.argument("high")
@click.argument("low")
@click.argument("trend")
def fib(high, low, trend):
    """Retrações e extensões de fibonacci."""
    click.echo(Fib(float(high), float(low), str(trend)))


@click.command()
def account():
    """Exibe dados da conta de trading."""
    mt5 = MT5Facade()
    click.echo(mt5.account())
    return 0


@click.command()
@click.argument("symbol")
@click.option("--volume", "-v", type=int, help="Volume ou quantidade do ativo")
@click.option("--price", "-p", type=float, help="Preço de entrada da operação")
@click.option("--stop_loss", "-sl", type=float, help="Preço de stop loss da operação")
@click.option(
    "--take_profit",
    "-tp",
    type=float,
    help="Preço de take profit ou stop gain da operação",
)
def buy(symbol, volume, price, stop_loss, take_profit):
    """Executa uma órdem de compra."""
    mt5 = MT5Facade(symbol)

    # Compra a mercado
    if not price:
        res = mt5.buy(volume, stop_loss, take_profit)
        if res:
            click.echo(res)
        else:
            click.echo(ORDER_ERROR)
        return 0

    # Verifica se existe preço atual
    price_current = mt5.close()
    if price_current == None:
        click.echo(PRICE_CURRENT_ERROR)

    # Compra limitada
    if price <= price_current:
        res = mt5.buy_limit(price, volume, stop_loss, take_profit)

    # Compra stop
    if price > price_current:
        res = mt5.buy_stop(price, volume, stop_loss, take_profit)

    click.echo(res)
    return 0


@click.command()
@click.argument("symbol")
@click.option("--volume", "-v", type=int, help="Volume ou quantidade do ativo")
@click.option("--price", "-p", type=float, help="Preço de entrada da operação")
@click.option("--stop_loss", "-sl", type=float, help="Preço de stop loss da operação")
@click.option(
    "--take_profit",
    "-tp",
    type=float,
    help="Preço de take profit ou stop gain da operação",
)
def sell(symbol, volume, price, stop_loss, take_profit):
    """Executa uma órdem de venda."""
    mt5 = MT5Facade(symbol)

    # Venda a mercado
    if not price:
        res = mt5.sell(volume, stop_loss, take_profit)
        if res:
            click.echo(res)
        else:
            click.echo(ORDER_ERROR)
        return 0

    # Verifica se existe preço atual
    price_current = mt5.close()
    if price_current == None:
        click.echo(PRICE_CURRENT_ERROR)

    # Venda limitada
    if price >= price_current:
        res = mt5.sell_limit(price, volume, stop_loss, take_profit)

    # Venda stop
    if price < price_current:
        res = mt5.sell_stop(price, volume, stop_loss, take_profit)

    click.echo(res)
    return 0


@click.command()
@click.option("--symbol", "-s", help="Ativo da órdem")
@click.option("--ticket", "-t", type=int, help="Ticket da órdem")
@click.option("--cancel", "-c", help="Cancela todas as órdens pendentes")
def orders(symbol, ticket, cancel):
    """Gerencia as órdens pendentes."""
    mt5 = MT5Facade()
    click.echo(mt5.orders())
    return 0


@click.command()
@click.option("--symbol", "-s", help="Ativo da posição")
@click.option("--ticket", "-t", type=int, help="Ticket da posição")
@click.option("--volume", "-v", type=int, help="Volume a reduzir")
@click.option("--stop_loss", "-sl", type=float, help="Novo stop loss")
@click.option("--take_profit", "-tp", type=float, help="Novo take profit")
@click.option("--cancel", "-c", help="Cancela todas as posições abertas")
def positions(symbol, ticket, volume, stop_loss, take_profit, cancel):
    """Gerencia as posições abertas."""
    mt5 = MT5Facade()
    if bool(symbol):
        if bool(stop_loss):
            res = mt5.modify_position_symbol(symbol.upper(), stop_loss, 0.0)
        if bool(take_profit):
            res = mt5.modify_position_symbol(symbol.upper(), 0.0, take_profit)
        if res:
            click.echo(POSITION_MODIFIED_SUCCESS)
        else:
            click.echo(POSITION_MODIFIED_ERROR)
        return 0

    click.echo(mt5.positions())
    return 0


@click.command()
@click.argument("type")
@click.option("--symbol", "-s", help="Ativo cuja posição será cancelada")
@click.option("--order", "-o", help="Ticket da órdem a ser cancelada")
@click.option("--position", "-p", help="Ticket da posição a ser cancelada")
def cancel(type, symbol, order, position):
    """Cancela órdens e posições."""
    mt5 = MT5Facade()
    if type == "orders" or type == "all":
        res = mt5.cancel_orders()
        if res:
            res = "Todas as órdens foram canceladas com sucesso!"
        else:
            res = "Falha no cancelamento das órdens!"
        click.echo(res)
    if type == "positions" or type == "all":
        res = mt5.cancel_positions()
        if res:
            res = "Todas as posições foram canceladas com sucesso!"
        else:
            res = "Falha no cancelamento das posições!"
        click.echo(res)
    return 0


cli.add_command(bars)
cli.add_command(sma)
cli.add_command(ema)
cli.add_command(atr)
cli.add_command(fib)
cli.add_command(account)
cli.add_command(buy)
cli.add_command(sell)
cli.add_command(orders)
cli.add_command(positions)
cli.add_command(cancel)


if __name__ == "__main__":
    exit(cli())
