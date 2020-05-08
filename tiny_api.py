from flask import Flask,jsonify
import requests

# First we get the latest news in Germany with the help of NewsAPI (https://newsapi.org/)
url = ('http://newsapi.org/v2/top-headlines?'
       'country=de&'
       'apiKey=76fb69866b1d42fdb58866ba66f4f45c')
response = requests.get(url)
news_list = response.json()

# then we iterate over them. If the the title does not contain "Corona", we dump it into a JSON-friendly list

json_friendly_news_list = []

for item in news_list["articles"]:
    if 'Corona' not in item["title"]:
        new_news_item = {
            "title": item["title"],
            "content": item["content"],
            "url": item["url"]
        }
        json_friendly_news_list.append(new_news_item)

# finally, we create the API with flask
app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_json():
    return jsonify({"news": json_friendly_news_list})

if __name__ == "__main__":
    app.run(debug=True)
