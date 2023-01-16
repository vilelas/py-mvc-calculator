# Calculadora em Python utilizando o padrão MVC

Esta é uma aplicação simples de calculadora desenvolvida em Python utilizando o padrão de projeto MVC (Model-View-Controller). Ela permite realizar operações básicas de matemática, como adição, subtração, multiplicação e divisão, e tem uma interface amigável e fácil de usar.

## Instalação

Para usar esta aplicação, você precisará ter o Python instalado em sua máquina. Ele pode ser baixado em [python.org.](https://www.python.org/)

Clone o repositório para sua máquina:

```bash
git clone https://github.com/vilelas/py-mvc-calculator.git
```

Entre na pasta do projeto:

```bash
cd py-mvc-calculator
```

## Execução

Para iniciar a aplicação, basta executar o arquivo `main.py`:

```bash
python main.py
```

## Como usar

Ao iniciar a aplicação, você verá uma tela com as opções de operações matemáticas. Selecione a operação desejada e insira os números nos campos indicados. Em seguida, pressione o botão "Enter" do seu teclado para obter o resultado.

## Arquitetura

Este projeto utiliza o padrão de projeto MVC para separar as responsabilidades da aplicação em três camadas: modelo, visualização e controlador. Isso torna o código mais organizado e fácil de manter.

### Modelo

A camada de modelo contém as regras de negócios da aplicação, como as operações matemáticas.

### Visualização

A camada de visualização contém a interface gráfica da aplicação, responsável por exibir as informações para o usuário e receber as entradas dele.

### Controlador

A camada de controlador é responsável por intermediar a comunicação entre a visualização e o modelo. Ele recebe as entradas do usuário da visualização e as envia para o modelo para processamento, e então exibe o resultado para o usuário.

## Contribuindo

Este projeto é open-source e aceita contribuições. Se você tem uma sugestão de melhoria ou encontrou um bug, sinta-se à vontade para abrir uma issue ou fazer um pull request.