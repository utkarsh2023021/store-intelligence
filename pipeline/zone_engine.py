import cv2
import numpy as np

class ZoneEngine:

    def __init__(self, zones):

        self.zones = zones

    def get_zone(self, cx, cy):

        point = (float(cx), float(cy))

        for zone_name, polygon in self.zones.items():

            contour = np.array(
                polygon,
                dtype=np.int32
            )

            inside = cv2.pointPolygonTest(
                contour,
                point,
                False
            )

            if inside >= 0:
                return zone_name

        return None