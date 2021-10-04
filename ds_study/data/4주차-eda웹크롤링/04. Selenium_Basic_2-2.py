import pandas as pd 
import time 
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")

print("selenium headless.. 1")
url = "https://finance.naver.com/marketindex/"
driver = webdriver.Chrome("../driver/chromedriver", options=options) 
driver.get(url)
driver.maximize_window()
# driver.set_window_size(1920, 1080) 
time.sleep(3)
print("selenium headless.. 2")

print("selenium headless.. 3")
# 화면 스크롤 하단 이동
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# iframe 태그 지정 
iframe = driver.find_element_by_css_selector("#frame_ex1")
# iframe 태그 이동
driver.switch_to_frame(iframe)
time.sleep(3)

print("selenium headless.. 4")
# 밑 페이지에 있는, 매매기준율 
contents = driver.find_elements_by_css_selector("body > div > table > tbody > tr")

print("selenium headless.. 5")
datas = [] 

for content in contents:
    title = content.find_element_by_css_selector(".tit > a").text
    sale = content.find_element_by_css_selector(".sale").text
    link = content.find_element_by_css_selector(".tit > a").get_attribute("href")
    datas.append({
        "title": title, 
        "sale": sale,
        "link": link
    })
    time.sleep(3)
    print("selenium headless.. for for for")
driver.quit()
df = pd.DataFrame(datas)
df.to_excel("./sel_naver_finance.xlsx", encoding="utf-8")
print("Selenium quit!")
