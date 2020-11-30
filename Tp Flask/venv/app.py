from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    #return "<h3>Hello</H3>" hello en H3
    return render_template('index.html')

@app.route('/<name>')
def hello(name=None):
   return render_template('hello.html',name=name)

@app.route('/api/book')
def book()
    return render_template('book.html')

@app.route('/api/book/<id>')
def bookId(id=None)
    return render_template('bookId.html',id=id)

if __name__=="__main__":
    app.run()
