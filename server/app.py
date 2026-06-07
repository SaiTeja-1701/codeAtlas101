from flask import (
    Flask,
    request,
    jsonify
)

from flask_cors import CORS

# clone repo utility
from utils.repo_loader import (
    clone_repository
)

# detect framework/project
from utils.project_detector import (
    detect_project
)

# parse python repositories
from parser.python_parser import (
    parse_python_repository
)

#parse mern repo
from parser.mern_parser import (
    parse_mern_repository
)

# initialize flask app
app = Flask(__name__)

# allow React frontend
# to call Flask backend
CORS(app)


@app.route("/health")
def health():
    """
    Simple endpoint
    to verify backend
    is alive.
    """

    return jsonify({
        "status": "running",
        "message":
            "CodeAtlas backend active"
    })


@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze_repo():
    """
    Main repository analysis endpoint.

    Flow:
    ----------
    React frontend
        ↓
    send repo URL
        ↓
    clone repo
        ↓
    detect project
        ↓
    parse repo
        ↓
    return metadata
    """

    try:

        # read frontend request body
        data = request.get_json()

        # get repo URL
        repo_url = data.get(
            "repo"
        )

        # basic validation
        if not repo_url:

            return jsonify({
                "error":
                    "Repository URL required"
            }), 400

        print(
            "\n========== NEW REPO =========="
        )

        print(repo_url)

        print(
            "=============================="
        )

        # ---------------------------------
        # STEP 1:
        # Clone repository
        # ---------------------------------
        clone_result = (
            clone_repository(
                repo_url
            )
        )

        """
        clone_result:

        {
            "repo_name":
                "fastapi",

            "repo_path":
                "temp_repos/fastapi"
        }
        """

        # ---------------------------------
        # STEP 2:
        # Detect project type
        # ---------------------------------
        project_info = (
            detect_project(
                clone_result[
                    "repo_path"
                ]
            )
        )

        print(
            "\n========== PROJECT DETECTED =========="
        )

        print(project_info)

        print(
            "======================================"
        )

        # ---------------------------------
        # STEP 3:
        # Parse python/mern repository
        # ---------------------------------
        parsed_data = []

        if (
            project_info[
                "project_type"
            ] == "python"
        ):

            print(
                "\nParsing Python repository..."
            )

            parsed_data = (
                parse_python_repository(
                    clone_result[
                        "repo_path"
                    ]
                )
            )
        elif(project_info[
                "project_type"
            ] == "mern"
        ):
            print(
                "\nParsing MERN repository..."
            )

            parsed_data = (
                parse_mern_repository(
                    clone_result[
                        "repo_path"
                    ]
                )
            )
        print(
            "\n========== PARSING DONE =========="
        )

        print(
            f"Parsed files: {len(parsed_data)}"
        )

        print(
            "==================================\n"
        )

        # ---------------------------------
        # STEP 4:
        # Send response
        # back to frontend
        # ---------------------------------
        return jsonify({

            "success": True,

            "message":
                "Repository analyzed",

            "repo_name":
                clone_result[
                    "repo_name"
                ],

            "repo_path":
                clone_result[
                    "repo_path"
                ],

            "analysis":
                project_info,

            # limit response
            # to avoid huge payload
            "parsed_files":
                parsed_data[:20]
        })

    except Exception as error:

        print(
            "\nERROR:",
            str(error)
        )

        return jsonify({
            "success": False,
            "error":
                str(error)
        }), 500


# run flask app
if __name__ == "__main__":

    app.run(
        debug=True,
        port=5001
    )