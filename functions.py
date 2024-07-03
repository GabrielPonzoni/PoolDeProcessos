# arquivo com banco de funções de utilidade geral
import os
from processos import *

def clear_screen() -> None:
    '''Função para limpar a tela.'''
    os.system('cls')
    
def press_enter() -> None:
    '''Pausa o rolamento da tela para mostrar
    algum resultado para o usuário. Geralmente usada
    antes de limpar a tela com a função clear_screen().'''
    input('(Pressione Enter)')

def validador_input_s_n() -> str:
    '''Função que valida as entradas do usuário, aceitando apenas 's','S' ou 'n','N'.
    Returns:
    str: A entrada do usuário verificada.'''

    user_input: str = input()
    validador: bool = False

    while(validador == False):
        if (user_input == '') or (user_input == None):
            print(f'Digite S ou N.')
            user_input = input()
        elif (user_input.lower() != 's') and (user_input.lower() != 'n'):
            print(f'Opção inválida. Digite S ou N.')
            user_input = input()
        else:
            validador = True
    return user_input.lower()

def validador_input_numeros(upper_range:int) -> str:
    '''Função que valida as entradas do usuário, aceitando apenas números inteiros positivos.
    Returns: 
    str: O número verificado informado pelo usuário.'''
    
    # verifica se o usuário entrou com um número inteiro;

    user_input: str  = input()
    validador: bool = False

    while(validador == False):
        if (user_input == '') or (user_input == None):
            user_input = input('Digite uma opção numérica.\n')
        elif (int(user_input) > upper_range) or (int(user_input) < 1):
            user_input = input('Digite uma opção válida do menu.\n')
        else:
            try:
                if isinstance(int(user_input), int) == True:
                    validador = True
            except ValueError:
                user_input = input('Digite apenas numéros.\n')
    return user_input
