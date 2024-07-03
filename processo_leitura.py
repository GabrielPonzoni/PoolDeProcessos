#subclasse
import csv
from processos import Processo
from functions import *

class ReadingProcess(Processo):

    def __init__(self, pid:int) -> None:
        super().__init__(pid)

    def __str__(self) -> str:
        return f"ReadingProcess"

    # retorna uma matriz (lista de listas). cada elemento é uma linha do arquivo lido;
    def execute(self) -> list: 
        super().execute()

        with open('computation.txt', 'r') as arquivo:
            lista_das_linhas = list(csv.reader(arquivo))
        print('Processo de leitura concluído com sucesso.')
        with open('computation.txt', 'w') as arquivo:   # reescreve o arquivo mas vazio
            pass
        return lista_das_linhas
