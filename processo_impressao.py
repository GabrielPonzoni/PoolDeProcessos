#subclasse
from processos import Processo
from functions import *

class PrintingProcess(Processo):

    def __init__(self, pid: int, lista_de_processos:list) -> None:
        super().__init__(pid)
        self.__lista_de_processos = lista_de_processos

    def __str__(self) -> str:
        return f"PrintingProcess"
    
    @property
    def lista_de_processos(self) -> list:
        return self.__lista_de_processos
    
    def execute(self) -> None:
        super().execute()
        for processo in self.lista_de_processos:
            if processo.__str__() == "ComputingProcess":
                print(f'{processo.pid}\t\t{processo}\t\t{processo.expressao}')
            else:
                print(f'{processo.pid}\t\t{processo}')
        print('Processo de impressão concluído com sucesso.')
        
