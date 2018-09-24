import time
from logging import INFO

import numpy as np
from flask import Flask, request

import config

app = Flask(__name__)
app.logger.setLevel(INFO)


@app.route('/mirror/headers')
def mirror():
    app.logger.info(f'Mirror headers received:\n{request.headers}')
    return str(request.headers)


@app.route('/wait/lognormal')
def wait_lognormal():
    sleep_time = get_lognormal_response_time()
    app.logger.info(f'Wait lognormal - Response time:\n{sleep_time}')
    time.sleep(sleep_time)
    return f'{str(sleep_time)}s'


@app.route('/response/<int:response_code>')
def choose_response(response_code):
    return str(request), response_code


@app.route('/log')
def log():
    app.logger.info(f'Headers:\n{request.headers}\n--------\n{request.get_json}')
    return 'Ok'


def get_lognormal_response_time(mu=config.lognormal_mu, sigma=config.lognormal_sigma):
    return int(np.random.lognormal(mu, sigma, 1)[0])/1000.0


def get_random_status_code(weight_codes=config.status_code_weight):
    return int(np.random.choice(list(weight_codes.keys()),
                                size=1,
                                p=list(weight_codes.values()))[0])


if __name__ == '__main__':
    app.run()
