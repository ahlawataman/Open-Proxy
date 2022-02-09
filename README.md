# Open-Proxy
Free proxies that are just checked and updated every 10 minutes

https://working-proxies.amanahlawat.repl.co/

'''
import requests

proxy = '[IP]:[Port]'

try:
  r = request.get(URL, proxies={'http': proxy, 'https': 'proxy'})
  print(r.json())
except:
  pass
