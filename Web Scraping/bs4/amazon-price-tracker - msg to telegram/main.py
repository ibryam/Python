import requests
from bs4 import BeautifulSoup
import lxml

base_site = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.de/-/en/AmazonBasics-Carry-On-Travel-Backpack-Black/dp/B01J24H2K0/?_encoding=UTF8&pd_rd_w=5C4qU&content-id=amzn1.sym.cd6be068-7dfd-4c5d-9b78-b50b0cc58556%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=cd6be068-7dfd-4c5d-9b78-b50b0cc58556&pf_rd_r=3VZCMQJJ8X6RS3Z58QVD&pd_rd_wg=byKrL&pd_rd_r=18c40f2e-3216-41eb-b086-7fe1f89fdfc4&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1"

# Full headers would look something like this
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.9,bg;q=0.8,tr;q=0.7",
#     "Dnt": "1",
#     "Priority": "u=0, i",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
# }



r = requests.get(base_site, headers=header)

soup = BeautifulSoup(r.content, "lxml")

# hold on the price element by using class and get the text
price = soup.find(class_="a-offscreen")

#get text of class_element
price = price.getText()

# remove dollar sign and convert to a floating number
price = float(price.split("$")[1])

print(price)