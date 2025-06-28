from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def frontend():
    return render_template('frontend.html')

if __name__ == '__main__':
    app.run(debug=True)
