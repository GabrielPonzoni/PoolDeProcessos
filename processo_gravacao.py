#subclasse
import csv
from processos import Processo
from functions import *

class WritingProcess(Processo):

    def __init__(self, pid:int, expressao:str) -> None:
        super().__init__(pid)
        self.__expressao = expressao
        self.__num1: float
        self.__num2: float
        self.__operador: str

    def __str__(self) -> str:
        return f"WritingProcess"
    
    @property
    def expressao(self):         # não tipificar: "expressao" sofrerá mudanças de tipo com .split()
        return self.__expressao
    
    @expressao.setter
    def expressao(self, expressao) -> None:
        self.__expressao = expressao

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
    def operador(self) -> str:
        return self.__operador

    @operador.setter
    def operador(self, operador) -> None:
        self.__operador = operador

    def analisador_de_expressao_matematica(self) -> None:
        '''Analisa e identifica os operandos e operador da expressão
        com a único objetivo de escrevê-la em "computation.txt" com
        a formatação correta. Parecido com o que existe em "processo_calculo.py".'''

        if ('+' in self.expressao) or ('-' in self.expressao) or ('*' in self.expressao) or ('/' in self.expressao):
            self.expressao = self.expressao.replace(' ','')
            if '+' in self.expressao:
                self.expressao = self.expressao.split('+')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '+'
            elif '-' in self.expressao:
                self.expressao = self.expressao.split('-')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '-'
            elif '*' in self.expressao:
                self.expressao = self.expressao.split('*')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '*'
            elif '/' in self.expressao:
                self.expressao = self.expressao.split('/')
                self.num1 = float(self.expressao[0])
                self.num2 = float(self.expressao[1])
                self.operador = '/'

    def execute(self) -> None:
        super().execute()
        self.analisador_de_expressao_matematica()
        with open('computation.txt', 'a') as arquivo:
            arquivo.write(str(self.num1) + ' ' + self.operador + ' ' + str(self.num2) + '\n') # ATENÇÃO: será impressa uma nova linha em branco ao final do arquivo
        print('Processo de gravação concluído com sucesso.')
