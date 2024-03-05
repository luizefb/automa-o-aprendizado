import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

pyautogui.PAUSE = 0.5

#abrir navegador
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("Enter")

#Entra no site
pyautogui.write(link)
pyautogui.press("Enter")

#Loga a conta
time.sleep(2)
pyautogui.click(x=-1069, y=367, button="left")
pyautogui.write("emailgenerico@gmail.com")
pyautogui.press("Tab")
pyautogui.write("123")
pyautogui.click(x=-977, y=517, button="left")

#Cadastrando produtos da tabela do .csv
for linha in tabela.index:

    #codigo produto
    pyautogui.click(x=-1205, y=257, button="left")
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    #A marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #O tipo 
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #A categoria

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #O Preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #O custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")


    obs = tabela.loc[linha, "obs"]

    if not pandas.isna(obs):
    #Observação
        pyautogui.write(obs)
    pyautogui.press("tab")


    #Enviar produto
    pyautogui.press("Enter")