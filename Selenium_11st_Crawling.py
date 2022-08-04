
# step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


# step2. 키워드, 업체명 리스트
keyword_list = [
    '빵',
    '식빵',
    '단팥빵',
    '호밀빵'
]

company_list = [

]


# step3.크롬드라이버로 원하는 url로 접속
result = None
while result is None:
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        url = 'https://www.11st.co.kr/main'
        driver = webdriver.Chrome(
            options=options, executable_path=r'C:\\Users\\wjsdnjsrn\\Desktop\\SearchM_Crawling\\Python\\chromedriver_win32\\chromedriver.exe')
        driver.get(url)
        driver.implicitly_wait(3)
        result = driver
    except:
        pass


# selenium 버전 출력
print()
print('Selenium', webdriver.__version__)
print()


# 키워드 입력 함수
for i in range(len(keyword_list)):
    result = None
    while result is None:
        try:
            # 검색어 입력
            driver.find_element('class name', 'search_text').send_keys(
                Keys.CONTROL + "a")
            driver.find_element(
                'class name', 'search_text').send_keys(Keys.DELETE)
            driver.find_element(
                'class name', 'search_text').send_keys(keyword_list[i])
            driver.find_element(
                'class name', 'search_text').send_keys(Keys.ENTER)
            driver.implicitly_wait(3)
            result = driver
        except:
            continue

    # 검색어 출력
    print(i+1, end='')
    print('.', keyword_list[i])

    print('  <포커스클릭>')

    # 광고물(AD) 접근 함수
    result = None
    while result is None:
        try:
            # 광고틀 div 접근
            ad_div = driver.find_element(
                'class name', 'c_listing.c_listing_view_type_list')
            # 상품 div 저장
            products = ad_div.find_elements('class name', 'c_card.c_card_list')
            driver.implicitly_wait(3)
            result = products
        except:
            continue

    # 상품 개수 만큼 반복
    for i in range(len(products)):
        result = None
        while result is None:
            try:
                # 회사명 추출
                company = products[i].find_element('class name', 'name').text
                # 물품명 추출
                product_name = products[i].find_element(
                    'class name', 'c_prd_name.c_prd_name_row_1').text
                driver.implicitly_wait(3)
                result = product_name
            except:
                continue

        print('   ', i+1, end='')
        print(')', company, '-', product_name)
    print()
