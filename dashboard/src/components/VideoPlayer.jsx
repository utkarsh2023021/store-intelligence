import React from "react";

export default function VideoPlayer({
  videoRef,
  videoUrl
}) {

  return (
    <video
      ref={videoRef}
      width="1200"
      controls
      style={{
        border: "2px solid #444",
        borderRadius: "8px"
      }}
    >
      <source
        src={videoUrl}
        type="video/mp4"
      />
    </video>
  );
}