import pandas as pd
import pyautogui
import time

#importar base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

pyautogui.PAUSE = 0.5

# abrir o sistema (no nosso caso o chrome)
pyautogui.press("win")   
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")   
pyautogui.click(x=916, y=512)
pyautogui.write("login")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=897, y=703)

# preencher lacunas com dados
for linha in tabela.index:
    pyautogui.click(x=1068, y=379)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if not pd.isna((tabela.loc[linha,"obs"])):
        pyautogui.write(str(tabela.loc[linha,"obs"]))   
       
    pyautogui.click(x=855, y=665)
    pyautogui.scroll(5000)
    