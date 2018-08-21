"""
Запуск через командную строку
$ python "10_exceptions in requests.py" https://github.com
"""

import requests
import sys

url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

except requests.Timeout:
    print("ошибка timeout, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("ошибка url: (0), (1)".format(url, code))
except requests.RequestException:
    print("ошибка скачивания url:", url)
else:
    print(response)






# url = "https://github.com"
# response = requests.get(url)
# print(response)











