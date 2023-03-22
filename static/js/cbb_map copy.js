function createMap(postseasons) {

  // Create the tile layer that will be the background of our map.
  let streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });


  // Create a baseMaps object to hold the streetmap layer.
  let baseMaps = {
    "Street Map": streetmap,
    "Topography Map": topo
  };

  // Create an overlayMaps object to hold the layers.
  let overlayMaps = {
    // "Wins": wins,
    // "Seed": seeds,
    // "Rank": ranks,
    "Postseason": postseasons
  };

  

  // Create the map object with options.
  let map = L.map("map", {
    center: [37, -95],
    zoom: 5,
    layers: [streetmap, postseasons]
  });

  // Create a layer control, and pass it baseMaps and overlayMaps. Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}

function createMarkers(response) {

  // Pull the "stations" property from response.data.
  // let stations = response.data.stations;

  // Initialize an array to hold markers.
  // let winMarkers = [];
  // let seedMarkers = [];
  // let rankMarkers = [];
  let postseasonMarkers = [];
  
  function circleSize (seed) {
      return seed * 1000
  };

  function circleSizePostseason(postseason) {
      if (postseason <= 1)
          return 60000;
      if (postseason <= 5)
          return 50000;
      if (postseason <= 17)
          return 40000;
      if (postseason <= 33)
          return 30000;
      else
          return 25000
  };

  function circleColor (seed) {
      if (seed <= 1)
          return "#C34A2C";
      if (seed <= 2)
          return "#d4640f";
      if (seed <= 5)
          return "#d49f0f";
      if (seed <= 9)
          return "#f2ea50";
      else
          return "#8bdb23"
  };
  
  function circleFill (postseason) {
      if (postseason > 32)
          return .25;
      if (postseason >= 16)
          return .5;
      if (postseason >= 4)
          return .75;
      if (postseason >= 1)
          return 1;
      else
          return .1;
  };
  // Loop through the stations array.
  for (var i = 0; i < response.length; i++) {
    let data = response[i];
    // For each station, create a marker, and bind a popup with the station's name.
    // let marker = L.marker([data.LATITUDE, data.LONGITUD])
    //   .bindPopup("<h2>" + data.TEAM + "<h2><h4>Wins: " + data.W +  "</h4><h4>Tournament Seed: " + data.SEED + "</h4><h4>Predicted finish: " + data.POSTSEASON + "</h4>");

    // // Add the marker to the array.
    // winMarkers.push(marker);

    let postseasonMarker = L.circle([data.LATITUDE, data.LONGITUD], {
          radius: circleSizePostseason(data.POSTSEASON),
          fillColor: circleColor(data.SEED),
          color: circleColor(data.SEED),
          fillOpacity: 1,
          stroke: true
    }).bindPopup("<h2>" + data.TEAM + "<h2><h4>Conference: " + data.CONF + "<h2><h4>Wins: " + data.W +  "<h2><h4>Ranking: " + data.RK +  "</h4><h4>Tournament Seed: " + data.SEED + "</h4><h4>Predicted finish: " + data.POSTSEASON + "</h4>");
    postseasonMarkers.push(postseasonMarker);

  //   let rankMarker = L.circle([data.LATITUDE, data.LONGITUD],{
  //         radius: 12000,
  //         fillColor: circleColor(data.RK),
  //         color: circleColor(data.RK),
  //         fillOpacity: .8,
  //         stroke: true
  //   }).bindPopup("<h2>" + data.TEAM + "<h2><h4>Conference: " + data.CONF + "<h2><h4>Wins: " + data.W +  "<h2><h4>Ranking: " + data.RK +  "</h4><h4>Tournament Seed: " + data.SEED + "</h4><h4>Predicted finish: " + data.POSTSEASON + "</h4>");;
  //   rankMarkers.push(rankMarker);

  //   let seedMarker = L.circle([data.LATITUDE, data.LONGITUD], {
  //     radius: circleSize(data.SEED),
  //     fillColor: "#E48080",
  //     color: "#E48080",
  //     fillOpacity: 1,
  //     stroke: true
  //   }).bindPopup("<h2>" + data.TEAM + "<h2><h4>Conference: " + data.CONF + "<h2><h4>Wins: " + data.W +  "<h2><h4>Ranking: " + data.RK +  "</h4><h4>Tournament Seed: " + data.SEED + "</h4><h4>Predicted finish: " + data.POSTSEASON + "</h4>");;
  //   seedMarkers.push(seedMarker)
  }

  // Create a layer group that's made from the markers array, and pass it to the createMap function.
  // createMap(L.layerGroup(seedMarkers),L.layerGroup(rankMarkers),L.layerGroup(postseasonMarkers));
  createMap(L.layerGroup(postseasonMarkers));
}

// Perform an API call to get the information. Call createMarkers when it completes.
d3.json("https://march-madness-ml.onrender.com/api/v1.0/MarchMadness").then(data => createMarkers(data));

