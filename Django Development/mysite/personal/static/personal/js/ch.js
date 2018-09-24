// // #            var endpoint = 'api/chart/data/'#}
// // {#            var defaultdata = [12, 19, 3, 5, 2, 3]#}
//            var datafromdjango ={{my_data}};
//             console.log(datafromdjango)
//             // var defaultdata= [10000,10,10000,10000,20000,15000,16000]
//             // var labels = [1,2,3,4,5,6,7]
// // {#            $.ajax({#}
// // {#                method: "GET",#}
// // {#                url : endpoint,#}
// // {#                success: function(data){#}
// // {#                    console.log(data)#}
// // {#                },#}
// // {#                error : function(error_data){#}
// // {#                    console.log("error")#}
// // {#                    console.log(error_data)#}
// // {#                }#}
// // {#            })#}
//             var ctx = document.getElementById("myChart");
//             var myChart = new Chart(ctx, {
//                 type: 'line',
//                 data: {
//                     labels: datafromdjango.labels,
//                     datasets: [{
//                         label: '# of Votes',
//                         data: datafromdjango.defaultdata,
//                         backgroundColor: [
//                             'rgba(255, 99, 132, 0.2)',
//                             'rgba(54, 162, 235, 0.2)',
//                             'rgba(255, 206, 86, 0.2)',
//                             'rgba(75, 192, 192, 0.2)',
//                             'rgba(153, 102, 255, 0.2)',
//                             'rgba(255, 159, 64, 0.2)'
//                         ],
//                         borderColor: [
//                             'rgba(255,99,132,1)',
//                             'rgba(54, 162, 235, 1)',
//                             'rgba(255, 206, 86, 1)',
//                             'rgba(75, 192, 192, 1)',
//                             'rgba(153, 102, 255, 1)',
//                             'rgba(255, 159, 64, 1)'
//                         ],
//                         borderWidth: 1
//                     }]
//                 },
//                 options: {
//                     responsive: false,
//                     maintainAspectRatio: true,
//                     scales: {
//                         yAxes: [{
//                             ticks: {
//                                 beginAtZero:true
//                             }
//                         }]
//                     }
//                 }
//             });
