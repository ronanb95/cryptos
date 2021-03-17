//Contains code that fetches and displays information about users profiles

fetch("api/profiles")
.then(response => {
    return response.json();
}).then(data => {
    let card_section = document.getElementById('card_section');
    updatedHTML = "";
    data.forEach(profile => {
        card = '<div class="card-container ">'+
                    '<img class="round" src=' + profile.image + ' alt="user" />'+
                    '<h3>' + profile.user + '</h3>'+
                    '<div class="information">'+
                        '<h6>Information</h6>'+
                        '<ul>'+
                            '<li>Email: '+ profile.email +'</li>'+
                            '<li>Favourite Coin: ' +  profile.fav_coin + '</li>'+
                        '</ul>'+
                    '</div>'+
                '</div>';
        updatedHTML += card;
    })
    card_section.innerHTML = updatedHTML;
})