import pandas as pd
import time
from selenium import webdriver


# 셀레니움 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("headless")

url = "https://finance.naver.com/marketindex/"
driver = webdriver.Chrome(r"D:\공부\프로젝트\네카라쿠배 - 데이터사이언스 1기\nekalakubae_data_science_1st\ds_study\driver\chromedriver.exe")
driver.get(url)

# 화면 사이즈 조정
driver.set_window_size(1920, 1080)
driver.maximize_window()
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# iframe 이동
frame_ex1 = driver.find_element_by_css_selector("#frame_ex1")
driver.switch_to.frame(frame_ex1)
time.sleep(3)

# 밑 페이지에 있는 매매기준율
contents = driver.find_elements_by_css_selector("body > div > table > tbody > tr")

datas = []

for cont in contents[:6]:
    title = cont.find_element_by_css_selector(".tit").text
    link = cont.find_element_by_css_selector(".tit > a").get_attribute("href")
    sale = cont.find_element_by_css_selector(".sale").text
    print(title, sale, url)
    datas.append({
        "title":title,
        "sale":sale,
        "link":link
    })
    time.sleep(3)

# driver close
driver.close()

# 데이터프레임 생성
df = pd.DataFrame(datas)
df.to_excel(r"D:\공부\프로젝트\네카라쿠배 - 데이터사이언스 1기\nekalakubae_data_science_1st\ds_study\code\sel_naver_finance.xlsx", encoding="utf-8")