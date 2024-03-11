from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.nytimes.com/games/connections', verify=False)
bs = BeautifulSoup(res.text, features="html.parser")

with open('./test.txt', '+w') as f:
    f.write(bs.prettify())