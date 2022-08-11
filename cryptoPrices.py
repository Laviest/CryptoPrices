from bs4 import BeautifulSoup
import requests
import time

BASE_URL = "https://www.coingecko.com"
requests = requests.get(BASE_URL).text
soup = BeautifulSoup(requests, "html.parser")

every_crypto = soup.find("div", class_="position-relative")
trOne = every_crypto.find_all("tr")

def crypto_prices():
    for index, crypto in enumerate(trOne):
        if index != 0:
            coin = crypto.find("span",
                               {"class": "lg:tw-flex font-bold tw-items-center tw-justify-between"}).text.strip()
            coin_shortcut = crypto.find("span", {
                "class": "d-lg-inline font-normal text-3xs tw-ml-0 md:tw-ml-2 md:tw-self-center tw-text-gray-500"}).text.strip()
            coin_price = crypto.find("td", {"class": "td-price price text-right pl-0"}).text.strip()
            last_24hours = crypto.find("td", class_="td-change24h change24h stat-percent text-right col-market").text.strip()
            if '-' in last_24hours:
                print(f"{index}.{coin}({coin_shortcut}) is at {coin_price}. In the last 24 hours it has gone DOWN for {last_24hours} \n")
            else:
                print(f"{index}.{coin}({coin_shortcut}) is at {coin_price}. In the last 24 hours it has gone UP for {last_24hours} \n")


last_hour_list = []
last_hour_coin = []
index = 0


def last_hour_change():
    for crypto in trOne:
        try:
            coin = crypto.find("div", {"class": "tw-flex-auto"}).a.text.strip()
            last_hour = crypto.find("td", class_="td-change1h change1h stat-percent text-right col-market").text.strip()
            if float(str(last_hour).strip(' \t\n\r%')) > 2:
                last_hour_list.append(last_hour)
                last_hour_coin.append(coin)
        except:
            continue


try:
    while True:
        print("************ WHICH PRICES HAVE RAISED OVER 2% IN THE LAST HOUR ************")
        last_hour_change()
        for hour in range(0, len(last_hour_list)):
            print(last_hour_coin[hour] + " has raised for " + str(last_hour_list[hour]).strip())
        last_hour_list = []
        last_hour_coin = []
        print("***************************************************************************")
        time.sleep(3600)
except KeyboardInterrupt:
    print("Stopping the program")

# Need to comment out the first part if we want the second part to work

try:
    while True:
        print("********************************** CRYPTO PRICES TODAY **********************************")
        crypto_prices()
        print("*****************************************************************************************")
        time.sleep(86400)  # 24 hours
except KeyboardInterrupt:
    print("Stopping the program.")



