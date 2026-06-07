import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import MermaidDiagram from "../components/MermaidDiagram";

import "../styles/HomePage.css";

function Home() {
  const [repoUrl,
    setRepoUrl] =
    useState("");

  const [
    repoAnalyzed,
    setRepoAnalyzed,
  ] = useState(false);

  const [loading,
    setLoading] =
    useState(false);

  const [question,
    setQuestion] =
    useState("");

  const [answer,
    setAnswer] =
    useState("");

  const [docs,
    setDocs] =
    useState({});

  const [
    selectedDoc,
    setSelectedDoc,
  ] = useState(
    "README.md"
  );

  const [
    docsGenerated,
    setDocsGenerated,
  ] = useState(false);

  // ----------------
  // analyze repo
  // ----------------
  const analyzeRepository =
    async () => {
      try {
        setLoading(true);

        await axios.post(
          "http://localhost:5001/analyze",
          {
            repo: repoUrl,
          }
        );

        setRepoAnalyzed(
          true
        );
      } catch (
        error
      ) {
        console.error(
          error
        );
      } finally {
        setLoading(false);
      }
    };

  // ----------------
  // ask repo
  // ----------------
  const askRepository =
    async () => {
      try {
        setLoading(true);

        const response =
          await axios.post(
            "http://localhost:5001/ask",
            {
              question,
            }
          );

        setAnswer(
          response.data.answer
        );
      } catch (
        error
      ) {
        console.error(
          error
        );
      } finally {
        setLoading(false);
      }
    };

  // ----------------
  // generate docs
  // ----------------
  const generateDocs =
    async () => {
      try {
        setLoading(true);

        await axios.post(
          "http://localhost:5001/generate-docs"
        );

        const response =
          await axios.get(
            "http://localhost:5001/docs"
          );

        setDocs(
          response.data.docs
        );

        setDocsGenerated(
          true
        );
      } catch (
        error
      ) {
        console.error(
          error
        );
      } finally {
        setLoading(false);
      }
    };

  return (
    <div className="page-container">

      <div className="hero-section">
        <h1 className="hero-title">
          CodeAtlas
        </h1>

        <p className="hero-subtitle">
          AI-Powered Repository
          Intelligence &
          Documentation
        </p>
      </div>

      {/* Analyze */}
      <div className="card">
        <h2 className="section-title">
          Analyze Repository
        </h2>

        <div className="input-wrapper">
          <input
            className="repo-input"
            placeholder="Paste GitHub repo URL"
            value={repoUrl}
            onChange={(e) =>
              setRepoUrl(
                e.target.value
              )
            }
          />

          <button
            className="primary-button"
            onClick={
              analyzeRepository
            }
          >
            Analyze
          </button>
        </div>

        {repoAnalyzed && (
          <div className="success-badge">
            Repository analyzed
          </div>
        )}
      </div>

      {/* Ask Repo */}
      {repoAnalyzed && (
        <div className="card">
          <h2 className="section-title">
            Ask Repository
          </h2>

          <div className="input-wrapper">
            <input
              className="question-input"
              placeholder="How authentication works?"
              value={question}
              onChange={(e) =>
                setQuestion(
                  e.target.value
                )
              }
            />

            <button
              className="primary-button"
              onClick={
                askRepository
              }
            >
              Ask AI
            </button>
          </div>

          {answer && (
            <div className="answer-card">
              <ReactMarkdown
                remarkPlugins={[
                  remarkGfm,
                ]}
              >
                {answer}
              </ReactMarkdown>
            </div>
          )}
        </div>
      )}

      {/* Docs */}
      {repoAnalyzed && (
        <div className="card">
          <div className="docs-header">
            <h2 className="section-title">
              Documentation
            </h2>

            <button
              className="primary-button"
              onClick={
                generateDocs
              }
            >
              Generate Docs
            </button>
          </div>

          {loading && (
            <p className="loading-text">
              Generating documentation...
            </p>
          )}

          {docsGenerated && (
            <div className="docs-layout">

              {/* sidebar */}
              <div className="docs-sidebar">
                {Object.keys(
                  docs
                ).map((file) => (
                  <button
                    key={file}
                    className={`doc-tab ${
                      selectedDoc ===
                      file
                        ? "active"
                        : ""
                    }`}
                    onClick={() =>
                      setSelectedDoc(
                        file
                      )
                    }
                  >
                    {file}
                  </button>
                ))}
              </div>

              {/* viewer */}
              <div className="docs-viewer">
                <ReactMarkdown
                  remarkPlugins={[
                    remarkGfm,
                  ]}

                  components={{
                    code({
                      children,
                      className,
                    }) {

                      const content =
                        String(
                          children
                        );

                      // detect mermaid
                      if (
                        className ===
                        "language-mermaid"
                      ) {
                        return (
                          <MermaidDiagram
                            chart={
                              content
                            }
                          />
                        );
                      }

                      return (
                        <code
                          className={
                            className
                          }
                        >
                          {children}
                        </code>
                      );
                    },
                  }}
                >
                  {
                    docs[
                      selectedDoc
                    ]
                  }
                </ReactMarkdown>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default Home;