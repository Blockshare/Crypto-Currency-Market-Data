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
from scrape import market_prices

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


@app.route('/market-data')
@payment.required(2500)
def market():

    try:
        data = market_prices()
        response = json.dumps(data, indent=2, sort_keys=True)
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
        app.run(host='0.0.0.0', port=8008)
