from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.repo_loader import clone_repository

app = Flask(__name__)
CORS(app)


@app.route("/health")
def health():
    return {
        "status": "running"
    }


@app.route("/analyze", methods=["POST"])
def analyze_repo():
    try:
        data = request.get_json()

        repo_url = data.get("repo")

        if not repo_url:
            return jsonify({
                "error": "Repository URL required"
            }), 400

        result = clone_repository(repo_url)

        return jsonify({
            "success": True,
            "message": "Repository cloned",
            "repo_name": result["repo_name"],
            "repo_path": result["repo_path"]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001
    )