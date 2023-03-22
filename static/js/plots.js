// setting up url from our render file
const url = "https://march-madness-ml.onrender.com/api/v1.0/MarchMadness";

const teamMap = new Map();

// Fetch the JSON data and console log it
// selecting the data for the plot
d3.json(url).then(function (data) {
  // let selected = d3.select("#selDataset");
  // console.log(data)
  var trace1x = [];
  var trace1y = [];
  var trace2x = [];
  var trace2y = [];

  // var statBreakdown = {};
  let ele1 = document.getElementById('selDataset1');
  let ele2 = document.getElementById('selDataset2'); 

  for (let i = 0; i < 16; i++) {
    console.log(data[i]);
    trace1x.push(data[i].TEAM);
    trace1y.push(data[i].POSTSEASON);
    trace2x.push(data[i].TEAM);
    trace2y.push(data[i].RK);
    ele1.innerHTML = ele1.innerHTML + '<option ' + data[i].TEAM + '">' + data[i].TEAM + '</option>';
    ele2.innerHTML = ele2.innerHTML + '<option ' + data[i].TEAM + '">' + data[i].TEAM + '</option>';
    teamMap.set(data[i].TEAM, data[i]);
  }

  var trace1 = {
    x: trace1x,
    y: trace1y,
    name: 'POSTSEASON',
    marker: { color: 'rgb(159, 223, 159)' },
    type: 'bar',
  };

  var trace2 = {
    x: trace2x,
    y: trace2y,
    name: 'RANK',
    marker: { color: 'rgb(184, 224, 255)' },
    type: 'bar',
  };

  var teams = [trace1, trace2];
  var layout = {
    yaxis: {
      title: {
        text: 'Rank vs Postseason',
        font: {
          size: 15,
          color: '#7f7f7f'
        }
      }
    },
    xaxis: {
      tickangle: 45,
      title: {
        text: 'Teams',
        font: {
          size: 15,
          color: '#7f7f7f'
        }
      }
    },
    barmode: 'group'
  };
  Plotly.newPlot('myDiv', teams, layout);
});

function paintStats(id, div) {
  let demobox = d3.select("#" + div);
  let team = teamMap.get(id);

  demobox.html("");
  demobox.append("p").text('Team: ' + team.TEAM);
  demobox.append("p").text('Number of games won: ' + team.W);
  demobox.append("p").text('Adjusted Defensive Efficiency: ' + team.ADJDE);
  demobox.append("p").text('Adjusted Offensive Efficiency: ' + team.ADJOE);
  demobox.append("p").text('Power Rating: ' + team.BARTHAG);
  demobox.append("p").text('Wins Above Bubble: ' + team.WAB);
  demobox.append("p").text('Posrseason: ' + team.POSTSEASON);
};
