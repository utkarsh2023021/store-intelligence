import {
  useEffect,
  useState
} from "react";

import {
  startPipeline,
  getStatus
} from "../services/pipelineService";

import "../styles/processing.css";

export default function Processing() {

  const [status,setStatus] =
    useState({

      camera:null,

      progress:0,

      status:"idle"
    });

  const runPipeline =
    async () => {

      await startPipeline();
    };

  useEffect(() => {

    const interval =
      setInterval(

        async () => {

          try {

            const res =
              await getStatus();

            setStatus(
              res.data
            );

          } catch(err) {

            console.log(err);
          }

        },

        1000
      );

    return () =>
      clearInterval(
        interval
      );

  }, []);

  return (

    <div
      className="processing-page"
    >

      <div
        className="processing-card"
      >

        <h1>
          Analytics Processing
        </h1>

        <button
          className="run-btn"
          onClick={
            runPipeline
          }
        >
          Run Analytics
        </button>

        <h3>

          Status:
          {" "}
          {
            status.status
          }

        </h3>

        <h3>

          Camera:
          {" "}
          {
            status.camera
          }

        </h3>

        <div
          className="progress-bar"
        >

          <div
            className="progress-fill"

            style={{

              width:
                `${status.progress}%`
            }}
          />

        </div>

        <p>

          {
            status.progress
          }%

        </p>

      </div>

    </div>
  );
}