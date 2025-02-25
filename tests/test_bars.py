# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_o_grafico_no_formato_minimo():
    res = run.invoke(mt, ["bars", "ibov", "--view", "ch", "--count", "1"])
    assert res.output == " 114191.00 112044.00 112316.00\n"


# def test_exibe_o_grafico_no_formato_ranges():
# def test_exibe_o_grafico_no_formato_completo():
