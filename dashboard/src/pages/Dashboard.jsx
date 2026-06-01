import { useEffect } from "react";
import { useState } from "react";

import SummaryCards from "../components/SummaryCards";
import TopZonesChart from "../components/TopZonesChart";
import DwellChart from "../components/DwellChart";

import "../styles/dashboard.css";

import {
  getDashboard
} from "../services/analyticsService";

export default function Dashboard() {

  const [data,setData] =
    useState(null);

  useEffect(() => {

    load();

  }, []);

  const load = async () => {

    try {

      const res =
        await getDashboard();

      setData(
        res.data
      );

    } catch(err) {

      console.log(err);
    }
  };

  if(!data)
    return <h2>Loading...</h2>;

return (

<div className="dashboard">

    <h1 className="dashboard-title">

        Store Analytics Dashboard

    </h1>

    <div className="cards">

        <SummaryCards
            totalVisitors={
                data.total_visitors
            }
        />

    </div>

    <div className="chart">

        <TopZonesChart
            data={data.top_zones}
        />

    </div>

    <div className="chart">

        <DwellChart
            data={data.avg_dwell}
        />

    </div>

</div>
);
}