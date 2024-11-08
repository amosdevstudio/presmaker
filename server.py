from gen_pptx import gen_pptx
from flask import Flask, render_template, request, send_file, redirect
import random
import string

app = Flask(__name__)

argument_template = """
{
    "topic": "<topic>"
    "additional-info": "<additional-info>"
    "language": "<mood>"
}
"""


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/presentation/<name>', methods=["GET"])
def get_presentation(name):
    return send_file("./presentations/" + name + ".pptx")


@app.route('/create/', methods=['POST'])
def create():
    data = request.form
    arguments = argument_template \
        .replace("<topic>", data["topic"]) \
        .replace("<additional-info>", data["additional-info"]) \
        .replace("<mood>", data["mood"])
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    path = './presentations/' + name + '.pptx'
    gen_pptx(arguments, path)
    return redirect("/presentation/" + name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
