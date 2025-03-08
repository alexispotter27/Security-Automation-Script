import React, { useEffect, useState } from "react";
import axios from "axios";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

const API_URL = "http://127.0.0.1:8000/scan-results";

const ScanChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(API_URL)
      .then(response => {
        // Group results by status
        const statusCounts = response.data.reduce((acc, { status }) => {
          acc[status] = (acc[status] || 0) + 1;
          return acc;
        }, {});

        // Convert to Recharts format
        const chartData = Object.keys(statusCounts).map(key => ({
          status: key,
          count: statusCounts[key],
        }));

        setData(chartData);
      })
      .catch(error => console.error("Error fetching scan results:", error));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Scan Results Overview</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="status" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="count" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ScanChart;
