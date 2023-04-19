function graphs1(patientID){
    const api_url = "http://127.0.0.1:5000/api/v1.0/productdata.json" ;
    d3.json(api_url).then(function(data) {
        let product = Object.keys(data)
        let counts = Object.values(data)
        let barColors = [ "#b91d47", "#00aba9", "#2b5797","#b01d77", "#09bba7", "#7z8877", "#b01d88", "#10eba3", "#7b5707"]


        new Chart("myChart", {
            type: "bar",
            data: {
              labels: product,
              datasets: [{
                backgroundColor: barColors,
                data: counts
              }]
            },
            options: {
              title: {
                display: false,
                text: "Counts of products"
              }
            }
        });
    });

}

function init(){
    const belly_button_json_url = "http://127.0.0.1:5000/api/v1.0/productdata.json" ;
    const firstPatient = 0 ;
    graphs1(firstPatient);
}

function optionChanged(patientID) {
    graphs1(patientID);


}

init();