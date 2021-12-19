# Web scraping ML


## tree

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


## how to use

cloen this repository, type `cd Web-scraping-ML/mlscrapping`.

to run on docker `docker-compose up`.

to run on windows `./run`.

to run on  linux `sh run.sh`.


## Un caso en el que usarías procesos para resolver un problema y por qué.
 `docker-compose up`

##	Un caso en el que usarías threads para resolver un problema y por qué.
 `en procesos paralelos o concordantes.`

 `ex: request an api in  main thread of android .`

 `no trabajar el thread principal . `



##	Un caso en el que usarías corrutinas para resolver un problema y por qué.
 `docker-compose up`



## Next step

- _Disponilizar Kafka 
