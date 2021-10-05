
import pandas as pd
import time 
import requests

from tqdm import tqdm_notebook
from selenium import webdriver
# explicitly wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("headless")

url = "https://store.musinsa.com/app/"
driver = webdriver.Chrome("../driver/chromedriver.exe", options=options)
driver.implicitly_wait(10) # 웹 페이지 전체가 로딩 될 때까지 10초간 대기하고, 10초 안에 페이지 로딩이 완료 되면 다음 코드 실행
driver.get(url)

# 화면 최대화
driver.maximize_window()

# 인기 탭 > 후드 집업
best_link = driver.find_element_by_css_selector("#ui-id-2 > ul:nth-child(1) > li:nth-child(1) > a").get_attribute("href")

# 후드 집업 링크를 새 탭으로 열기
driver.execute_script(f"window.open('{best_link}')")

# 후드 집업 탭으로 이동
driver.switch_to.window(driver.window_handles[1])

# 단독 상품 조건 클릭
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "btn_exclusive"))).click()

# 세일 상품 조건 클릭
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "btn_sale"))).click()

# 최소 금액 설정
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "minPrice"))).send_keys("10000")

# 최대 금액 설정
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "maxPrice"))).send_keys("100000")

# 검색 버튼 클릭
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "btn_price_search"))).click()

# 부모 태그
outers = driver.find_elements_by_css_selector("#searchList > li")

# 전체 데이터 크롤링
datas = []
for outer in tqdm_notebook(outers):
    title = outer.find_element_by_css_selector("p.list_info > a").get_attribute("title")
    price = outer.find_element_by_css_selector("p.price").text.split(" ")[1][:-1]
    link = outer.find_element_by_css_selector("p.list_info > a").get_attribute("href")
    img = outer.find_element_by_css_selector("img").get_attribute("src")
    
    try:sale = outer.find_element_by_css_selector(".icon_new").text.split(" ")[1][:-1]
    except:sale = "0"    
    
    datas.append({
        "title" : title,
        "price" : price,
        "sale" : sale,
        "link" : link,
        "img" : img
    })
    print(f"title:{title} \t|\t price:{price}")
else:
    driver.close()

df = pd.DataFrame(datas)
df.to_excel("./musinsa/musinsa.xlsx", encoding="utf-8")
print("Success save to excel")

# 이미지 다운로드
for idx, rows in tqdm_notebook(df.iterrows()):
    thumb_link = rows["img"]
    response = requests.get(thumb_link)
    name = str(idx) + "_" + rows["title"]
    name = name.replace("/", "" )
    with open(f"./musinsa/{name}.png", "wb") as f:
        f.write(response.content)

# 메인 윈도우 이동
driver.switch_to.window(driver.window_handles[0])
driver.close()
print("작업 종료!!!")
