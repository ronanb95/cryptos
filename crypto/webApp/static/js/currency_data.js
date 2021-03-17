//Change 2 here to x for update every x minutes
const Interval_Time = 60000 * 2

let market_ajax_call = function(){
    $.get("api/realtime", function(data, status) {
        let table = document.getElementById('table_body');
        let updatedHTML = '';
        data.forEach(coin => {
            if(coin.price_change_24h < 0){
                row =   "<tr>"+
                            "<td> <img class='coin_image' src=" + coin.image + "/></td>" +
                            "<td>" + coin.name + "</td>" +
                            "<td>" + coin.current_price + "</td>" +
                            "<td>" + coin.market_cap + "</td>" +
                            "<td class='red'>" + coin.price_change_24h + "</td>" +
                        "</tr>"

            } else {
                row =   "<tr>"+
                            "<td> <img class='coin_image' src=" + coin.image + "/></td>" +
                            "<td>" + coin.name + "</td>" +
                            "<td>" + coin.current_price + "</td>" +
                            "<td>" + coin.market_cap + "</td>" +
                            "<td class='green'>" + coin.price_change_24h + "</td>" +
                        "</tr>"
            }
            updatedHTML += row;
        })   
        table.innerHTML = updatedHTML;     
    })
};

$(document).ready(market_ajax_call());

//Perform update every 2 minutes
setInterval(market_ajax_call, Interval_Time);

document.getElementById('refresh_btn').addEventListener('click', market_ajax_call);