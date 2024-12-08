from flask import Flask, render_template
from groq import Groq
import os
import requests

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


@app.route("/", methods=["GET", "POST"])
def index():
    url = "https://v2.jokeapi.dev/joke/Programming"
    response = requests.get(url)
    response = response.json()
    print(response)

    if response["type"] == "single":
        joke_text = f'{response["joke"]}'
    elif response["type"] == "twopart":
        joke_text = f'{response["setup"]} {response["delivery"]}'

    request_text = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Explain this programming joke for me: {joke_text}",
            }
        ],
        model="llama3-8b-8192",
    )
    explanation_answer = request_text.choices[0].message.content
    return render_template(
        "index.html", joke_text=joke_text, explanation_answer=explanation_answer
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
