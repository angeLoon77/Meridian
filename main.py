from flask import Flask, jsonify
from service import analyze_ticker

app = Flask(__name__)

@app.route("/api/analysis/<ticker>")
def analysis(ticker):
    try:
        result = analyze_ticker(ticker)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run(debug=True)