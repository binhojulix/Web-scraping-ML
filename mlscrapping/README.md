# Webscrapping ML


## A árvore do diretório

    ├── README.md
    ├── docker-compose.yml
    ├── run.bat
    ├── run.sh
    ├── scrap
    │   ├── requirements.txt
    │   ├── Dockerfile
    │   ├── setup.py
    │   ├── src
    │   │   ├── app.py
    │   │   └── conftest.py
    │   │   └── produto.py
    │   │   ├── app.py
    │   │   └── produtoBuilder.py
    │   │   └── scrap_jupyter.ipynb
    │   │   ├── scrap.py
    │   │   └── textStract.py
    │   ├── test
    │   │   ├── test_scrap.py
    │   │   └── test_textStract.py

### app.py

if __name__ == "__main__":
   scrap = Scrap(5)
   scrap.start()
  

# TO RUN ON DOCKER

`docker-compose up`


# TO RUN ON WINDOWS

`./run`

# TO RUN ON LINUX

`sh run.sh`

