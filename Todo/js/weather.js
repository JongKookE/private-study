const API_KEY = "d726e571b68db0674237b4b8071b6428";


function on_geo_ok(position){
    const lat = position.coords.latitude;
    const longi = position.coords.longitude;
    console.log(`위도: ${lat}, 경도 ${longi}`);
    console.log(position);
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${longi}&appid=${API_KEY}&unit=metrics`;
    console.log(url);   
    fetch(url).then(Response => Response.json()).then(data => {
        const weather = document.querySelector("#weather span:first-child");
        const city = document.querySelector("#weather span:last-child");
        city.innerText = data.name;
        weather.innerText = data.weather[0].main;
    });
}

function on_geo_error(){
    alert("날씨정보를 불러올 수 없습니다.");
}

navigator.geolocation.getCurrentPosition(on_geo_ok,on_geo_error);