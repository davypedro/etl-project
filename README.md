## Pré-requisitos

### - VS Code: É o editor de código que vamos utilizar para desenvolver o nosso projeto de dados. Faça download do VS Code aqui: https://code.visualstudio.com/download

### - Git e GitHub:

Você deve ter o Git instalado em sua máquina.
Você também deve ter uma conta no GitHub. [Instruções de criação de conta no GitHub aqui] (https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account).

### - Pyenv: É usado para gerenciar versões do Python. Instruções de instalação do Pyenv aqui. Vamos usar nesse projeto o Python 3.11.3.

### - Poetry: Este projeto utiliza Poetry para gerenciamento de dependências. Instruções de instalação do Poetry aqui.

## Instalação e configuração

  1. Clone o repositório:
     https://github.com/davypedro/etl-project.git

  2. ## Configure a versão do Python com pyenv:
     - pyenv install 3.11.5
     - pyenv local 3.11.5
    
   3. ## Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:
     - poetry env use 3.11.5
     - poetry shell

   4. ## Instale as dependencias do projeto:
     - poetry install

   5. ## Execute os testes para garantir que tudo está funcionando como esperado:
      - task test

   6. ## Execute o comando de execucão da pipeline para realizar a ETL:
      - task run
     
   7. ## Verifique na pasta data/output se o arquivo foi gerado corretamente.
      
      
  
