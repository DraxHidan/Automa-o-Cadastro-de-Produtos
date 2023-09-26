# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir o chorome
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# entrar no link
pyautogui.click(x=421, y=53)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)


# Passo 2: Fazer login
pyautogui.click(x=808, y=351)
pyautogui.write("rafael@gmail.com")
pyautogui.press("tab")# passar pro campo de senha
pyautogui.write("210419")
pyautogui.press("tab")# passar pro botao de login
pyautogui.press("enter")

time.sleep(3)
# Passo 3: Importar a base de dados de produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

pyautogui.PAUSE = 0.1
for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=769, y=234)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_uni = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    

    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_uni))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # aperter pra enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(-5000)
    time.sleep(1)
    pyautogui.scroll(5000)

# Passo 5: Repetir o cadastro