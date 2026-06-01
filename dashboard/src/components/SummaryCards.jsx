export default function SummaryCards({
  totalVisitors
}) {

  return (
    <div
      style={{
        display:"flex",
        gap:"20px",
        marginBottom:"20px"
      }}
    >
      <div
        style={{
          border:"1px solid #ccc",
          padding:"20px",
          width:"250px"
        }}
      >
        <h3>Total Visitors</h3>

        <h1>
          {totalVisitors}
        </h1>
      </div>
    </div>
  );
}