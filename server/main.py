from flask import Flask, jsonify
from functions import generate_all_graphs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/allgraphs', methods=['GET'])
def allgraphs():
    try:
        graphs = generate_all_graphs()
        if 'error' in graphs:
            return jsonify(graphs), 500  # Return error response
        return jsonify(graphs)  # Return the graphs as JSON
    except Exception as e:
        print(f"Error in /api/allgraphs route: {e}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
