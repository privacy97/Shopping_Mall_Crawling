import requests
from bs4 import BeautifulSoup

list1 = [
'수세미',
'도트수세미',
'3M수세미',
'3M옥수수수세미',
'옥수수수세미'
]

list2 = [
'3M공식온라인대리점',
'3M온라인공식판매샵',
'3M온라인공식스토어',
'3M온라인_공식대리점'
]

for i in range(len(list1)):
  print(i+1, end='')
  print('.', list1[i])
  
  url = 'https://browse.auction.co.kr/search?keyword='
  url = url + list1[i]

  response = requests.get(url)

  if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
      
    for j in range(8):
      try:
        try:
          txt1 = '#section--inner_content_body_container > div:nth-child(2) > div:nth-child(' + str(j+1) + ') > div.itemcard > div.section--itemcard > div.section--itemcard_info > div.section--itemcard_info_shop > a > span.text'
          title = soup.select_one(txt1)
          if title is None:
            txt1 = '#section--inner_content_body_container > div:nth-child(2) > div:nth-child(' + str(j+1) + ') > div.itemcard > div > div.section--itemcard_info > div.section--itemcard_info_shop > a > span.img'
            title = soup.select_one(txt1)
          
          temp = title.get_text()
          if temp in list2:
            print('    ', end='')
            print(j+1, end='')
            print(') ', end='')
            print(temp, end=' - ')
            
            txt2 = '#section--inner_content_body_container > div:nth-child(2) > div:nth-child(' + str(j+1) + ') > div.itemcard > div.section--itemcard > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title'
            title = soup.select_one(txt2)
            temp = title.get_text()
            print(temp)
          
        except:
          try:
            txt1 = '#section--inner_content_body_container > div:nth-child(3) > div:nth-child(' + str(j+1) + ') > div.itemcard > div.section--itemcard > div.section--itemcard_info > div.section--itemcard_info_shop > a > span.text'
            title = soup.select_one(txt1)
            if title is None:
              txt1 = '#section--inner_content_body_container > div:nth-child(3) > div:nth-child(' + str(j+1) + ') > div.itemcard > div > div.section--itemcard_info > div.section--itemcard_info_shop > a > span.img'
              title = soup.select_one(txt1)
            
            temp = title.get_text()
            if temp in list2:
              print('    ', end='')
              print(j+1, end='')
              print(') ', end='')
              print(temp, end=' - ')
            
              txt2 = '#section--inner_content_body_container > div:nth-child(3) > div:nth-child(' + str(j+1) + ') > div.itemcard > div.section--itemcard > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title'
              title = soup.select_one(txt2)
              temp = title.get_text()
              print(temp)
          except:
            txt1 = '#section--inner_content_body_container > div:nth-child(4) > div:nth-child(' + str(j+1) + ') > div.itemcard > div.section--itemcard > div.section--itemcard_info > div.section--itemcard_info_shop > a > span.text'
            title = soup.select_one(txt1)
            if title is None:
              txt1 = '#section--inner_content_body_container > div:nth-child(4) > div:nth-child(' + str(j+1) + ') > div.itemcard > div > div.section--itemcard_info > div.section--itemcard_info_shop > a > span.img'
              title = soup.select_one(txt1)
            
            temp = title.get_text()
            if temp in list2:
              print('    ', end='')
              print(j+1, end='')
              print(') ', end='')
              print(temp, end=' - ')
            
              txt2 = '#section--inner_content_body_container > div:nth-child(4) > div:nth-child(' + str(j+1) + ') > div.itemcard > div.section--itemcard > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title'
              title = soup.select_one(txt2)
              temp = title.get_text()
              print(temp)
      except:
        continue
        #print('    ', end='')
        #print(j+1, end='')
        #print(') ', end='')
        #print('Smile_배송')
    print()
  else : 
    print(response.status_code)
