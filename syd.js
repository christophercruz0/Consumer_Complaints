async function getCompanyData(){
    const url = "http://127.0.0.1:5000/api/v1.0/companyData/"
    const response = await fetch(url)
    const companyData = await response.json();
    console.log(companyData);
    return companyData;
  };
  
  function Options(companyData){
    var DatasetInput = d3.select("#selDataset");
    companyData.forEach(function(item){
      DatasetInput.append("option").attr('value', item.company).text(item.company + " (" + item.count + ")");
    });
  };
  
  function init(){
    getCompanyData().then(function(companyData){
      Options(companyData);
      // Set default value for dashboard
      var selectedValue = d3.select("#selDataset").property("value");
      var selectedItem = companyData.find(item => item.company === selectedValue);
      d3.select("#companyCount").text(selectedItem.count);
    });
  }
  
  function optionChanged(val){
    console.log("Selected",val);
    getCompanyData().then(function(companyData){
      var selectedItem = companyData.find(item => item.company === val);
      d3.select('.panel-body').text(selectedItem.count);
    });
  }
  
  init();

  async function getTOP(){
    const url = "http://127.0.0.1:5000/api/v1.0/top10Company/"
    const response = await fetch(url)
    const TOP = await response.json();
    console.log(TOP);
    return TOP;
}

async function createChart() {
    const TOP = await getTOP();
      
    const chartData = {
        labels: TOP.map(item => item.company),
        datasets: [
        {
            label: "Top 10 Companies",
            data: TOP.map(item => item.count),
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1
        }
       ]
     };
      
     const chartOptions = {
        responsive: true,
        legend: {
        display: false
        },
        scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            }
         }
        ]
       }
     };
      
     const ctx = document.getElementById("top-chart").getContext("2d");
     const myChart = new Chart(ctx, {
        type: "bar",
        data: chartData,
        options: chartOptions
    });
}   


createChart();

  
  