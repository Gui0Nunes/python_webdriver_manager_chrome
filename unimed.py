#Nesse exemplo vamos acessar o site do laboratório de exames da unimed de Jaú e baixar o resultado de um exame

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 
import dotenv
import os
from dotenv import load_dotenv
dotenv.load_dotenv(dotenv.find_dotenv('./env/.env'))

username = os.getenv('username')
senha = os.getenv('senha')
link = os.getenv('link')
#abaixo: teste print das informações .env
# print(username+'-'+senha)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(link)
#time.sleep(2)

navegador.find_element('xpath','//*[@id="ctl00_ContentPlaceHolderConteudo_TXT_postoAmostraUnificado"]').send_keys(username)
navegador.find_element('xpath','//*[@id="ctl00_ContentPlaceHolderConteudo_TXT_PacienteSenha"]').send_keys(senha)
navegador.find_element('xpath','//*[@id="BTN_PacienteAcesso"]').click()
result = navegador.find_element('xpath','//*[@id="ctl00_ContentPlaceHolderConteudo_GV_Pacientes"]/tbody/tr[5]/td[1]/input')
result.click() 
time.sleep(2)

#Abaixo: Resgata varios valores e salva em uma lista (array)
#results = navegador.find_elements('xpath','//*[@id="ctl00_ContentPlaceHolderConteudo_GV_Pacientes"]/tbody/tr')              
#Abaixo: conta quantos items estão dentro da lista (array)
# qtd = len(results)
# vlrEscolhido = '3'
# resultsEnd = '//*[@id="ctl00_ContentPlaceHolderConteudo_GV_Pacientes"]/tbody/tr['+ vlrEscolhido +']/td[1]/input'
# navegador.find_element('xpath', resultsEnd).click()
# Valor terceiro item da lista -> //*[@id="ctl00_ContentPlaceHolderConteudo_GV_Pacientes"]/tbody/tr[3]/td[1]/input

print('fim')
