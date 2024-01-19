import pyautogui
import time
import pandas 

tabelaChamados = pandas.read_csv("totalChamados.csv")
for linha in tabelaChamados.index:

    pyautogui.PAUSE = 2 #pausa entre atividades/operações esta em segundos

    #Passo 1 - Entrar no sistema da empresa

    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    link = "https://tclsemp.topdesk.net/"
    pyautogui.write(link)
    pyautogui.press("enter")

    #Selecionar campo de autoatendimento e preencher o login

    pyautogui.click(x=959, y=654)
    #time.sleep(1)
    pyautogui.click(x=899, y=776)
    time.sleep(2)

    #Escolhendo a categoria de chamado

    pyautogui.click(x=1003, y=727)
    time.sleep(1)
    pyautogui.click(x=425, y=754)
    time.sleep(1)
    pyautogui.click(591, y=735)
    time.sleep(1)
    pyautogui.click(x=1277, y=880)
    time.sleep(1)

    #Preenchendo campos do chamado e enviando

    usuario = tabelaChamados.loc[linha, "usuario"]
    pyautogui.click(x=813, y=701)
    pyautogui.write('Solicito troca de monitor do usuario')
    time.sleep(1)
    pyautogui.click(x=661, y=752)
    time.sleep(1)
    pyautogui.write('Solicito a substituicao do monitor do usuario: '+usuario)
    pyautogui.click(x=1085, y=990)
    pyautogui.click(x=1883, y=23)



