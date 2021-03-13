# importar biblioteca
from selenium import webdriver # importa para navegar no navegador
import time # importa o delay
from webdriver_manager.chrome import ChromeDriverManager # simula sem baixa dependecia
from selenium.webdriver.common.keys import Keys
# navegar no wats
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') 
time.sleep(45)
#definir contato e grupos e mensagem
contatos = ['Alex']
mensagem = 'alex desculpa eu não te responder mas foi por uma boa causa eu estava fazendo um bot em pyton e essa mensagem vai ser envida via bot pq pra grava video demora mto'

# busca contato ou grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# campo de pesquisa "copyable-text selectable-text"
# campo de mensagem "copyable-text selectable-text"
# envia mensagem
