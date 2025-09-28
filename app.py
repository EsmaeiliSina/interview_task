from flask import Flask, jsonify, request
import requests
from requests.exceptions import RequestException

# creating a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    Handles the root route, returning a simple hello world message.
    """
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

@app.route('/api/<int:book_id>', methods=['GET'])
def get_book_page(book_id):
    """
    Fetches book page information from the Taaghche API.
    """
    try:
        response = requests.get(f"https://get.taaghche.com/v2/book/{book_id}/page", timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        return jsonify(response.json())

    except RequestException as e:
        return jsonify({"error": f"Error fetching data from Taaghche API: {e}"}), 502
    except ValueError:
        return jsonify({"error": "Invalid JSON response from Taaghche API"}), 502


# driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


