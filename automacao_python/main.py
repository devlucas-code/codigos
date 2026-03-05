import pyautogui
import time
import pandas as pd
import webbrowser

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

webbrowser.open(link)

time.sleep(5)

email = "lucasmarion@gmail.com"
senha = "123"

pyautogui.click(x=679, y=498)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

tabela = pd.read_csv("./produtos.csv")              
          
print(tabela)

for linha in tabela.index:
    print(f"Cadastrando produto linha {linha}")
    print(f"Cadastrando produto {tabela.loc[linha, 'codigo']}")
    
    pyautogui.click(x=657, y=345)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
         pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.scroll(1000)