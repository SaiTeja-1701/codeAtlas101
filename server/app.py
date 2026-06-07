from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/analyze", methods=["POST"])
def analyze_repo():
    data = request.get_json()

    repo_input = data.get("repo")

    print("\n========== NEW REPO ==========")
    print(repo_input)
    print("==============================\n")

    return jsonify({
        "success": True,
        "message": "Repo received",
        "repo": repo_input
    })


@app.route("/health")
def health():
    return {
        "status": "running"
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)