from flask import Flask, render_template, request
import requests
import newspaper
from keys import API_KEY
from datetime import datetime, timedelta



app = Flask(__name__)
search_page_number = 1
key_word = 'india'
start = datetime.today()
end = start - timedelta(days=7)
source = 'the-times-of-india'
source_page_number = 1

def add_content(response):
    for result in response["articles"]:
        text = ''
        try:
            article = newspaper.Article(result["url"])
            article.download()
            article.parse()
            text = article.text
        except:
            text = "Content is not provided by the site.🤕"

        result['content'] = text

@app.route("/")
def index():
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url).json()
    add_content(response)
    # print(response)
    return render_template('index.html', results=response["articles"])


@app.route('/search', methods=["GET", "POST"])
def search():
    global search_page_number, key_word
    has_prev_page = True
    has_next_page = True

    if request.method == "POST":
        if request.form.get('search_key') is not None:
            search_page_number = 1
            key_word = request.form.get('search_key')
                

        if request.form.get('prev'):
            search_page_number -= 1
        if request.form.get('next'):
            search_page_number += 1

        url = f'https://newsapi.org/v2/everything?q={key_word}&apiKey={API_KEY}&language=en&pageSize=10&page={search_page_number}&from={end}&end={start}&sortBy=publishedAt'
        response = requests.get(url).json()
        add_content(response)

    else:
        search_page_number = 1
        url = f'https://newsapi.org/v2/everything?q={key_word}&apiKey={API_KEY}&language=en&pageSize=10&page={search_page_number}&from={end}&end={start}&sortBy=publishedAt'
        response = requests.get(url).json()
        add_content(response)

    if search_page_number == 1:
        has_prev_page = False
    if search_page_number >= 10:
        has_next_page= False
        
    return render_template('search.html', results=response["articles"], page_number=search_page_number, has_prev_page=has_prev_page, has_next_page=has_next_page)

@app.route('/sources', methods=['GET', 'POST'])
def sources():
    global source, source_page_number
    has_prev_page = True
    has_next_page = True
    if request.method == "POST":

        if request.form.get("source_id"):
            source_page_number = 1
            source = request.form.get("source_id")
        
        if request.form.get("prev"):
            source_page_number -= 1
        if request.form.get('next'):
            source_page_number += 1

        url = f'https://newsapi.org/v2/everything?sources={source}&language=en&apiKey={API_KEY}&pageSize=10&page={source_page_number}&from={end}&end={start}&sortBy=publishedAt'
        response = requests.get(url).json()
        add_content(response)

        if source_page_number == 1:
            has_prev_page = False
        if source_page_number >= 10:
            has_next_page = False

    return render_template('sources.html', results=response['articles'], page_number=source_page_number, has_prev_page=has_prev_page, has_next_page=has_next_page)

if __name__ == "__main__":
    app.run(debug=True)
