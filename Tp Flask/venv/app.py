from flask import Flask,render_template,jsonify

app=Flask(__name__)

@app.route('/')
def home():
    #return "<h3>Hello</H3>" hello en H3
    return render_template('index.html')

@app.route('/<name>')
def hello(name=None):
   return render_template('hello.html',name=name)



@app.route('/<bookId>')
def idBook(id ):
    books = json.load(open('books.json'))
    return render_template('book.html', contenu=books[int(id)])

@app.route('/titre/<bookName>')
def titleBook(titre ):
    books = json.load(open('books.json'))
    for i in range(len(books)):
        if books[i]['boobkName'] == bookName:
            return render_template('book.html', contenu = books[i])

if __name__=="__main__":
    app.run()
