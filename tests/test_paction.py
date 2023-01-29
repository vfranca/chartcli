import pytest
from mtcli.paction import type_bar


def test_barra_com_maxima_e_minima_mais_alta():
    assert type_bar([9, 10], [2, 3]) == "ASC"


def test_barra_com_maxima_mais_alta_e_minima_igual():
    assert type_bar([9, 10], [2, 2]) == "ASC"


def test_barra_com_minima_e_maxima_mais_baixa():
    assert type_bar([10, 9], [2, 1]) == "DESC"


def test_barra_com_minima_mais_baixa_e_maxima_igual():
    assert type_bar([10, 10], [2, 1]) == "DESC"


def test_barra_com_maxima_mais_alta_e_minima_mais_baixa():
    assert type_bar([9, 10], [2, 1]) == "OB"


def test_barra_com_maxima_mais_baixa_e_minima_mais_alta():
    assert type_bar([10, 9], [1, 2]) == "IB"


def test_barra_com_maxima_igual_e_minima_igual():
    assert type_bar([10, 10], [2, 2]) == "IB"
