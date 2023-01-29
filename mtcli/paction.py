# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from mtcli.conf import up_bar, down_bar, outside_bar, inside_bar

# Verifica o tipo da barra
def type_bar(h, l):
    """Verifica o tipo da barra."""
    # Verifica se é uma upbar
    # máxima mais alta e mínima mais alta ou igual
    if h[1] > h[0] and l[1] >= l[0]:
        return up_bar
    # Verifica se é uma downbar
    # mínima mais baixa e máxima mais baixa ou igual
    if l[1] < l[0] and h[1] <= h[0]:
        return down_bar
    # Verifica se é uma outside bar
    # máxima mais alta e mínima mais baixa
    if h[1] > h[0] and l[1] < l[0]:
        return outside_bar
    # Verifica se é uma inside bar
    # máxima mais baixa ou igual e mínima mais alta ou igual
    if h[1] <= h[0] and l[1] >= l[0]:
        return inside_bar