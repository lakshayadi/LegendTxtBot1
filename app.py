from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    image_url = "https://example.com/your_image.jpg"
    return f'<img src="{image_url}" alt="Your Image">'

if __name__ == "__main__":
    app.run()
