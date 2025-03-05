from flask import Flask, json, render_template, redirect, request, abort, jsonify
from api_requests import status_win_time, all_api_date

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/index')
def home():
    return render_template("index.html", dates=all_api_date())


@app.route("/api/date/<date>")
def api_get_matrix(date):
    return jsonify(status_win_time(date))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


