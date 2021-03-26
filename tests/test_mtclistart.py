from mtcli import mtclistart
import mock


@mock.patch("mtcli.mtclistart.input")
def test_obtem_string_do_caminho_do_csv(input):
    input.return_value = "c:"
    assert mtclistart.get_csv_path() == "c:"


def test_nome_do_arquivo_env():
    assert mtclistart.env_filename == ".env"


def test_caminho_do_csv_reformatado():
    path = "C:\\Files"
    assert mtclistart.path_format(path) == "c:/Files/"


def test_cria_arquivo_env_com_os_parametros_iniciais():
    path = "C:/Files/"
    assert mtclistart.create_envfile(path) == True
