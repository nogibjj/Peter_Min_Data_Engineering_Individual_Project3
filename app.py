from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello World!"

@app.route("/random_cs_jokes")
def random_programming_jokes():
    url = "https://v2.jokeapi.dev/joke/Programming"
    response = requests.get(url)
    response = response.json()
    return f'{response["type"]} {response["delivery"]}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)