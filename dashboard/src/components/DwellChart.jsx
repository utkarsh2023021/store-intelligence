import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

export default function DwellChart({
  data
}) {

  const chartData =
    Object.entries(data).map(
      ([zone,dwell]) => ({
        zone,
        dwell
      })
    );

  return (

    <div>

      <h2>
        Average Dwell Time
      </h2>

      <BarChart
        width={700}
        height={350}
        data={chartData}
      >
        <CartesianGrid />

        <XAxis dataKey="zone" />

        <YAxis />

        <Tooltip />

        <Bar dataKey="dwell" />
      </BarChart>

    </div>
  );
}