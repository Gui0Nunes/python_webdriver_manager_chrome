
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# nav = webdriver.Chrome()
nav = webdriver.Firefox()
print('Abrir o navegador')
nav.get("https://guilhermenunes.com.br/selenium/")
print('Aguardar o carregamento da pagina')
time.sleep(3)
print('Digitar o Login')
time.sleep(1)
nav.find_element(By.ID,'login').send_keys("userTeste")
print('Digitar a Senha')
time.sleep(1)
nav.find_element(By.ID,'senha').send_keys("gui@nunes")
print('Clicar em entrar')
time.sleep(1)
nav.find_element(By.ID,'entrar_login').click()
time.sleep(1)
print('Clicar em Editar Contatos')
time.sleep(1)
nav.find_element(By.ID,'mdl-contatos').click()
time.sleep(1)
print('Imprimir o resultado')
time.sleep(1)
texto1 = nav.find_element(By.ID,'conteudoListaContatos').text
time.sleep(1)
print(texto1)

