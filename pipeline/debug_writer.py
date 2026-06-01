import cv2

class DebugWriter:

    def __init__(self, path, width, height, fps):

        self.writer = cv2.VideoWriter(
            path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height)
        )

    def write(self, frame):

        self.writer.write(frame)

    def close(self):

        self.writer.release()