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
    '한국쓰리엠공식온라인',
    '3M온라인_공식대리점',
    '3M온라인공식판매샵',
    '3M온라인스토어'
]

for i in range(len(list1)):
    print(i+1, end='')
    print('.', list1[i])

    url = 'http://browse.gmarket.co.kr/search?keyword='
    url = url + list1[i]

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            for j in range(8):
                try:
                    txt1 = '#section__inner-content-body-container > div:nth-child(3) > div:nth-child(' + str(
                        j+1) + ') > div.box__item-container > div.box__information > div.box__information_seller > a'
                    title = soup.select_one(txt1)
                    temp = title['title']

                    if temp[0:temp.find(' ')] in list2:
                        print('    ', end='')
                        print(j+1, end='')
                        print(') ', end='')
                        print(temp[0:temp.find(' ')], end=' - ')

                        txt2 = '#section__inner-content-body-container > div:nth-child(3) > div:nth-child(' + str(
                            j+1) + ') > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item'
                        title = soup.select_one(txt2)
                        temp = title['title']
                        print(temp)
                except:
                    try:
                        txt1 = '#section__inner-content-body-container > div:nth-child(2) > div:nth-child(' + str(
                            j+1) + ') > div.box__item-container > div.box__information > div.box__information_seller > a'
                        title = soup.select_one(txt1)
                        temp = title['title']

                        if temp[0:temp.find(' ')] in list2:
                            print('    ', end='')
                            print(j+1, end='')
                            print(') ', end='')
                            print(temp[0:temp.find(' ')], end=' - ')

                            txt2 = '#section__inner-content-body-container > div:nth-child(2) > div:nth-child(' + str(
                                j+1) + ') > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item'
                            title = soup.select_one(txt2)
                            temp = title['title']
                            print(temp)
                    except:
                        txt1 = '#section__inner-content-body-container > div:nth-child(4) > div:nth-child(' + str(
                            j+1) + ') > div.box__item-container > div.box__information > div.box__information_seller > a'
                        title = soup.select_one(txt1)
                        temp = title['title']

                        if temp[0:temp.find(' ')] in list2:
                            print('    ', end='')
                            print(j+1, end='')
                            print(') ', end='')
                            print(temp[0:temp.find(' ')], end=' - ')

                            txt2 = '#section__inner-content-body-container > div:nth-child(4) > div:nth-child(' + str(
                                j+1) + ') > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item'
                            title = soup.select_one(txt2)
                            temp = title['title']
                            print(temp)
            print()
        except:
            print('ERROR')
            print()
    else:
        print(response.status_code)
