Gabriel Ponzoni
Gaspar Caon

GERENCIADOR DE PROCESSOS PRAXEDES
=================================

Este programa permite ao usuário gerenciar uma fila (lista)
de processos.

"functions.py" é um arquivo que contem funções de uso recor-
rente dentro do método principal, como validação de input de
usuário e comandos taquigráficos (como limpeza de tela).

"gerador_pid.py" é uma classe que gerencia PIDs segundo uma
fórmula específica. Apenas um objeto desta classe é empregado.

"fila_de_processos.txt" é um arquivo CSV responsável por arma-
zenar uma fila de processos, se solicitado. Diferentemente do
arquivo "computation.txt", que apenas armazena expressões mate-
máticas, "fila_de_processos.txt" contém os tipos de processos
e expressões matemáticas, nos casos em que o processo seja um
processo de cálculo.

O programa possui um recurso extra no menu principal: uma opção
para o usuário verificar o conteúdo da fila de processos SEM a
necessidade de criar um processo de impressão. Tal recurso mos-
trou-se muito útil para fins de debug, e consideramos útil man-
tê-lo ativo.

Ademais, os seguintes recursos, embora não estudados explicita-
mente em sala de aula, nos foram sugeridos por IA, pesquisas no
site Stack Overflow e vídeos do youtube para resolver problemas 
encontrados durante a programação:

- global
- enumeration
- __str__()
- del
- try: e except: