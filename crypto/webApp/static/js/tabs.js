//Contains code to control the functionality of the users and market table sections tab switching

function openTab(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("tab");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active_tab", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active_tab";
}