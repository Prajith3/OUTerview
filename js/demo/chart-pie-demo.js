

// var emotions = ["calm", "happy", "angry", "disgust"];

// var colouarray = ['red', 'green', 'yellow', 'blue'];

// var initialData = [0.1, 0.4, 0.3, 0.6];

// var updatedDataSet;

// var ctx = document.getElementById("barChart");
// var barChart = new Chart(ctx, {
//   type: 'bar',
//   data: {
//     labels: emotions,
//     datasets: [{
//       backgroundColor: colouarray,
//       label: 'Prediction',
//       data: initialData
//     }]
//   },
//   options: {
//     scales: {
//       yAxes: [{
//         ticks: {
//           beginAtZero: true,
//           min: 0,
//           max: 1,
//           stepSize: 0.5,
//         }
//       }]
//     }
//   }
// });

// function updateBarGraph(chart, label, color, data) {
//   chart.data.datasets.pop();
//   chart.data.datasets.push({
//     label: label,
//     backgroundColor: color,
//     data: data
//   });
//   chart.update();
// }

// setInterval(function() {
//   updatedDataSet = [Math.random(), Math.random(), Math.random(), Math.random()];
//   updateBarGraph(barChart, 'Prediction', colouarray, updatedDataSet);
// }, 1000);