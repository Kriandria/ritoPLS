from flask import Flask, render_template, request, abort
import requests, json, pprint

# Logic
app = Flask(__name__, static_path='/static')

@app.route('/')
def index():
    return render_template('index.html', landing=True)

@app.route('/summoner', methods=['POST'])
def summoner():
	return render_template('summoner.html')


if __name__ == '__main__':
    app.run(debug=True)
