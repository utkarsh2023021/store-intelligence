import {
  useEffect,
  useState
} from "react";

import {
  getAllZones,
  deleteZone
}
from "../services/zoneService";

export default function ZoneList() {

  const [zones,setZones] =
    useState([]);

  useEffect(() => {

    loadZones();

  }, []);

  const loadZones =
    async () => {

      const res =
        await getAllZones();

      setZones(
        res.data
      );
    };

  const handleDelete =
    async (id) => {

      if (
        !window.confirm(
          "Delete zone?"
        )
      ) return;

      await deleteZone(id);

      loadZones();
    };

  const grouped = {};

  zones.forEach(zone => {

    if (
      !grouped[
        zone.camera_id
      ]
    ) {

      grouped[
        zone.camera_id
      ] = [];
    }

    grouped[
      zone.camera_id
    ].push(zone);
  });

  return (

    <div
      className="zone-list"
    >

      <h3>
        Saved Zones
      </h3>

      {

        Object.entries(
          grouped
        ).map(

          ([camera,zones]) => (

            <div
              key={camera}
              className="zone-group"
            >

              <h4>

                {camera}

                <span
                  className="zone-count"
                >

                  {zones.length}

                </span>

              </h4>

              {

                zones.map(
                  zone => (

                    <div
                      key={zone.id}
                      className="zone-item"
                    >

                      <div>

                        {
                          zone.zone_name
                        }

                      </div>

                      <div
                        className="zone-actions"
                      >

                        <button
                          className="edit-btn"
                        >
                          Edit
                        </button>

                        <button
                          className="delete-btn"
                          onClick={() =>
                            handleDelete(
                              zone.id
                            )
                          }
                        >
                          Delete
                        </button>

                      </div>

                    </div>
                  )
                )
              }

            </div>
          )
        )
      }

    </div>
  );
}