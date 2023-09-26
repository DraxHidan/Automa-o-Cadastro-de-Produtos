import pyautogui
import time

pyautogui.PAUSE = 0.5


# entrando no navegador

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# entrando no whats

pyautogui.click(x=19, y=202)
time.sleep(5)


# selecionando a primeira conversa recente

pyautogui.click(x=275, y=158)
time.sleep(1)

# escreve a mensagem

for i in range(0, 5):
    pyautogui.write("teste")
    pyautogui.press("enter")


