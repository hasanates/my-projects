from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World fro, Flask!!"

@app.route('/second')
def second():
    return 'ikimci satir mi'

@app.route('/third/subthird')
def third():
    return 'this is the subpage of third page'

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'ID number of this page is {id}'







if __name__ == '__main__':
    app.run(debug=True)