const prod_list_json = "http://127.0.0.1:5000/api/v1.0/productList"


const dataPromise = d3.json(sample_json);
//console.log("Data Promise: ", dataPromise);

// Fetch the JSON data and console log it
d3.json(prod_list_json).then(function(data) {
  console.log(data);
    const product_l = data.map(data => {
        return(data.product);
    })
    console.log(product_l);
  //console.log(data.metadata);
  //console.log(data.samples)

//Assigning variables to the different elements for use later

d3.select("#selDataset")
.selectAll('selDataset')
.data(product_l  )
.enter()
.append('option')
.text(function (d) { return d; }) // text showed in the menu
.attr("value", function (d) { return d; }); // corresponding value returned by the button

});

