from flask import Flask, jsonify, request


app = Flask(__name__)

# Define a list of data
data_list = [
{"id": 1, "name": "John", "age": 25},
{"id": 2, "name": "Jane", "age": 30},
{"id": 3, "name": "Bob", "age": 35},
]
@app.route("/")
def index():
    return "Welcome to the API!"

@app.route("/search")
def search():
    # Get the search query from the URL parameter
    query = request.args.get("person")
    # Find the matching element in the data list
    for data in data_list:
        if data["name"] == query:
            return jsonify(data)
# Return an error message if no matching element is found
    return jsonify({"error": "No matching data found."}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)