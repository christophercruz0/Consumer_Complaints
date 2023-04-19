function graphs1(patientID){
    const api_url = "http://127.0.0.1:5001/api/v1.0/productdata.json" ;
    d3.json(api_url).then(function(data) {
        let product = Object.keys(data)
        let counts = Object.values(data)
        let barColors = [ "#b91d47", "#00aba9", "#2b5797"]


        new Chart("myChart", {
            type: "pie",
            data: {
              labels: product,
              datasets: [{
                backgroundColor: barColors,
                data: counts
              }]
            },
            options: {
              title: {
                display: true,
                text: "Counts of products"
              }
            }
        });
    });

}

function init(){
    const belly_button_json_url = "http://127.0.0.1:5001/api/v1.0/productdata.json" ;
    const firstPatient = 0 ;
    graphs1(firstPatient);
}

function optionChanged(patientID) {
    graphs1(patientID);


}

init();