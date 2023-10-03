from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Leitura do arquivo JSON de configuração
with open('config.json', 'r') as file:
    config = json.load(file)

# Acesso às variáveis
login_insta = config.get('LOGIN_INSTA')
senha_insta = config.get('SENHA_INSTA')
postagem_insta = config.get('POSTAGEM_INSTA')
comentario = config.get('COMENTARIO')

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Criando uma instância do driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Abrir o Instagram
driver.get("https://instagram.com/")
time.sleep(20)

# Fazer login
driver.find_element(by=By.NAME, value="username").send_keys(login_insta)
driver.find_element(by=By.NAME, value="password").send_keys(senha_insta)
driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]').click()   
time.sleep(20)

# Digitar a foto do perfil
driver.get(postagem_insta)
time.sleep(20)

# Função para os comentários
def comentar():
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea').click()
    time.sleep(5)                                      
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea').send_keys(comentario)
    time.sleep(10)                                       
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea').send_keys(Keys.RETURN)

# 1)
comentar()
time.sleep(20)

# 2)
comentar()
time.sleep(25)

# 3)
comentar()
time.sleep(30)

# 4)
comentar()
time.sleep(35)

# 5)
comentar()
time.sleep(40)

# 6)
comentar()
time.sleep(45)

# 7)
comentar()
time.sleep(50)

# 8)
comentar()
time.sleep(55)

# 9)
comentar()
time.sleep(60)

# 10)
comentar()
time.sleep(65)

driver.quit()