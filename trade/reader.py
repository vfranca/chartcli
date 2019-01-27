from .src.reader import *
from .src.candle import Candle
from .src.fib import Fib

def reader(file, **kwargs):
    """Retorna uma lista de candles."""
    times = kwargs.get("times")
    date = kwargs.get("date")
    show = kwargs.get("show")
    candles = []
    high = []
    low = []
    body = []
    open = []
    close = []
    
    rows = chart_reader(file)
    for row in rows:
        candle = Candle(row)
        # Filtra a lista de candles a partir de uma data
        if date and candle.date != date:
            continue
        # Obtem a tendencia de topos e fundos
        high.append(candle.high)
        low.append(candle.low)
        if len(high) == 2:
            trend = get_trend(high, low)
            lt_diff = get_lt_diff(high, low, trend)
            high.pop(0)
            low.pop(0)
        else:
            trend = ""
            lt_diff = 0
        # Verifica a ocorr�ncia de padr?es de dois candles
        body.append(candle.body)
        open.append(candle.open)
        close.append(candle.close)
        if len(body) == 2:
            complex_pattern = get_two_candles_pattern(body, open, close)
            body.pop(0)
            open.pop(0)
            close.pop(0)
        else:
            complex_pattern = ""

        # Verifica o formato de exibi�?o
        if show == "full":
            candles.append(get_show_full(candle, trend = trend, complex_pattern = complex_pattern))
        elif show == "channel":
            candles.append(get_show_channel(candle, trend, lt_diff))
        elif show == "close":
            candles.append(get_show_close(candle))
        else:
            candles.append(get_show_default(candle, trend = trend, complex_pattern = complex_pattern))

        # Filtra a quantidade de candles
        if times and len(candles) > times:
            candles.pop(0)
            
    return candles
