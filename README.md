# Open-Proxy
Free proxies that are just checked and updated every 10 minutes

https://working-proxies.amanahlawat.repl.co/

```
import requests

proxy = '[IP]:[Port]'

try:
  r = requests.get(URL, proxies={'http': proxy, 'https': proxy}) #Can also add timeout=3 parameter
  print(r.json())
except:
  pass

```
