from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

FINNHUB_API_KEY = "your_api_key_here"

@app.route('/quote', methods=['GET'])
def quote():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Missing 'symbol' parameter"}), 400

    response = requests.get(
        'https://finnhub.io/api/v1/quote',
        params={
            'symbol': symbol,
            'token': FINNHUB_API_KEY
        }
    )

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
