#superclasse
class Processo:
    def __init__(self, pid: int) -> None:
        self.__pid = pid
        # PID será um código gerado segundo uma fórmula.
        # Quando um processo for gerado, o PID será calculado,
        # e precisa ser único para cada processo. É preciso
        # ter algum valor de referência inicial para o primeiro PID.
        # sugiro lançar tal valor no método principal.
    
    #get e setter __pid
    @property
    def pid(self) -> int:
        return self.__pid
    
    @pid.setter
    def pid(self, pid) -> None:
        self.__pid = pid
    
    def execute(self): # apenas declaraçao do processo execute
        pass