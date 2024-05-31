from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def selenium_script(x,y,z):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https:www.google.com")
    driver.maximize_window()

    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
    )

    input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
    input_element.clear()
    input_element.send_keys("instagram" + Keys.ENTER) 



    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"instagram"))
    )

    link = driver.find_element(By.PARTIAL_LINK_TEXT,"instagram")
    link.click()



    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"_aa48"))
    )


    name = driver.find_element(By.CLASS_NAME,"_aa48")
    name.send_keys(x)


    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//label[@class='_aa48']"))
    )

    password = driver.find_element(By.XPATH, "//label[@class='_aa48']")
    password.send_keys(y)


    WebDriverWait(driver,10).until(
        
        EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button'))
        
    )

    login_button =driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
    driver.execute_script("arguments[0].click();",login_button)
    sleep(10)


    not_now =driver.find_element(By.CLASS_NAME,"_ac8f")
    not_now.click()
    sleep(12)



    not_now_2 = driver.find_element(By.XPATH,"//div[contains(@class, '_a9-z')]//button[2]").click()
    sleep(10)




    search_box = driver.find_element(By.XPATH,'//span[@class="x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j" and @aria-describedby=":r3:"]')
    search_box.click()
    sleep(16)

    account_name = driver.find_element(By.CSS_SELECTOR,'input[aria-label="Search input"]')
    account_name.send_keys(z)


    sleep(10)

    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//div[@class='x6s0dn4 x78zum5 xdt5ytf x5yr21d x1odjw0f x1n2onr6 xh8yej3']//a[@href='/{z}/']"))
    )
    element.click()

    #fuck_element = driver.find_element(By.XPATH,f"//div[@class='x6s0dn4 x78zum5 xdt5ytf x5yr21d x1odjw0f x1n2onr6 xh8yej3']//a[@href='/{z}/']")


    #fuck_element.click()
    sleep(12)
    

    post = driver.find_element(By.CLASS_NAME,"_aagw")
    post.click()
    sleep(8)


    for _ in range(3):

        '''like_button = driver.find_element(By.CSS_SELECTOR,"svg.x1lliihq.x1n2onr6.xyb1xck")'''


        like_button = driver.find_element(By.CSS_SELECTOR,"span.x1rg5ohu.xp7jhwk > div.x1i10hfl.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xcdnw81")

        like_button.click()
        
        sleep(5)
       

        comment_button = driver.find_element(By.CSS_SELECTOR ,"svg.x1lliihq.x1n2onr6.x5n08af[aria-label='Comment'][role='img']")

        comment_button.click()

        sleep(2)
    
            # Wait until the text field is present and visible
        text_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]'))
            )

            # Input text into the text field
        text_field.send_keys('This is a test comment.')

        sleep(3)

            # Optionally, submit the form or perform other actions

        submit = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'x1i10hfl') and contains(@class, 'xjqpnuy') and contains(@class, 'xa49m3k') and contains(@class, 'xqeqjp1') and contains(@class, 'x2hbi6w') and contains(@class, 'xdl72j9') and contains(@class, 'x2lah0s') and contains(@class, 'xe8uvvx') and contains(@class, 'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'x2lwn1j') and contains(@class, 'xeuugli') and contains(@class, 'x1hl2dhg') and contains(@class, 'xggy1nq') and contains(@class, 'x1ja2u2z') and contains(@class, 'x1t137rt') and contains(@class, 'x1q0g3np') and contains(@class, 'x1lku1pv') and contains(@class, 'x1a2a7pz') and contains(@class, 'x6s0dn4') and contains(@class, 'xjyslct') and contains(@class, 'x1ejq31n') and contains(@class, 'xd10rxx') and contains(@class, 'x1sy0etr') and contains(@class, 'x17r0tee') and contains(@class, 'x9f619') and contains(@class, 'x1ypdohk') and contains(@class, 'x1f6kntn') and contains(@class, 'xwhw2v2') and contains(@class, 'xl56j7k') and contains(@class, 'x17ydfre') and contains(@class, 'x2b8uid') and contains(@class, 'xlyipyv') and contains(@class, 'x87ps6o') and contains(@class, 'x14atkfc') and contains(@class, 'xcdnw81') and contains(@class, 'x1i0vuye') and contains(@class, 'xjbqb8w') and contains(@class, 'xm3z3ea') and contains(@class, 'x1x8b98j') and contains(@class, 'x131883w') and contains(@class, 'x16mih1h') and contains(@class, 'x972fbf') and contains(@class, 'xcfux6l') and contains(@class, 'x1qhh985') and contains(@class, 'xm0m39n') and contains(@class, 'xt0psk2') and contains(@class, 'xt7dq6l') and contains(@class, 'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, 'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, 'x1n2onr6') and contains(@class, 'x1n5bzlp') and contains(@class, 'x173jzuc') and contains(@class, 'x1yc6y37')]")))

        submit.click()
        sleep(5)


        next_button = driver.find_element(By.XPATH,"//div[contains(@class,' _aaqg _aaqh')]")
        next_button.click()
        sleep(4)


    driver.quit()

