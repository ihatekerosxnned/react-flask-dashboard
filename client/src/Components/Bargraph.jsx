import React, { useEffect, useState } from "react";
import Plot from "react-plotly.js";
import axios from "axios";

const Bargraph = () => {
  const [graphs, setGraphs] = useState({});

  useEffect(() => {
    axios
      .get("http://localhost:8080/api/allgraphs")
      .then((response) => {
        setGraphs(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching the graphs!", error);
      });
  }, []);
  return (
    <>
      <div className="container bg-white w-screen">
        {/* LINE CAHRT */}
        <div className=" bg-white flex container w-screen m-auto items-center justify-center">
          <div className="container w-full">
          {graphs.line_chart_gender && (
          <div>
            <Plot
              data={JSON.parse(graphs.line_chart_gender).data}
              layout={JSON.parse(graphs.line_chart_gender).layout}
              style={{ width: '100%' }} // Set the Plot width to 100%
            />
          </div>
        )}
          </div>
        </div>
        {/* BAR GRAPH */}
        <div className=" bg-white flex container w-screen m-auto items-center justify-center">
          <div className="container w-6/12">
          {graphs.bargraph_all && (
          <div>
            <Plot
              data={JSON.parse(graphs.bargraph_all).data}
              layout={JSON.parse(graphs.bargraph_all).layout}
            />
          </div>
        )}
          </div>
          <div className="container w-6/12">
          {graphs.graph_11_male_female && (
              <div>
                <Plot
                  data={JSON.parse(graphs.graph_11_male_female).data}
                  layout={JSON.parse(graphs.graph_11_male_female).layout}
                />
              </div>
            )}
          </div>
        </div>
        {/* PIE CHARTS */}
        <div className=" bg-white flex container w-screen m-auto items-center justify-center">
          <div className="container w-6/12">
            {graphs.piechart_gender && (
              <div>
                <Plot
                  data={JSON.parse(graphs.piechart_gender).data}
                  layout={JSON.parse(graphs.piechart_gender).layout}
                />
              </div>
            )}
          </div>
          <div className="container w-6/12">
            {graphs.graph_11_12 && (
              <div>
                <Plot
                  data={JSON.parse(graphs.graph_11_12).data}
                  layout={JSON.parse(graphs.graph_11_12).layout}
                />
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default Bargraph;
