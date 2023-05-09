#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data - a list of 100 numbers
data = list(range(100))

# Endpoint to receive a POST request and return a paginated list of numbers
@app.route('/numbers', methods=['POST', 'GET'])
def numbers():
    # Get the pagination parameters from the request body
    page = int(request.json.get('page', 1))
    per_page = int(request.json.get('per_page', 10))
    
    # Calculate the start and end indices for the current page
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    
    # Get the current page of data
    page_data = data[start_index:end_index]
    
    # Create the response object with the page data and pagination metadata
    response = {
        'data': page_data,
        'page': page,
        'per_page': per_page,
        'total': len(data),
        'total_pages': len(data) // per_page + 1
    }
    
    # Return the response as JSON
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5550)