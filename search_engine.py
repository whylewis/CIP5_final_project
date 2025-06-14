import requests
import datetime
import json
import os

API_BASE_URL = "https://newsapi.org/v2/everything"
API_KEY = os.getenv('NEWS_API_KEY')
# sign up at https://newsapi.org for a free API key
# Windows: open Command Prompt and type>> setx NEWS_API_KEY "your_api_key_here"
# Mac/Linux: open Terminal and type>> export NEWS_API_KEY="your_api_key_here"

def get_yesterday():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    formatted_yesterday = yesterday.strftime("%y-%m-%d")
    return formatted_yesterday

def get_today():
    today = datetime.date.today()
    formatted_today = today.strftime("%y-%m-%d")
    return formatted_today

def search_articles(search_term, formatted_yesterday, formatted_today):
    params = {
        "q":search_term, "apiKey":API_KEY, 
        "from":formatted_yesterday, 
        "to":formatted_today, 
        "language":"en", 
        "sortBy":"publishedAt"
        }
    response = requests.get(API_BASE_URL, params)
    return response.json()

def display_result(search_result, formatted_yesterday, formatted_today):
    articles = search_result["articles"]

    if articles:
        print(f"Total of {len(articles)} article(s) have found from {formatted_yesterday} to {formatted_today}:\n")
        for article in articles:
            article_source = article["source"]["name"]
            article_title = article["title"]
            article_description = article["description"]
            article_url = article["url"]
            article_date = article["publishedAt"]
            
            print(f"{article_title} || {article_source} || {article_date}\n[Summary] {article_description}\nTo read more, please visit: {article_url}\n")
            print("===============================================================================================================\n")
    else:
        print("No article found.\n")

def main(): 
    yesterday = get_yesterday()
    today = get_today()

    while True:
        search_term = input("Type a keyword to search: ")
        while search_term == "":
            search_term = input("Invalid keyword. Type a keyword to search: ")
        search_result = search_articles(search_term, yesterday, today)
        display_result(search_result, yesterday, today)

if __name__ == "__main__":
    main()