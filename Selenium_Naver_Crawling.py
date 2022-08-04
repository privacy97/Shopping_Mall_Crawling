
# 관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


# 키워드 리스트
keyword_list = [
    '빵',
    '식빵',
    '단팥빵',
    '호밀빵'
]

# 업체명 리스트
company_list = [

]


# 크롬드라이버로 원하는 url로 접속
result = None
while result is None:
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        url = 'https://search.shopping.naver.com/search/all?query=a'
        driver = webdriver.Chrome(
            options=options, executable_path=r'C:\\Users\\wjsdnjsrn\\Desktop\\SearchM_Crawling\\Python\\chromedriver_win32\\chromedriver.exe')
        driver.get(url)
        driver.implicitly_wait(1)
        result = driver
    except:
        pass


# selenium 버전 출력
print()
print('Selenium', webdriver.__version__)
print()


# 키워드 입력
for i in range(len(keyword_list)):
    result = None
    while result is None:
        try:
            driver.find_element('class name', 'searchInput_search_input__1Eclz').send_keys(
                Keys.CONTROL + "a")
            driver.find_element(
                'class name', 'searchInput_search_input__1Eclz').send_keys(Keys.DELETE)
            driver.find_element(
                'class name', 'searchInput_search_input__1Eclz').send_keys(keyword_list[i])
            driver.find_element(
                'class name', 'searchInput_search_input__1Eclz').send_keys(Keys.ENTER)
            driver.implicitly_wait(3)
            result = driver
        except:
            continue

    # 키워드 출력
    print(i+1, end='')
    print('.', keyword_list[i])

    # 상품 접근
    result = None
    while result is None:
        try:
            # 스크롤 다운(네이버 특별)
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            # 상품 리스트 div 접근
            products_div = driver.find_element('class name', 'list_basis')
            # 일반 상품 div 저장
            Normal_products = products_div.find_elements(
                'class name', 'basicList_item__2XT81')
            # 광고 상품 div 저장
            Ad_products = products_div.find_elements(
                'class name', 'basicList_item__2XT81.ad')
            driver.implicitly_wait(3)

            if len(Ad_products) >= 1 and len(Normal_products) >= 40:
                result = Ad_products
        except:
            driver.refresh()
            continue

    print('  <일반상품>')
    # 일반 상품 출력
    for j in range(len(Normal_products)):
        result = None
        while result is None:
            try:
                # 회사명 추출
                Normal_company = Normal_products[j].find_element(
                    'class name', 'basicList_mall_title__3MWFY').text
                # 물품명 추출
                Normal_product_name = Normal_products[j].find_element(
                    'class name', 'basicList_link__1MaTN').text
                driver.implicitly_wait(3)
                result = Normal_product_name
            except:
                continue

        # 출력 가공
        if Normal_company[-2::] == '정보':
            Normal_company = Normal_company[0:-2]
        else:
            Normal_company = "<가격비교>"

        if not Normal_company:
            result = None
            while result is None:
                try:
                    Normal_company = Normal_products[j].find_element(
                        'css selector', 'a.basicList_mall__sbVax > img')
                    Normal_company = Normal_company.get_attribute('alt')
                    result = Normal_company
                except:
                    continue

        # 출력
        print('   ', j+1, end='')
        print(')', Normal_company, '-', Normal_product_name)

    print()
    print('  <광고상품>')

    # 광고 상품 출력
    for j in range(len(Ad_products)):
        result = None
        while result is None:
            try:
                # 회사명 추출
                Ad_company = Ad_products[j].find_element(
                    'class name', 'basicList_mall_title__3MWFY').text
                # 물품명 추출
                Ad_product_name = Ad_products[j].find_element(
                    'class name', 'basicList_link__1MaTN').text
                driver.implicitly_wait(3)
                result = Ad_product_name
            except:
                continue

        # 출력 가공
        if Ad_company[-2::] == '정보':
            Ad_company = Ad_company[0:-2]
        else:
            Ad_company = "<가격비교>"

        if not Ad_company:
            result = None
            while result is None:
                try:
                    Ad_company = Ad_products[j].find_element(
                        'css selector', 'a.basicList_mall__sbVax > img')
                    Ad_company = Ad_company.get_attribute('alt')
                    result = Ad_company
                except:
                    continue

        # 출력
        print('   ', j+1, end='')
        print(')', Ad_company, '-', Ad_product_name)
    print()
