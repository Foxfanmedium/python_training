# import requests
#
# r = requests.get('http://example.com')
# print(r.text)
#
# url = 'http://example.com'
# par = {'key1':'value1', 'key2':'value2'}
# r = requests.get(url, params=par)
# print(r.url)
#
#
# url = 'http://httpbin.org/cookies'
# cookies = {'cookies_are' : 'working'}
# r = requests.get(url, cookies = cookies) # отправка сформированных куки на сервер
# print(r.text)
#
# print(r.cookies['example_cookies_name']) # использование куки полученных от сервера
#=====================================================================================================================
# import requests
# lines = 0
# with open ('dataset_3378_2.txt', 'r') as site:  # автоматом считываем ссылку из файла
#     site = site.read()\
#         .strip()
#     filo = requests.get(site)
#     for i in filo.text.splitlines():
#         lines += 1
#     print(lines)


import requests

lines = 0
with open('dataset_3378_2.txt', 'r') as site:  # автоматом считываем ссылку из файла
    site = site.readline()
    filo = requests.get(site)
    lenght = len(filo.text.splitlines())
    print(lenght)



