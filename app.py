from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    image_url = "https://graph.org/file/13d8c0de8c97b7d295481.png"
    return f'<img src="{image_url}" alt="Your Image">'

if __name__ == "__main__":
    app.run()
