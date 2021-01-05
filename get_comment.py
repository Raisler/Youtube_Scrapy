import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox, Chrome
import pandas as pd

video1 = 'https://www.youtube.com/watch?v=5itPFMSxBl8'  # Tudo fica bem
video2 = 'https://www.youtube.com/watch?v=qMt6R88UPkQ' # Pequeninhos
with Chrome() as driver:
    data = []
    wait = WebDriverWait(driver,15)
    driver.get('https://www.youtube.com/watch?v=qMt6R88UPkQ')
        
    for item in range(20):
             
            
        driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(30)

        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#content-text'))):
            data.append(comment.text)                                       
            print(f'--> {comment.text}')

    df = pd.DataFrame(data, columns=['comment'])
    df.to_csv('video2.csv')

