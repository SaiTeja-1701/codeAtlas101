import { useState } from "react";
import axios from "axios";

const Home = () => {
  const [repoInput, setRepoInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!repoInput.trim()) return;

    try {
      setLoading(true);

      const response = await axios.post(
        "http://localhost:5001/analyze",
        {
          repo: repoInput,
        }
      );

      console.log(response.data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>
          🧭 CodeAtlas
        </h1>

        <p style={styles.subtitle}>
          AI-powered codebase intelligence
        </p>

        <input
          type="text"
          placeholder="Paste GitHub repo URL or local path"
          value={repoInput}
          onChange={(e) =>
            setRepoInput(e.target.value)
          }
          style={styles.input}
        />

        <button
          onClick={handleAnalyze}
          style={styles.button}
          disabled={loading}
        >
          {loading
            ? "Analyzing..."
            : "Analyze Repository"}
        </button>
      </div>
    </div>
  );
};

const styles = {
  container: {
    minHeight: "100vh",
    background: "#0f172a",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    color: "white",
  },

  card: {
    width: "600px",
    background: "#1e293b",
    padding: "40px",
    borderRadius: "20px",
    display: "flex",
    flexDirection: "column",
    gap: "20px",
  },

  title: {
    margin: 0,
    fontSize: "42px",
  },

  subtitle: {
    color: "#94a3b8",
    marginTop: "-10px",
  },

  input: {
    padding: "16px",
    borderRadius: "10px",
    border: "none",
    fontSize: "16px",
  },

  button: {
    padding: "16px",
    borderRadius: "10px",
    border: "none",
    background: "#2563eb",
    color: "white",
    fontSize: "16px",
    cursor: "pointer",
  },
};

export default Home;