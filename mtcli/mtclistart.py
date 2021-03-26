# Cria o .env do mtcli


env_filename = ".env"


def get_csv_path():
    path = str(input("Digite o caminho do MetaTrader 5"))
    return path


def path_format(path):
    return "c:/Files/"


def create_envfile(path):
    return 1


if __name__ == "__main__":
    path = get_csv_path()
    print(path)
    path = path_format(path)
    print(path)
