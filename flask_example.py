from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home_page():
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(debug=True)
