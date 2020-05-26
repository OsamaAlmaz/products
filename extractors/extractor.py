import requests
from constants.constant import URL

if __name__ == '__main__':
    re = requests.get(URL)
    if re:
        
