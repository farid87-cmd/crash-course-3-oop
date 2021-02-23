import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Succsess Response = {response.status_code}')
        #print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'hasil pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'WOOPS, ada kesalahan request {response.status_code}')
except Exception as e:
    print(f'ADA ERROR!!, {e}')
print('Program Ended')

