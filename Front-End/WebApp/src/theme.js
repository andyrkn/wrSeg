var darkTheme = localStorage.getItem("isDark");
function toggleTheme() {
    if (localStorage.getItem("isDark") == "true")
        localStorage.setItem("isDark", "false");
    else
        localStorage.setItem("isDark", "true");
    setStyle();
}
function setStyle() {
    if (localStorage.getItem("isDark") == "true") {
        document.getElementById("inner-circle").style.backgroundColor = 'white';
        document.getElementById("toggle-btn").style.backgroundColor = 'gray';
        document.getElementById("inner-circle").style.marginLeft = '0px';
        document.getElementsByTagName("body")[0].style.backgroundColor = '#495172';
        var cards = document.getElementsByClassName("card");
        for (var i = 0; i < cards.length; i++) {
            cards[i].style.backgroundColor = "#313854";
            cards[i].style.color="white";
        }
        var element = document.getElementById("toggle-icon");
        element.classList.remove("fa-moon");
        element.classList.add("fa-sun");
        element.style.color="gray";
    }
    else {
        document.getElementById("inner-circle").style.backgroundColor = 'gray';
        document.getElementById("toggle-btn").style.backgroundColor = 'white';
        document.getElementById("inner-circle").style.marginLeft = '30px';
        document.getElementsByTagName("body")[0].style.backgroundColor = '#eee';
        var cards = document.getElementsByClassName("card");
        for (var i = 0; i < cards.length; i++) {
            cards[i].style.backgroundColor = "#eee";
            cards[i].style.color="black";   
        }
        
        var element = document.getElementById("toggle-icon");
        element.classList.remove("fa-sun");
        element.classList.add("fa-moon");
        element.style.color="white";
    }
    console.log(window.location);
}