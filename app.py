from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <img src="https://media3.giphy.com/media/OT5JXpKLIHzf23BywU/giphy.gif" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""
if __name__ == "__main__":
    app.run()
