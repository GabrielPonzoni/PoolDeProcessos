GERENCIADOR DE PROCESSOS PRAXEDES
=================================

### Este programa permite ao usuário gerenciar uma fila (lista) de processos em arquivos .txt, cada processo pode ser executado separadamente. 
>Problema proposto para o Simulador de Execução de Processos construída com base na descrição original do Prof. Márcio Garcia Martins [(Unisinos)](https://www.unisinos.br/)

# 🔨 Funcionalidades do projeto

- `Funcionalidade 1`: criar processo, abre opções para criar 4 tipos de processos, são eles: Calculo, Gravacao, Impressao, Leitura. Para cada processo criado é atribuido um PID (Process ID) que identifica numericamente o Processo
- `Funcionalidade 2`: executar próximo processo, tem como funçao executar o primeiro elemento da fila/lista de processos, mostrando no terminal o __execute()__ do processo, logo em seguida ele o remove da fila de processos.
- `Funcionalidade 3`: executar processo específico, ele solicita um input do PID do processo, após isso verifica na lista se o processo existe, realiza a execuçao do processo e por fim o remove da fila de processos.
- `Funcionalidade 4`: salvar fila de processos do arquivo, salva o fila que foi criada durante a execução do programa que foi manipulada ou até mesmo criada num arquivo .txt 
- `Funcionalidade 5`: Carregar fila de processos do arquivo, importa essa fila que está dentro do arquivo fila_de_processos.txt __sobrevescrevendo__ a fila que já está dentro do programa, caso essa mesma esteja vazia e o programa esteja com alguns itens na fila eles serão __sobrescritos__.
- `Funcionalidade 6`: mostrar a fila de processos que estão __apenas__ dentro do programa durante sua execução, é uma exibicao semelhante ao processo.execute() da classe processo_leitura. Mostra todos os PID e os tipo do processos de cada um armazenado na lista.
- `Funcionalidade 7`: Finaliza o programa. _Nota: Não salva a fila que foi criada durante a execucao do programa, para salvar deve usar a funcionalidade 4._

# 💭Considerações

"functions.py" é um arquivo que contem funções de uso recor rente dentro do método principal, como validação de input de usuário e comandos taquigráficos (como limpeza de tela).

"gerador_pid.py" é uma classe que gerencia PIDs segundo uma
fórmula específica. Apenas um objeto desta classe é empregado.

"fila_de_processos.txt" é um arquivo CSV responsável por armazenar uma fila de processos, se solicitado. Diferentemente do arquivo "computation.txt", que apenas armazena expressões matemáticas, "fila_de_processos.txt" contém os tipos de processos e expressões matemáticas, nos casos em que o processo seja um processo de cálculo.

O programa possui um recurso extra no menu principal: uma opção
para o usuário verificar o conteúdo da fila de processos SEM a
necessidade de criar um processo de impressão. Tal recurso mostrou-se muito útil para fins de debug, e consideramos útil mantê-lo ativo.

Ademais, os seguintes recursos, embora não estudados explicita-
mente em sala de aula, nos foram sugeridos por IA, pesquisas no
site Stack Overflow e vídeos do youtube para resolver problemas 
encontrados durante a programação:

- ``global``
- ``enumeration``
- `__str__()`
- ``del``
- ``try:`` e ``except:``

### Autores:
| [<img loading="lazy" src="https://i.postimg.cc/28zXxtWH/333365603-1006563527394289-653866351373794602-n.jpg" width=115><br><sub>Gabriel Ponzoni</sub>](https://github.com/GabrielPonzoni) |  [<img loading="lazy" src="https://i.postimg.cc/j2YBKdLK/Imagem-do-Whats-App-de-2024-07-03-s-11-25-21-b72c1111.jpg" width=115><br><sub>Gaspar Machado Caon</sub>](https://github.com/MeanRaccoon) |
| :---: | :---: |
