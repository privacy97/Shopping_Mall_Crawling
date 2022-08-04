
# 관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


# 키워드 리스트
keyword_list = [
  
]

# 업체명 리스트
company_list = [
  
]


# 크롬드라이버로 원하는 url로 접속
# 블루투스 오류
result = None
while result is None:
  try:
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    url = ''
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\Users\wjsdnjsrn\Desktop\\Git_Hub\Shopping_Mall_Crawling\\chromedriver_win32\\chromedriver.exe')
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
      driver.find_element('class name', '').send_keys(Keys.CONTROL + "a")
      driver.find_element('class name', '').send_keys(Keys.DELETE)
      driver.find_element('class name', '').send_keys(keyword_list[i])
      driver.find_element('class name', '').send_keys(Keys.ENTER)
      driver.implicitly_wait(3)
      result = driver
    except:
      continue
  
  
  # 키워드 출력
  print(i+1, end='')
  print('.', keyword_list[i])
  
  
  # 광고물(AD) 접근 함수
  result = None
  while result is None:
    try:
      # 광고틀 div 접근
      ad_div = driver.find_element('class name', '')
      # 상품 div 저장
      products = ad_div.find_elements('class name', '')
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
        company = products[i].find_element('class name', '').text
        # 물품명 추출
        product_name = products[i].find_element('class name', '').text
        driver.implicitly_wait(3)
        result = product_name
      except:
        continue
    
    
    # 일치하는 회사, 물품 출력
    if company in company_list:
      print('   ',i+1, end='')
      print(')', company, '-', product_name)
  print()