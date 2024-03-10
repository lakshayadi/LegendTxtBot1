from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <img src="https://graph.org/file/13d8c0de8c97b7d295481.png" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""
if __name__ == "__main__":
    app.run()
