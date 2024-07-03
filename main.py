from random import *
from gerador_pid import *
from functions import *

from processos import *
from processo_calculo import *
from processo_gravacao import *
from processo_leitura import *
from processo_impressao import *

def menu_principal() -> None:
    global fila_de_processos
    
    validador: bool = False
    while(validador == False):

        clear_screen()
        print('GERENCIADOR DE PROCESSOS PRAXEDES LTDA.')
        print('=======================================')
        print('Digite a opção desejada:\n')
        print('1. Criar processo')
        print('2. Executar próximo processo')
        print('3. Executar processo específico')
        print('4. Salvar fila de processos')
        print('5. Carregar fila de processos do arquivo (a fila de processos será completamente sobreescrita!)')
        print('6. Mostrar fila de processos SEM gerar processo de impressão')
        print('7. Sair')
    
        user_input = validador_input_numeros(7)

        match user_input:
            case '1':
                criar_processo()
            case '2':
                executar_proximo_processo()
            case '3':
                executar_processo_especifico()
            case '4':
                salvar_fila_de_processos()
            case '5':
                fila_de_processos = carregar_fila_de_processos_do_arquivo()
            case '6':
                mostrar_lista_de_processos()
            case '7':
                validador = True  # exit while loop
                print('Saindo...')
            case _:
                pass

def criar_processo() -> None:

    validador: bool = False
    while(validador == False):

        clear_screen()
        print('Qual processo deseja criar? Digite a opção desejada:\n')
        print('1. Processo de cálculo')
        print('2. Processo de impressão')
        print('3. Processo de leitura')
        print('4. Processo de gravação')
        print('5. Voltar')

        user_input = validador_input_numeros(5)

        match user_input:
            case '1':
                novo_processo_de_calculo(gerador.calcula_pid())
            case '2':
                novo_processo_de_impressao(gerador.calcula_pid())
            case '3':
                novo_processo_de_leitura(gerador.calcula_pid())
            case '4':
                novo_processo_de_gravacao(gerador.calcula_pid())
            case '5':
                validador = True
            case _:
                pass

def novo_processo_de_calculo(pid:int) -> None:
    '''Cria um processo de cálculo e adiciona-o à fila de processos.
    Solicita ao usuário informar uma expressão matemática. Essa expressão
    será avaliada quando o método 'execute()' for chamado.'''

    expressao = input('Informe a expressão no formato [Número] [Operador] [Número]:\n')
    fila_de_processos.append(ComputingProcess(pid, expressao))
    print('Processo de cálculo adicionado na fila com sucesso.')
    press_enter()

def novo_processo_de_impressao(pid:int) -> None:
    '''Cria um processo de impressão e adiciona-o à fila de processos.'''

    #global fila_de_processos
    fila_de_processos.append(PrintingProcess(pid, fila_de_processos))       # ATENÇÃO: POSSÍVEL CIRCULARIDADE DETECTADA
    print('Processo de impressão adicionado na fila com sucesso.')
    press_enter()

def novo_processo_de_leitura(pid:int) -> None:
    '''Cria um processo de leitura e adiciona-o à fila de processos.'''

    fila_de_processos.append(ReadingProcess(pid))
    print('Processo de leitura de cálculos adicionado na fila com sucesso.')
    press_enter()

def novo_processo_de_gravacao(pid:int) -> None:
    '''Cria um processo de gravação e adiciona-o à fila de processos.'''
    
    global fila_de_processos
    expressao = input('Informe a expressão no formato [Número] [Operador] [Número]:\n')
    fila_de_processos.append(WritingProcess(pid, expressao))
    print('Processo de gravação de cálculo adicionado na fila com sucesso.')
    press_enter()

def executar_proximo_processo() -> None:
    '''Identifica o tipo do próximo processo.
    Executa o respectivo método execute() e trabalha com o seu output se necessário.'''

    global fila_de_processos
    try:
        match fila_de_processos[0].__str__():            
            case "ComputingProcess":
                print(f'Executando processo de cálculo {fila_de_processos[0].pid}...')
                fila_de_processos[0].execute()
                del fila_de_processos[0]
                press_enter()         
            case "PrintingProcess":               
                print(f'Executando processo de impressão {fila_de_processos[0].pid}...')
                fila_de_processos[0].execute()
                del fila_de_processos[0] 
                press_enter()            
            case "ReadingProcess":                
                print(f'Executando processo de leitura {fila_de_processos[0].pid}...')
                lista_de_linhas: list = fila_de_processos[0].execute()
                del fila_de_processos[0]
                for linha in lista_de_linhas:   # linha é uma lista com 1 expressão matemática na forma de string
                    fila_de_processos.append(ComputingProcess(gerador.calcula_pid(), linha[0]))
                press_enter()
            case "WritingProcess":           
                    print(f'Executando processo de gravação {fila_de_processos[0].pid}...')
                    fila_de_processos[0].execute()
                    del fila_de_processos[0] 
                    press_enter()    
            case _:
                print('Há pelo menos 01 processo não identificado.')
                press_enter()
    except IndexError:
        print('A fila de processos está vazia, ou terminou.')
        press_enter()

def executar_processo_especifico() -> None: 
    global fila_de_processos
    if fila_de_processos == []:
        print('A fila de processos está vazia, ou terminou.')
        press_enter()
    else:
        print("Digite o PID do processo desejado:")
        user_input = validador_input_numeros(1000)

        processo_existe: bool = False
        for indice, processo in enumerate(fila_de_processos):
            # procura por um match entre os pids na fila de processos;
            # enumerate conta o índice e o seu respectivo elemento da fila de processos;
            # esta foi uma dica do chatGpt para evitar problemas de índice após deleção de elementos durante o loop
            if processo.pid == int(user_input):
                processo_existe = True
                # verificar se é um processo de leitura
                if processo.__str__() == "ReadingProcess":
                    print(f'Executando processo de leitura {processo.pid}...')
                    lista_de_linhas: list = processo.execute()
                    del fila_de_processos[indice]
                    for linha in lista_de_linhas:   # linha é uma lista com 1 expressão matemática na forma de string
                        fila_de_processos.append(ComputingProcess(gerador.calcula_pid(), linha[0]))
                    print('Processo de leitura executado com sucesso.')
                    press_enter()
                    break
                else:
                    processo.execute()
                    del fila_de_processos[indice]
                    press_enter()
                    break
        if processo_existe == False:
            print('O PID informado não corresponde a nenhum processo.')
            press_enter()

def salvar_fila_de_processos() -> None:
    global fila_de_processos
    '''Salva a fila de processos no arquivo "fila_de_processos.txt". O formato do arquivo se parece com:

    0,2/5
    1
    3,8+9
    2
    ...

    O primeiro número é um rótulo do enumerador de processos (ver declaração no método principal).
    Para processos de cálculo e de gravação, consta também a expressão matemática relacionada.
    '''

    if fila_de_processos == []:
        print("A fila de processos está vazia.")
        press_enter()
    else:        
        with open('fila_de_processos.txt', 'w') as arquivo: 
            for processo in fila_de_processos:
                print(processo)
                match processo.__str__():            
                    case "ComputingProcess":
                        arquivo.write(processo.__str__() + ',' + processo.expressao + '\n')
                    case "PrintingProcess":
                        arquivo.write(processo.__str__() + '\n')
                    case "ReadingProcess":
                        arquivo.write(processo.__str__() + '\n')
                    case "WritingProcess":
                        arquivo.write(processo.__str__() + ',' + processo.expressao + '\n')
                    case _:
                        arquivo.write(f"Processo {processo.pid} não identificado.")
        print("Fila de processos salvada com sucesso em 'fila_de_processos.txt'.")
        press_enter()

def carregar_fila_de_processos_do_arquivo() -> list:
    fila_de_processos = []
    
    with open('fila_de_processos.txt', 'r') as arquivo:
        lista_das_linhas = list(csv.reader(arquivo))

    for linha in lista_das_linhas:
        match linha[0]:
            case "ComputingProcess":
                fila_de_processos.append(ComputingProcess(gerador.calcula_pid(),linha[1]))
            case "PrintingProcess":
                fila_de_processos.append(PrintingProcess(gerador.calcula_pid(),fila_de_processos))   # ATENÇÃO: POSSÍVEL CIRCULARIDADE DETECTADA
            case "ReadingProcess":
                fila_de_processos.append(ReadingProcess(gerador.calcula_pid()))
            case "WritingProcess":
                fila_de_processos.append(WritingProcess(gerador.calcula_pid(),linha[1]))

    print("Fila de processos importada do arquivo com sucesso.")
    press_enter()
    return fila_de_processos

def mostrar_lista_de_processos() -> None:
    '''Mostra a fila de processos SEM gerar um processo de impressão'''
    global fila_de_processos

    clear_screen()
    for x in fila_de_processos:
        print(f'{x.pid}\t{x}')
    press_enter()

def main():
    # declaração de variáveis de escopo global, acessíveis em todo o programa

    global gerador
    gerador = Gerador_PID()     # cria um objeto gerador de PIDs
    global fila_de_processos
    fila_de_processos = []
    
    menu_principal()

if __name__ == '__main__':
    main()