# Loading Developer Libraries
import json
import logging
import psutil
import subprocess
import os
import sys
import yaml

from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Import market price funtions from scrape.py
from scrape import ethereum_market_price, bitcoin_market_price, litecoin_market_price

# hide logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


# machine payable endpoint (402-endpoint) for json output of ether market data
@app.route('/ether')
@payment.required(5000)
def ether():

	try:
		data = ethereum_market_price()
		response = json.dumps(data, indent=4, sort_keys=True)
		return response
	except ValueError as e:
		return 'HTTP Status 400 {}'.format(e.args[0]), 400


# machine payable endpoint (402-endpoint) for json output of bitcoin market data
@app.route('/bitcoin')
@payment.required(5000)
def bitcoin():

	try:
		data = bitcoin_market_price()
		response = json.dumps(data, indent=4, sort_keys=True)
		return response
	except ValueError as e:
		return 'HTTP Status 400 {}'.format(e.args[0]), 400

# machine payable endpoint (402-endpoint) for json output of litecoin market data
@app.route('/litecoin')
@payment.required(5000)
def litecoin():

	try:
		data = litecoin_market_price()
		response = json.dumps(data, indent=4, sort_keys=True)
		return response
	except ValueError as e:
		return 'HTTP Status 400 {}'.format(e.args[0]), 400

# machine payable endpoint (402-endpoint) for json output for all market data being collected
@app.route('/all')
@payment.required(10000)
def currency():

	try:
		data = ethereum_market_price(), bitcoin_market_price(), litecoin_market_price()
		response = json.dumps(data, indent=4, sort_keys=True)
		return response
	except ValueError as e:
		return 'HTTP Status 400 {}'.format(e.args[0]), 400

if __name__ == '__main__':
    if 'daemon' not in sys.argv:
        pid_file = './scrape.pid'
        if os.path.isfile(pid_file):
            pid = int(open(pid_file).read())
            os.remove(pid_file)
            try:
                p = psutil.Process(pid)
                p.terminate()
            except:
                pass
        try:
            p = subprocess.Popen(['python3', 'currency-server.py', 'daemon'])
            open(pid_file, 'w').write(str(p.pid))
        except subprocess.CalledProcessError:
            raise ValueError("error starting currency-server.py daemon")
    else:
        print ("Server running...")
        print('You had better catch it ... ')
        app.run(host='0.0.0.0', port=8080)