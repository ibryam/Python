import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "3FOXLGU2SZJFA663"
NEWS_API_KEY = "12652364f1964416a3165f3018cca851"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,

}

news_params = {
    "apiKey": NEWS_API_KEY,
    # "q":COMPANY_NAME,
    "qInTitle": COMPANY_NAME,


}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

#data_list =  [new_item for item in list]
#list = is a dictionary, we tap into data.items(), this provides the key + the item for each item in data
#out of the result, we only, hence new_item to append to the new data_list list

data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data["4. close"]

print(yesterdays_closing_price)

the_day_before_yesterdays_data = data_list[1]
the_day_before_yesterdays_closing_price = the_day_before_yesterdays_data["4. close"]
print(the_day_before_yesterdays_closing_price)
diff_price = abs(float(yesterdays_closing_price) - float(the_day_before_yesterdays_closing_price))
diff_percentage = (diff_price/float(yesterdays_closing_price))*100

print(diff_percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if diff_percentage > 4:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(articles)



# "Headline: {article_title}. \nBrief: {article_description}"

formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

