from flask import Flask, render_template, request, redirect, url_for, abort
import requests, json, pprint

# Logic
app = Flask(__name__, static_path='/static')

# application wide definitions


@app.route('/')
def index():
    return render_template('index.html', landing=True)

@app.route('/summoner', methods=['GET', 'POST'])
def summoner():
    error = False
    bad_name = False
    if request.method == 'POST':
        user_name = request.form['name']
        payload = {'api_key': 'b0afea27-1602-4ed8-aff5-24caf6bbb2d1'}

        # attempt to query the riot games api for the summoner basic info
        s_info = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}".format(user_name), params=payload) #format the API request URL
        if s_info.status_code == 200:
            print("SUCCESS! The summoner {} was found!".format(user_name))
            error = False
        else:
            print("ERROR The summoner {} was not found!".format(user_name))
            error = True

        return render_template('summoner.html', summoner=request.form['name'], failure=error)

@app.route('/status', methods=['GET', 'POST'])
def status():
    error = False
    bad_name = False
    if requests.method == 'POST':
        server_name = request.form['name']
        payload = {'api_key': 'e3ab974f-7a2f-417c-b31d-78c86c1dd190'}
        
        # attempt to query the riot games api for the status of requested server
        s_info = requests.get("http://status.leagueoflegends.com/shards/{}".format(server_name), params = payload)
        if s_info.status_code == 200:
            print("The server {} is currently online!".format(server_name))
            error = False
        else:
            print("ERROR The server {} is currently down, or does not exist. Please check case and spelling.".format(server_name))
            error = True
        
        return render_template('status.html', status=request.form['name'], failure=error)

if __name__ == '__main__':
    app.run(debug=True)
