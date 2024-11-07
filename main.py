from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<p>Hello World</p>'

@app.route('/test')
def test():
    return '<p>test</p>'


if __name__ == "__main__":
    app.run(debug=True)
