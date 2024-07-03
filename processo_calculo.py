#subclasse
from processos import Processo
from functions import *

class ComputingProcess(Processo):

    def __init__(self, pid: int, expressao:str) -> None:
        super().__init__(pid)
        self.__expressao = expressao
        self.__num1: float
        self.__num2: float
        self.__operador: str
    
    def __str__(self) -> str:
        return f"ComputingProcess"

    @property
    def num1(self) -> float:
        return self.__num1
    
    @num1.setter
    def num1(self, num) -> None:
        self.__num1 = num

    @property
    def num2(self) -> float:
        return self.__num2
    
    @num2.setter
    def num2(self, num) -> None:
        self.__num2 = num

    @property
    def expressao(self):        # não tipificar: "expressao" sofrerá mudanças de tipo com .split()
        return self.__expressao
    
    @expressao.setter
    def expressao(self, expressao):
        self.__expressao = expressao

    @property
    def operador(self) -> str:
        return self.__operador
    
    @operador.setter
    def operador(self, operador) -> None:
        self.__operador = operador

    def execute(self) -> None:
        super().execute()
        operador = '_'
        if '+' in self.expressao or '-' in self.expressao or '*' in self.expressao or '/' in self.expressao:
            self.expressao = self.expressao.replace(' ','')
            if '+' in self.expressao:
                self.expressao = self.expressao.split('+')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '+'
                print(f'Processo {self.pid}:\t{self.num1} {self.operador} {self.num2} = {self.num1 + self.num2}')
            elif '-' in self.expressao:
                self.expressao = self.expressao.split('-')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '-'
                print(f'Processo {self.pid}:\t{self.num1} {self.operador} {self.num2} = {self.num1 - self.num2}')
            elif '*' in self.expressao:
                self.expressao = self.expressao.split('*')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '*'
                print(f'Processo {self.pid}:\t{self.num1} {self.operador} {self.num2} = {self.num1 * self.num2}')
            elif '/' in self.expressao:
                self.expressao = self.expressao.split('/')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '/'
                try:
                    print(f'\tProcesso {self.pid}:\t{self.num1} {self.operador} {self.num2} = {self.num1 / self.num2}')
                except ZeroDivisionError:
                    print(f'ERRO no processo {self.pid}: divisão por zero. Continuando...')
