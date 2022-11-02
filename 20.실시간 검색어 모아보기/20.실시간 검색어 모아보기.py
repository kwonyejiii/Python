#!/usr/bin/env python
# coding: utf-8

# 시그널(네이버 실시간검색사이트)

# In[2]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)


# In[7]:


from selenium import webdriver
URL = 'https://signal.bz/news'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

naver_results = driver.find_elements_by_css_selector('#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div > div > a > span.rank-text')


# In[8]:


naver_results


# In[9]:


for naver_list in naver_results:
    print(naver_list.text)


# In[ ]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.google.co.kr'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

naver_results = driver.find_elements_by_css_selector('')

