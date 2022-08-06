import requests

convert_from = input()


cache_to_usd = dict()
response_usd = requests.get("http://www.floatrates.com/daily/usd.json").json()  # get all conversions from USD

cache_to_eur = dict()
response_eur = requests.get("http://www.floatrates.com/daily/eur.json").json()  # get all conversions from EUR

for key in response_usd.keys():
    cache_to_usd[key] = response_usd[key]["inverseRate"]  # stores in cache all conversions to USD
for key in response_eur.keys():
    cache_to_eur[key] = response_eur[key]["inverseRate"]  # stores in cache all conversions to EUR

cache_to_user_input = dict()

while True:
    convert_to = input()
    if convert_to == "":
        break

    amount = input()
    if amount == "":
        break
    amount = float(amount)

    print("Checking the cache...")
    if convert_to == "usd" or convert_to == "eur":
        print("Oh! It is in the cache!")
        if convert_to == "usd":
            result = amount * cache_to_usd[convert_from]
        else:
            result = amount * cache_to_eur[convert_from]
        print("You received {} {}.".format(round(result, 2), convert_to.upper()))
    else:
        if convert_to in cache_to_user_input:
            print("Oh! It is in the cache!")
            result = amount * cache_to_user_input[convert_to]
        else:
            print("Sorry, but it is not in the cache!")
            url_format = "http://www.floatrates.com/daily/{}.json".format(convert_from)
            response_user_input = requests.get(url_format).json()
            result = amount * response_user_input[convert_to]["rate"]
        print("You received {} {}.".format(round(result, 2), convert_to.upper()))
        cache_to_user_input[convert_to] = response_user_input[convert_to]["rate"]

