from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

FINNHUB_API_KEY = os.environ.get('FINNHUB_API_KEY')

# Stock Quote
@app.route('/quote')
def get_quote():
    symbol = request.args.get('symbol')
    response = requests.get(
        f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}'
    )
    return jsonify(response.json())

# Earnings Report
@app.route('/earnings')
def get_earnings():
    symbol = request.args.get('symbol')
    response = requests.get(
        f'https://finnhub.io/api/v1/stock/earnings?symbol={symbol}&token={FINNHUB_API_KEY}'
    )
    return jsonify(response.json())

# ETF Holdings
@app.route('/etf-holdings')
def etf_holdings():
    symbol = request.args.get('symbol')
    response = requests.get(
        f'https://finnhub.io/api/v1/etf/holdings?symbol={symbol}&token={FINNHUB_API_KEY}'
    )
    return jsonify(response.json())

# Mutual Fund Profile
@app.route('/mf-profile')
def mf_profile():
    symbol = request.args.get('symbol')
    response = requests.get(
        f'https://finnhub.io/api/v1/mutual-fund/profile?symbol={symbol}&token={FINNHUB_API_KEY}'
    )
    return jsonify(response.json())

# Mutual Fund Holdings
@app.route('/mf-holdings')
def mf_holdings():
    symbol = request.args.get('symbol')
    response = requests.get(
        f'https://finnhub.io/api/v1/mutual-fund/holdings?symbol={symbol}&token={FINNHUB_API_KEY}'
    )
    return jsonify(response.json())

# Key Metrics
@app.route('/key-metrics')
def key_metrics():
    symbol = request.args.get('symbol')
    response = requests.get(
        f'https://finnhub.io/api/v1/stock/metric?symbol={symbol}&metric=all&token={FINNHUB_API_KEY}'
    )
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
