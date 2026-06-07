from flask import Flask, request, jsonify
from flask_cors import CORS

# our custom utilities
from utils.repo_loader import clone_repository
from utils.project_detector import detect_project


# initialize flask app
app = Flask(__name__)

# allow frontend (React) to talk to backend
CORS(app)


@app.route("/health")
def health():
    """
    Health check endpoint.

    Used to verify backend is running.
    """

    return jsonify({
        "status": "running",
        "message": "CodeAtlas backend active"
    })


@app.route("/analyze", methods=["POST"])
def analyze_repo():
    """
    Main endpoint for repository analysis.

    Flow:
    frontend sends repo URL
        ↓
    clone repository
        ↓
    analyze structure
        ↓
    return metadata
    """

    try:
        # get JSON body from frontend
        data = request.get_json()

        # extract repo url
        repo_url = data.get("repo")

        # validation
        if not repo_url:
            return jsonify({
                "error": "Repository URL required"
            }), 400

        print("\n========== NEW REPO ==========")
        print(repo_url)
        print("==============================")

        # clone repository locally
        clone_result = clone_repository(repo_url)

        """
        clone_result looks like:

        {
            "repo_name": "fastapi",
            "repo_path": "temp_repos/fastapi"
        }
        """

        # detect project type/framework
        project_info = detect_project(
            clone_result["repo_path"]
        )

        print("\n========== ANALYSIS ==========")
        print(project_info)
        print("==============================\n")

        # send response back to frontend
        return jsonify({
            "success": True,
            "message": "Repository analyzed",

            "repo_name":
                clone_result["repo_name"],

            "repo_path":
                clone_result["repo_path"],

            "analysis":
                project_info
        })

    except Exception as e:
        print("ERROR:", str(e))

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# run flask server
if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001
    )