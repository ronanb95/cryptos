//Change 2 here to x for update every x minutes
const Interval_Time = 60000 * 2

let market_ajax_call = function(){
    $.get("api/realtime", function(data, status) {
        console.log(data)
        let table = document.getElementById('table_body');
        let updatedHTML = '';
        data.forEach(coin => {
            row =   "<tr>"+
                        "<td> <img class='coin_image' src=" + coin.image + "/></td>" +
                        "<td>" + coin.name + "</td>" +
                        "<td>" + coin.current_price + "</td>" +
                        "<td>" + coin.market_cap + "</td>" +
                        "<td>" + coin.price_change_24h + "</td>" +
                    "</tr>"
            updatedHTML += row;
        })   
        table.innerHTML = updatedHTML;     
    })
};

$(document).ready( function () {
    $('#table_id').DataTable();
} );

$(document).ready(market_ajax_call());

//Perform update every 2 minutes
//setInterval(ajax_call, interval);