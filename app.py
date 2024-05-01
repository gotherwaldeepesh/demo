from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_func():
    return "<h1> Hello world </h1>"

@app.route('/home')
def my_func2():
    return "<h1> Hello home </h1>"
print('hello')

if __name__ == "__main__":
    app.run()

