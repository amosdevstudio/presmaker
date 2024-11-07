from gen_text import gen_text
from flask import Flask, render_template, request

app = Flask(__name__)

argument_template = """
{
    "topic": "<topic>"
    "additional-info": "<additional-info>"
    "mood": "<mood>"
}
"""


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    data = request.form
    arguments = argument_template \
        .replace("<topic>", data["topic"]) \
        .replace("<additional-info>", data["additional-info"]) \
        .replace("<mood>", data["mood"])
    return gen_text(arguments)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
