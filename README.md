# 2023.1-Amis-ClassroomService


## Como executar os testes

Caso esteja já esteja no `docker` basta executar o seguinte comando : 

```bash
PYTHONPATH=src TEST=true pytest -v -s
```

Caso contrário recomenda-se utilizar um [ambiente virtual](https://docs.python.org/3/tutorial/venv.html) para instalar as dependências e executar os testes, estando na raiz do projeto basta seguir os passos a seguir.

```bash
# Cria um ambiente virtual e utiliza ele como source
python3 -m venv venv
source venv/bin/activate

# Instalação das dependências
pip3 install -r requirements.txt

# Execução dos testes.
PYTHONPATH=src TEST=true pytest -v -s
```
