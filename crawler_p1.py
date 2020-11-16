
from bs4 import BeautifulSoup
import urllib.request as req

def getMeals (date=input):
    baseURL='http://school.cbe.go.kr/cbs-h/M01050705/list?ymd=2020'
    res=req.urlopen(baseURL+date)
    soup = BeautifulSoup(res,'html.parser')
    meals=soup.find_all(class_='tch-lnc-wrap')
    dic = {}
    for meal in meals:
        # print(repr(meal.dt.text), end="")
        # st = meal.ul.text 
        # st = st.replace ('\r\n', ' ')
        # st = st.replace ('\n', '')
        # print(st,end="")
        
        #meal.dt.text 
        dic.update({meal.dt.text: meal.ul.text})
        #st= meal.ul.text
    return dic 


user_date = input("Enter a date:")
result=getMeals(user_date)
print(result)
