import { useState } from "react";

export default function PolygonCanvas({
  image,
  onSave,
}) {

  const [points, setPoints] =
    useState([]);

  const [imgInfo, setImgInfo] =
    useState(null);

  const handleClick = (e) => {

    const img = e.target;

    const rect =
      img.getBoundingClientRect();

    const x =
      e.clientX - rect.left;

    const y =
      e.clientY - rect.top;

    setPoints(prev => [

      ...prev,

      [
        Math.round(x),
        Math.round(y)
      ]
    ]);
  };

  const handleImageLoad = (
    e
  ) => {

    const img = e.target;

    setImgInfo({

      naturalWidth:
        img.naturalWidth,

      naturalHeight:
        img.naturalHeight,

      displayWidth:
        img.clientWidth,

      displayHeight:
        img.clientHeight
    });
  };

  const handleSave = () => {

    if (!imgInfo) return;

    const scaleX =
      imgInfo.naturalWidth
      /
      imgInfo.displayWidth;

    const scaleY =
      imgInfo.naturalHeight
      /
      imgInfo.displayHeight;

    const scaledPolygon =
      points.map(
        ([x, y]) => [

          Math.round(
            x * scaleX
          ),

          Math.round(
            y * scaleY
          )
        ]
      );

    onSave(
      scaledPolygon
    );
  };

  const clearPoints = () => {

    setPoints([]);
  };

  return (

    <div
      style={{
        position: "relative",
        display: "inline-block"
      }}
    >

      <img
        src={image}
        alt=""
        onLoad={
          handleImageLoad
        }
        onClick={
          handleClick
        }
        style={{
          maxWidth: "1200px",
          display: "block",
          borderRadius: "12px"
        }}
      />

      <svg
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          pointerEvents: "none"
        }}
      >

        {

          points.length > 1 && (

            <polygon

              points={

                points
                  .map(
                    p =>
                      `${p[0]},${p[1]}`
                  )
                  .join(" ")
              }

              fill="
                rgba(
                  34,
                  197,
                  94,
                  0.3
                )
              "

              stroke="
                rgb(
                  34,
                  197,
                  94
                )
              "

              strokeWidth="3"
            />
          )
        }

        {

          points.map(
            (p, i) => (

              <circle
                key={i}
                cx={p[0]}
                cy={p[1]}
                r="6"
                fill="red"
              />
            )
          )
        }

      </svg>

      <div
        style={{
          marginTop: "12px",
          display: "flex",
          gap: "10px"
        }}
      >

        <button
          onClick={
            handleSave
          }
        >
          Save Polygon
        </button>

        <button
          onClick={
            clearPoints
          }
        >
          Clear
        </button>

      </div>

    </div>
  );
}