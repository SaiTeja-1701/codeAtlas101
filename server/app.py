from flask import (
    Flask,
    request,
    jsonify
)

from flask_cors import CORS

from features.repository_analysis import (
    analyze_repository
)

from utils.vector_memory import (
    vector_store
)

from features.qa import (
    ask_repository
)

from features.docs import (
    generate_docs
)

from features.docs import (
    generate_docs
)

app = Flask(__name__)
CORS(app)


@app.route("/health")
def health():
    """
    Check backend status.
    """

    return jsonify({
        "status": "running",
        "message":
            "CodeAtlas backend active"
    })


def validate_repo_input(
    repo_url
):
    """
    Validate repo URL input.
    """

    if not repo_url:

        return (
            jsonify({
                "error":
                    "Repository URL required"
            }),
            400
        )

    return None


@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze_repo():
    """
    Analyze repository endpoint.
    """

    try:

        data = (
            request.get_json()
        )

        repo_url = data.get(
            "repo"
        )

        validation = (
            validate_repo_input(
                repo_url
            )
        )

        if validation:
            return validation

        print(
            "\n========== NEW REPO =========="
        )

        print(repo_url)

        print(
            "=============================="
        )

        # full analysis pipeline
        result = (
            analyze_repository(
                repo_url
            )
        )

        return jsonify({
            "success": True,

            "message":
                "Repository analyzed",

            "repo_name":
                result[
                    "repo_name"
                ],

            "repo_path":
                result[
                    "repo_path"
                ],

            "analysis":
                result[
                    "analysis"
                ],

            "parsed_files":
                result[
                    "parsed_files"
                ][:20],

            "chunks":
                result[
                    "chunks"
                ][:20]
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

@app.route(
    "/ask",
    methods=["POST"]
)
def ask_repo():
    """
    Ask repository questions.
    """

    try:

        data = (
            request.get_json()
        )

        question = data.get(
            "question"
        )

        if not question:

            return jsonify({
                "error":
                    "Question required"
            }), 400

        result = (
            ask_repository(
                question
            )
        )

        return jsonify({
            "success": True,

            "question":
                question,

            "answer":
                result["answer"],

            "retrieved_chunks":
                result[
                    "retrieved_chunks"
                ]
        })

    except Exception as error:

        return jsonify({
            "error":
                str(error)
        }), 500

@app.route(
    "/generate-docs",
    methods=["POST"]
)
def docs_route():
    """
    Generate repository docs.
    """

    try:

        result = (
            generate_docs()
        )

        return jsonify(
            result
        )

    except Exception as error:

        return jsonify({
            "error":
                str(error)
        }), 500

@app.route(
    "/generate-docs",
    methods=["POST"]
)
def generate_docs_route():
    """
    Generate AI docs.
    """

    try:

        result = (
            generate_docs()
        )

        return jsonify(
            result
        )

    except Exception as error:

        return jsonify({
            "error":
                str(error)
        }), 500

if __name__ == "__main__":

    app.run(
        debug=True,
        use_reloader=False,
        port=5001
    )