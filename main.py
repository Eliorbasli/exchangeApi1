import requests
import json


def get_exchange(symbol = "EUR", number = 10 , headers={}):
  symbol = "EUR"
  url = "https://api.apilayer.com/exchangerates_data/latest?symbols=&base${symbol}"
  payload = {}
  # headers= {
  #   "apikey": "wgk75GOY6ZqwzGGVzrLH1NxyrHr3kbl3"
  # }
  response = requests.request("GET", url, headers=headers, data = payload)
  status_code = response.status_code
  result = json.loads(response.text)
  x = result["rates"]

  under_number_set = {""}
  for keys , values  in x.items():
    if(values < number ):
      under_number_set.add(keys)

  return(under_number_set)

def main():
  headers= {
    "apikey": "wgk75GOY6ZqwzGGVzrLH1NxyrHr3kbl3"
  }

  print("-----check1------")
  print(get_exchange(number = 10, symbol ="GBP" , headers = headers))
  print("-----check2------")
  print(get_exchange(headers = headers))
  print("-----check3------")
  print(get_exchange(symbol ="EUR",number=20 , headers = headers))


main()