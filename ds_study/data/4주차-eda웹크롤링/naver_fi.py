import pandas as pd 
import time 
from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
driver = webdriver.Chrome()
url = "https://finance.naver.com/marketindex/"
driver.get(url)
driver.set_window_size(1920, 1080)
time.sleep(3)

# 화면 스크롤 하단 이동(화면 이동을 해야 크롤링이 가능한 경우 사용)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# iframe 태그 이동 
iframe = driver.find_element_by_css_selector("#frame_ex1")
driver.switch_to_frame(iframe)
time.sleep(3)

# 데이터가 담긴 부모 태그 선택
contents = driver.find_elements_by_css_selector("body > div > table > tbody > tr")

# 빈 리스트 생성 
datas = [] 

# 제목, 가격, 링크 데이터 데이터 프레임으로 저장
for content in contents[:3]:
    name = content.find_element_by_css_selector("td.tit > a").text
    sale = content.find_element_by_css_selector("td.sale").text
    link = content.find_element_by_css_selector("td.tit > a").get_attribute("href")
    datas.append({
        "name": name, 
        "sale": sale, 
        "link": link
    })
driver.quit()
df = pd.DataFrame(datas)
df.to_excel("./finance.xlsx", encoding="utf-8")
