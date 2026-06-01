import { useState } from "react";

import PolygonCanvas
from "../components/PolygonCanvas";

import ZoneList
from "../components/ZoneList";

import "../styles/calibration.css";

import {
  createZone
}
from "../services/zoneService";

export default function ZoneCalibration() {

  const [cameraId, setCameraId] =
    useState("CAM1");

  const [zoneName, setZoneName] =
    useState("");

  const [image, setImage] =
    useState(null);

  const handleUpload = (e) => {

    const file =
      e.target.files[0];

    if (!file) return;

    const url =
      URL.createObjectURL(file);

    setImage(url);
  };

  const savePolygon = async (
    polygon
  ) => {

    if (!zoneName) {

      alert(
        "Please enter zone name"
      );

      return;
    }

    try {

      const img =
        document.querySelector(
          ".zone-image"
        );

      await createZone({

        camera_id:
          cameraId,

        zone_name:
          zoneName,

        polygon,

        image_width:
          img.naturalWidth,

        image_height:
          img.naturalHeight
      });

      alert(
        "Zone Saved Successfully"
      );

      setZoneName("");

    } catch (err) {

      console.error(err);

      alert(
        "Failed To Save Zone"
      );
    }
  };

  return (

    <div className="calibration-page">

      <div
        className="calibration-header"
      >

        <h1>
          Camera Zone Calibration
        </h1>

        <p>
          Upload camera screenshot,
          draw polygons and save
          zone boundaries.
        </p>

      </div>

      <div
        className="calibration-layout"
      >

        <div
          className="canvas-section"
        >

          <div
            className="controls"
          >

            <select
              value={cameraId}
              onChange={(e) =>
                setCameraId(
                  e.target.value
                )
              }
            >

              <option value="CAM1">
                CAM1
              </option>

              <option value="CAM2">
                CAM2
              </option>

              <option value="CAM3">
                CAM3
              </option>

              <option value="CAM4">
                CAM4
              </option>

              <option value="CAM5">
                CAM5
              </option>

            </select>

            <input
              type="text"
              placeholder="Zone Name"
              value={zoneName}
              onChange={(e) =>
                setZoneName(
                  e.target.value
                )
              }
            />

            <input
              type="file"
              accept="image/*"
              onChange={
                handleUpload
              }
            />

          </div>

          {
            image && (

              <div
                className="image-container"
              >

                <img
                  src={image}
                  alt=""
                  className="zone-image"
                  style={{
                    display:
                      "none"
                  }}
                />

                <PolygonCanvas
                  image={image}
                  onSave={
                    savePolygon
                  }
                />

              </div>
            )
          }

        </div>

        <ZoneList />

      </div>

    </div>
  );
}