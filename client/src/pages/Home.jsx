import { useState } from "react";
import axios from "axios";

function Home() {
  // repository URL input
  const [repoUrl, setRepoUrl] =
    useState("");

  // repo analyzed status
  const [repoAnalyzed,
    setRepoAnalyzed] =
    useState(false);

  // loading state
  const [loading,
    setLoading] =
    useState(false);

  // user question
  const [question,
    setQuestion] =
    useState("");

  // AI answer
  const [answer,
    setAnswer] =
    useState("");

  // analyze repository
  const analyzeRepository =
    async () => {

      try {

        setLoading(true);

        const response =
          await axios.post(
            "http://localhost:5001/analyze",
            {
              repo: repoUrl
            }
          );

        console.log(
          response.data
        );

        setRepoAnalyzed(
          true
        );

        alert(
          "Repository analyzed!"
        );

      } catch (error) {

        console.error(
          error
        );

        alert(
          "Failed to analyze repo"
        );

      } finally {

        setLoading(false);
      }
    };

  // ask repository
  const askRepository =
    async () => {

      try {

        setLoading(true);

        const response =
          await axios.post(
            "http://localhost:5001/ask",
            {
              question
            }
          );

        setAnswer(
          response.data.answer
        );

      } catch (error) {

        console.error(
          error
        );

        alert(
          "Failed asking repository"
        );

      } finally {

        setLoading(false);
      }
    };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "40px auto",
        padding: "20px",
        fontFamily:
          "Arial"
      }}
    >
      <h1>
        CodeAtlas
      </h1>

      <p>
        AI-Powered
        Repository Intelligence
      </p>

      {/* Repo URL */}
      <input
        type="text"
        placeholder="Paste GitHub repository URL"
        value={repoUrl}
        onChange={(e) =>
          setRepoUrl(
            e.target.value
          )
        }
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "12px"
        }}
      />

      {/* Analyze button */}
      <button
        onClick={
          analyzeRepository
        }
        disabled={loading}
        style={{
          padding:
            "12px 20px",
          cursor: "pointer"
        }}
      >
        {loading
          ? "Analyzing..."
          : "Analyze Repository"}
      </button>

      {/* Ask section */}
      {repoAnalyzed && (
        <div
          style={{
            marginTop:
              "40px"
          }}
        >
          <h2>
            Ask Repository
          </h2>

          <input
            type="text"
            placeholder="How authentication works?"
            value={
              question
            }
            onChange={(e) =>
              setQuestion(
                e.target.value
              )
            }
            style={{
              width:
                "100%",
              padding:
                "12px",
              marginBottom:
                "12px"
            }}
          />

          <button
            onClick={
              askRepository
            }
            disabled={
              loading
            }
            style={{
              padding:
                "12px 20px"
            }}
          >
            Ask AI
          </button>

          {/* Answer card */}
          {answer && (
            <div
              style={{
                marginTop:
                  "30px",
                background:
                  "#f5f5f5",
                padding:
                  "20px",
                borderRadius:
                  "10px",
                whiteSpace:
                  "pre-wrap"
              }}
            >
              <h3>
                AI Answer
              </h3>

              {answer}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default Home;