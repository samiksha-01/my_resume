from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/cover-letter')
def cover_letter():
    return render_template('cover_letter.html')

if __name__ == '__main__':
    app.run(debug=True)
