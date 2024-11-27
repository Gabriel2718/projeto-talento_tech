**Talento Tech-PR**
Autor: <a href="https://www.linkedin.com/in/gabriel-carvalho-reginato/" target="_blank">Gabriel Carvalho Reginato<a>
# Projeto invididual com Git

Meu projeto consiste em um algoritmo simples desenvolvido em Python que simula o gerenciamento do estoque de uma loja de componentes de computadores, aplicando os conhecimentos adquiridos nas disciplinas de Programação Orientada a Objetos e Fundamentos de Engenharia de Software no desenvolvimento da aplicação.


# Arquivos do projeto

Ao longo do projeto foram criados **12 arquivos Python**, sendo **um deles para armazenar a classe abstrata** (Componente), **7 para as classes que serão instanciadas** durante a execução da aplicação (Processador, Ram, Armazenamento, PlacaMae, PlacaDeVideo, Fonte e Gabinete), **1 para a classe intermediária (Memoria)** que herda da classe Componente e especializa as classes Armazenamento e Ram. Além destes, também foram criados **o arquivo para armazenar as funções de cadastro e consulta** dos objetos criados, **o arquivo para a execução da aplicação via terminal** e um arquivo que ao ser executado gera uma **interface gráfica criada a partir da biblioteca Tkinter**.

# Funcionalidades

## Terminal

É possível executar a aplicação via terminal através do arquivo terminal.py, que ao ser compilado exibirá um menu no terminal com as opções: **cadastrar componente**, onde o usuário deverá escolher, através do teclado numérico, um dos componentes listados no menu que aparecerá em seguida, e então inserir as informações básicas do produto; **consultar componentes**, que executará um laço que mostrará cada componente e seus respectivos dados de acordo com o método _consultarDados()_ de cada tipo de objeto; **sair**, que encerrará a execução.

## GUI (Interface Gráfica de Usuário)

A GUI, executada através do arquivo gui.py, oferece as mesmas funcionalidades da execução via terminal. No entanto, as operações de cadastro e consulta são realizadas por meio de inserção de dados em campos de texto e botões, assim como no material didático da disciplina de Programação Orientada a Objetos. Para a aba de cadastro da interface gráfica foi desenvolvido um algoritmo que atualiza os campos de texto e etiquetas de acordo com o tipo de componente selecionado. Na aba de consulta, foi criado um objeto do tipo Listbox para exibir os valores de uma lista que armazena o retorno da função _consultarDados()_ de cada componente cadastrado


# Cronograma do desenvolvimento

#### 22/11 - 23/11: Levantamento de requisitos e elaboração do diagrama de classes.
#### 23/11 - 24/11: Codificação do diagrama de classes e criação das funções de cadastro e consulta.
#### 24/11 - 25/11: Implementação da execução via terminal.
#### 27/11 - 27/11: Implementação da GUI e adaptação das funções de cadastro para serem utilizadas na GUI por meio de polimorfismo por sobrecarga.
