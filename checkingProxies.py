import requests
import pandas
import concurrent.futures

df = pandas.read_excel('proxy list.xlsx', dtype={'Proxy': object})
proxyList = df['Proxy'].values.tolist()

def extract(proxy):
    try:
        r = requests.get('http://httpbin.org/ip', proxies={'http': proxy, 'https': proxy})
        print(r.json(), ' - working')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxyList)