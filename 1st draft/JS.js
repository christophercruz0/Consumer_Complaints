async function getproductData(){
  const url ='http://127.0.0.1:5000/api/v1.0/productdata'
  const response = await fetch(url)
  const productdata = await response.json();
  console.log(productdata);
  return productdata;
};

getproductData().then(productdata => {
  const name = productdata.map(productdata => {
      return(productdata.name);
  })
  
  const count = productdata.map(productdata => {
        return(productdata.count);
  })
 
      // setup 
      const data = {
      labels: name,
      datasets: [{
          label: 'Complaints',
          data: count,
          backgroundColor: [
          'rgba(255, 26, 104, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(0, 0, 0, 0.2)'
          ],
          borderColor: [
          'rgba(255, 26, 104, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(0, 0, 0, 1)'
          ],
          borderWidth: 1
      }]
      };

      // config 
      const config = {
      type: 'bar',
      data,
      options: {
          indexAxis :'y',
          labels :{
           font :{ size :5,
          
          scales: {
          y: {
              beginAtZero: true
          }
          }
          }
          }
      }
      };

      // render init block
      const myChart = new Chart(
      document.getElementById('myChart'),
      config
      );

      })