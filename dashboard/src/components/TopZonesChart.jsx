import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

export default function TopZonesChart({
  data
}) {

  const chartData =
    Object.entries(data).map(
      ([zone,count]) => ({
        zone,
        count
      })
    );

  return (

    <div>

      <h2>
        Top Zones
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

        <Bar dataKey="count" />
      </BarChart>

    </div>
  );
}