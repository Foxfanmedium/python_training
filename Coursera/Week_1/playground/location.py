import requests


def get_location_info():
    return requests.get("http://freegeoip.net/json/").json()


print(get_location_info())


# if __name__ == "__main__":
#     print(get_location_info)



