import requests

url = "https://api.coinmarketcap.com/data-api/v3/nft/collections?start=0&limit=100"

payload={}
headers = {
  'X-Cmc_pro_api_key': '35ae80bb-79a2-4d53-8a3b-4b8c89e1b1c2',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
