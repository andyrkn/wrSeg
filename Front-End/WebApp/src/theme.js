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
        document.getElementsByTagName("body")[0].style.backgroundColor='#495172';
        }
    else {
        document.getElementById("inner-circle").style.backgroundColor = 'gray';
        document.getElementById("toggle-btn").style.backgroundColor = 'white';
        document.getElementById("inner-circle").style.marginLeft = '30px';
        document.getElementsByTagName("body")[0].style.backgroundColor='#eee';
        }
    console.log(window.location);
}