
#### Instalação - centOS
#### Instalação - MacOS
#### Instalação - Ubuntu
    I. Instale Conda via os seguintes comandos no terminal
```bash
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
    Dê as permissões necessárias para acessar o programa
```bash
    chmod 775 Miniconda3-latest-Linux-x86_64.sh
```
    Rode o script
```bash
    ./Miniconda3-latest-Linux-x86_64.sh
```

    II. Baixe o pip e instale da seguinte forma:
```bash
    wget https://bootstrap.pypa.io/get-pip.py
```
```python
    python get-pip.py
```
    III. Instale as dependências necessárias
```
    conda install matplotlib basemap numpy spyder arrow
```
    IV. Instale netcdf4 via pip
```bash
    pip install netcdf4
```
    V. Rode o programa via spyder
```bash
    spyder
```
#### Instalação - Windows

#### Necessário fazer

* Corrigir warnings relativos às mudanças de API na versão 2.0 do matplotlib
* Replicar correções para as variáveis restantes
* Corrigir geração de arquivos dat
* Adicionar guia de instalação para Ubuntu, centOS, Windows e Mac
* (Importante) Melhorar desacoplamento dos métodos e classes
* Utilizar classes
* Adicionar exemplo de utilização usando crontab
* Identificar tipo de blend que é utilizado em generateGraphs
* Adicionar no log, o tempo de cada rodada