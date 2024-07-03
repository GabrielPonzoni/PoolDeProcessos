# Classe que gera um objeto contador de PID.
# O ideal é ter apenas 01 objeto desta classe.

class Gerador_PID:
    
    def __init__(self):
        self.__pid: int = 100       # PID inicial, ou de referência

    @property
    def pid(self) -> int:
        return self.__pid

    @pid.setter
    def pid(self, novo_pid:int) -> None:
        self.__pid:int = novo_pid

    # calcula o próximo PID e atualiza PID de referência
    def calcula_pid(self) -> int:
        self.pid += 3
        return self.pid       # PID é calculado por: PID = PID + 3