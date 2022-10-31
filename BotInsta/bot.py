from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

chromedrive_path = ('chromedriver.exe')
webdriver = webdriver.Chrome(executable_path=chromedrive_path)
webdriver.get("https://www.instagram.com/")
sleep(2)

login = webdriver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
login.send_keys('sukitheshitzu')
senha = webdriver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
senha.send_keys('f2cCCO#su8ND&W6y')
button_loggin = webdriver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')
button_loggin.click()
sleep(4)

#nao_botao = webdriver.find_element(By.LINK_TEXT, 'Agora não')
#sleep(3)
#nao_botao.click()
#sleep(5)

hashtag_list = ['python', 'setup', 'sql', 'edcbrasil', 'everydaycarrybrasil', 'sql']

novos_users_seguidos = []

tag = 0
seguindo = 0
likes = 0
comentarios = 0

for hashtag in hashtag_list:
    tag = tag + 1
    sleep(randint(6,7))
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(randint(6,7))
    primeira_thumb = webdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div/div[1]/div[1]/a/div/div[2]')
    sleep(randint(4,5))
    primeira_thumb.click()
    sleep(randint(4,5))
    try:    
        for _ in range(1,10):
            usuario = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a").text

            if usuario not in novos_users_seguidos:
                if webdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').text == 'Seguir':
                    webdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').click()
                    novos_users_seguidos.append(usuario)
                    seguindo = seguindo + 1
                    sleep((2))

                    #like
                    button_like = webdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button')
                    button_like.click()
                    likes = likes + 1
                    sleep(randint(2,4))

                    #comentario
                    webdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[2]/button').click()
                    comment_box = webdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
                    sleep(randint(6,7))
                    com = randint(1, 10)
                    if com < 6:
                        comment_box.send_keys('Top demais!')
                        sleep(2)
                    elif com > 5 and com < 9:
                        comment_box.send_keys('Bom trabalho!')
                        sleep(2)
                    elif com == 9:
                        comment_box.send_keys('show de bola!')
                        sleep(2)
                    elif com == 10:
                        comment_box.send_keys('Great!')
                        sleep(2)
                    comment_box.send_keys(Keys.ENTER)
                    comentarios = comentarios + 1
                    sleep(randint(4,5))
            
                webdriver.find_element(By.NAME, "_ab6-").click()
                sleep(randint(4,5))
            else:
                webdriver.find_element(By.NAME, "_ab6-").click()
                sleep(randint(4,5))
    except:
        continue        
                
    
        
    

print('liked {} fotos' .format(likes))
print('comentarios {} fotos' .format(comentarios))
print('seguindo {} pessoas novas' .format(seguindo))


   


   
        





