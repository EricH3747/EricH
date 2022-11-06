import streamlit as st
import requests


def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items) ->list:
    optionList=[]
    for item in items:
        name=item['cityName'][0:3]
        if name in optionList:
            continue
        else:
            optionList.append(name)
    return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county in name:
            specificBookstoreList.append(item)
    return specificBookstoreList

def app():
    bookstoreList=getAllBookstore()
    countyOption=getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    specificBookstore=getSpecificBookstore(bookstoreList, county)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果', num)

if __name__ == '__main__':
    app()



