
# step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd


# step2. 키워드, 업체명 리스트
keyword = str(input())


# step3.크롬드라이버로 원하는 url로 접속
result = None
while result is None:
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        url = 'https://search.shopping.naver.com/search/all?query=a'
        driver = webdriver.Chrome(options=options, executable_path=r'C:\\Development\\Thesis\\main\\chromedriver_win32\\chromedriver.exe')
        driver.get(url)
        driver.implicitly_wait(1)
        result = driver
    except:
        pass


# selenium 버전 출력
print()
print('Selenium', webdriver.__version__)
print()


# 키워드 입력 함수
result = None
while result is None:
    try:
        driver.find_element('class name', 'searchInput_search_input__vLBeq').send_keys(
            Keys.CONTROL + "a")
        driver.find_element(
            'class name', 'searchInput_search_input__vLBeq').send_keys(Keys.DELETE)
        driver.find_element(
            'class name', 'searchInput_search_input__vLBeq').send_keys(keyword)
        driver.find_element(
            'class name', 'searchInput_search_input__vLBeq').send_keys(Keys.ENTER)
        driver.implicitly_wait(3)
        result = driver
    except:
        continue


# 키워드 출력
print(keyword)


# 상품 접근 함수
result = None
while result is None:
    try:
        # 스크롤 다운(네이버 특별)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        # 상품 div 접근
        products_div = driver.find_element('class name', 'list_basis')
        # 일반상품 div
        general_products = products_div.find_elements('class name', 'basicList_item__0T9JD')
        # 광고상품 div
        ad_products = products_div.find_elements('class name', 'basicList_item__0T9JD.ad')
        driver.implicitly_wait(3)

        if len(general_products) >= 40:
            result = general_products
        else:
            driver.refresh()
    except:
        driver.refresh()
        continue


# 상품 출력 함수
def product_print(products):

    # 상품 리스트
    products_list = []

    # 상품 개수 만큼 반복
    for k in range(len(products)):
        result = None
        while result is None:
            try:
                # 회사명 추출
                company = products[k].find_element('class name', 'basicList_mall_title__FDXX5').text
                if (company[-2:] == '정보'):
                    company = company[:-2]

                # 물품명 추출
                product_name = products[k].find_element('class name', 'basicList_link__JLQJf').text
                driver.implicitly_wait(3)
                result = product_name
            except:
                continue
        
        # 상품 카테고리 추출
        result = None
        while result is None:
            try:
                product_category = products[k].find_elements('class name', 'basicList_category__cXUaZ.basicList_nohover__TJr2_')
                driver.implicitly_wait(3)
                result = product_category
            except:
                continue

        # 상품 카테고리 저장
        category = ''
        for j in range(len(product_category)):
            category = category + product_category[j].text
            if j != (len(product_category)-1):
                category = category + ' > '

        
        # json 형식 저장
        products_list.append(
            {
                "company" : company,
                "product_name" : product_name,
                "category" : category
            }
        )
    
    for i in products_list:
        print(i)

    # 결과값 반환
    return products_list



print('AD 상품')
print(product_print(ad_products))
print()


print('일반 상품')
print(product_print(general_products))
print()

