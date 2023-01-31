import pytest
from mtcli.paction import type_bar
from mtcli.paction import gap_fechamento
from mtcli.paction import variacao_percentual


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


def test_fechamento_com_gap_da_maxima_anterior():
    assert gap_fechamento([16, 17], [10, 20], [1, 10]) == "G7"


def test_fechamento_gap_da_minima_anterior():
    assert gap_fechamento([7, 6], [20, 10], [10, 1]) == "G-4"


def test_fechamento_sem_gap():
    assert gap_fechamento([10, 10], [15, 20], [5, 1]) == ""


def test_variacao_positiva_entre_fechamentos():
    assert variacao_percentual([10.00, 10.20]) == "2.0%"


def test_variacao_negativa_entre_fechamentos():
    assert variacao_percentual([10.00, 9.80]) == "-2.0%"


def test_sem_variacao_entre_fechamentos():
    assert variacao_percentual([10.00, 10.00]) == "0.0%"
