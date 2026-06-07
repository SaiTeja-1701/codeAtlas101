import { useEffect, useRef, useState }
from "react";

import mermaid from "mermaid";

mermaid.initialize({
  startOnLoad: false,
  theme: "default",
  securityLevel: "loose",
});

function MermaidDiagram({
  chart,
}) {

  const elementRef =
    useRef(null);

  const [hasError,
    setHasError] =
    useState(false);

  useEffect(() => {

    const renderChart =
      async () => {

        try {

          setHasError(
            false
          );

          const cleanChart =
            chart.trim();

          const uniqueId =
            `mermaid-${Math.random()
              .toString(36)
              .slice(2)}`;

          const result =
            await mermaid.render(
              uniqueId,
              cleanChart
            );

          if (
            elementRef.current
          ) {

            elementRef.current.innerHTML =
              result.svg;
          }

        } catch (
          error
        ) {

          console.error(
            "Mermaid error:",
            error
          );

          setHasError(
            true
          );
        }
      };

    renderChart();

  }, [chart]);

  if (hasError) {

    return (
      <div
        className=
          "mermaid-error"
      >
        <h4>
          Diagram could
          not render
        </h4>

        <pre>
          {chart}
        </pre>
      </div>
    );
  }

  return (
    <div
      ref={elementRef}
      className=
        "mermaid-container"
    />
  );
}

export default MermaidDiagram;