const clock = document.querySelector("h2#clock");

function get_clock(){
    const date = new Date();
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");
    clock.innerText= `${hours}:${minutes}:${seconds}`
    
}

get_clock()

setInterval(get_clock, 1000);