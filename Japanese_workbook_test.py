#!/usr/bin/env python
# coding: utf-8

# In[ ]:


roading = """
/) /)
*´ㅅ`)/ 필요한 소재를 다운로드 하고 있습니다
"""
main ="""
*゜  (＼ (＼ 
c(⌒(_*´ㅅ`)_ 단어장 연성에 필요한 내용을 입력해 주세요
"""
sub1 ="""
/) /)
*´ㅅ`)/ txt파일을 읽는 중이예요
"""
sub2 ="""
/) /)
*´ㅅ`)/ 사전에서 단어를 찾는 중이예요
"""
sub3 ="""
/) /)
*´ㅅ`)/ excel파일을 만드는 중이예요
"""
ending = """
　　　　　　　　　| 
　　　　　　　　　| 
　　　end 　　　 ﾉ/) /)
　　　　　　　 ／/*´ㅅ`) 
　　　　　　／　/   ⊂ノ 
 　　　　　　＼ /ーーJ 
 ￣￣￣￣￣￣￣
 
 
 
 ---------------------------------------------------------------------------------------------------------------
 """


# In[ ]:


print(roading)

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import random
import re

print(main)

while True:
    filename = str(input("txt파일 이름 입력 >>>>  "))
    excel_save = str(input("xlsx파일 이름 입력 >>>>  "))
    num = int(input("문제 개수 입력 >>>>  "))
    list_re = []

    print(sub1)

    f = open(filename+'.txt', 'r', encoding='utf-8')
    file = f.readlines()
    file = random.sample(file,num)

    print(sub2)

    for i in range(0, len(file)):
        word = file[i].strip('\n')

        s = requests.Session()
        dict_page = "https://dict.naver.com/search.nhn?dicQuery=" + word
        html = ""
        resp = s.get(dict_page)
        if resp.status_code == 200:
            html = resp.text
        soup = bs(html, 'html.parser')

        result1, result2, result11 = ''

        # 일본어
        try:
            result1 = soup.find('div', {'class': 'jp_dic_section search_result dic_jp_entry'})                 .find('dl', {'class': 'dic_search_result'}).find('dd')                .find('sup', {'class': 'huri'}).previous_sibling.get_text()
            result11 = re.sub('[0-9\s. ]','',result1)

            result2 = soup.find('div', {'class': 'jp_dic_section search_result dic_jp_entry'})                     .find('dl', {'class': 'dic_search_result'}).find('dd')                    .find('sup', {'class': 'huri'}).get_text()

        except:
            result11 += '음(훈)독을 찾지 못했습니다'
            result2 += '한자를 찾지 못했습니다'

        list_re.append([result11,result2, word])

    print(sub3)

    df = np.array(list_re).reshape(len(list_re),3)
    df = pd.DataFrame(df)
    df.to_excel(excel_save+'.xlsx')

    print(ending)

