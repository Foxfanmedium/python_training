import requests

def get_location_info():
    return requests.get("https://ipstack.com/").json()


if __name__ == '__main__':
    print(get_location_info)


