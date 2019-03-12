# Django 2.x 
## Roteiro de Instalação no Linux Ubuntu 14.04
O roteiro abaixo visa dar passo-a-passo o que é necessário para criação de uma aplicação utilizando o Django framework.

### Passo: Criação do Diretório de Trabalho
Crie uma pasta que receberá o Ambiente Virtual e o projeto propriamente dito.

```shell
$ mkdir firstproj
$ cd firstproj
```
<a name="step_virtualenv"></a>
### Passo: Criação do Ambiente Virtual (VirtualEnv)
O ambiente virtual é um estilo de desenvolvimento que isola as versões utilizadas durante o desenvolvimento.
Assim que o ambiente for ativado, o prefixo **(venv)** aparecerá no prompt.

```shell
$ sudo apt-get install python3.4-venv  # Caso não esteja instalado
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install django==2.0.13  # Last release for python 3.4
```
#### Extras
Se 
*** WINDOWS
// Download Python 3.7 from https://www.python.org/downloads/windows
Setting up Virtual Env
$ python -m venv c/Roque/lab/Django/PythonREST/Django01/
Activate Virtual Env
$ . Scripts/activate
// Upgrade PIP
$ pip install --upgrade pip
// Install Django
$ pip install django
$ pip install djangorestframework
$ pip install django-filter
Download SQLite from https://www.sqlite.org/download.html
Download SQLiteBrowser from https://sqlitebrowser.org/dl/
// To test app
$ pip install --user --upgrade httpie
$ pip install ipython
https://www.getpostman.com/downloads/

___
### What Python version can I use with Django?

Django     |Versão do Python                                       
-----------|---------------------------------------------
1.11.20    |2.7, 3.4, 3.5, 3.6, 3.7 (added in 1.11.17)   
2.0.13	   |3.4, 3.5, 3.6, 3.7                           
2.1, 2.2   |3.5, 3.6, 3.7                                

### Pacotes úteis
Não esqueça de ativar a [VirtualEnv](#step_virtualenv).

##### Fotos e Imagens com [Pillow](https://pillow.readthedocs.io/en/stable)
```shell
(venv) $ pip install Pillow   
```
##### Criação de API's com [Django REST Framework](https://www.django-rest-framework.org)
```shell  
(venv) $ pip install djangorestframework
(venv) $ pip install django-filter
```


### Referências

[Django Releases](https://docs.djangoproject.com/pt-br/2.1/releases/)  
[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)   
[Httpie][HTTPie]  
[Postman][Postman]

[Postman]: https://www.getpostman.com "Official Website"
[HTTPie]: https://httpie.org "Official Website"