#Passo a passo do projeto
#instalação bibliotecas sem certificado: pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <Nome da biblioteca>
#Passo 1 - Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Passo 3 - Importar base de dados
#Passo 4 - Cadastrar um produto
#Passo 5 - Repetir isso ate acabar a base de dados

#Biblioteca: pyautogui, time (Pausa a operação em determinada trecho do codigo)

#clicar = payautogui.click
#escrever = pyautogui.write
#apertar uma tecla = pyautogui.press
#Atalho = pyautogui.hotkey
#scroll = pyautogui.scroll (1000) (-1000) positivo para cima negativo para baixo

import pyautogui
import time
import pandas



pyautogui.PAUSE = 1 #pausa entre atividades/operações esta em segundos

#Passo 1 - Entrar no sistema da empresa

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#digitar o link

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

#apertar o enter

pyautogui.press("enter")
time.sleep(5) 

#Passo 2 - Fazer Login
pyautogui.click(x=-1167, y=405) #clicar nas cordenadas adquiridas no auxiliar.pý
#Digitar email
pyautogui.write("jarlissonxavier@gmail.com")
#Proximo Campo Senha:
pyautogui.press("tab")
#Digitar Senha
pyautogui.write("minha senha")
#Clicar no botaop logar, pegar coordenadas
pyautogui.click(x=-971, y=573)
time.sleep(3)

#importar base de dados
#pip install pandas numpy openpyxl

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=-1184, y=292)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #'1'
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

