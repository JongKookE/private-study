const body = document.querySelector("body");
const MIN_DURATION = 10;

function make_snowflake(){
    const snowflake = document.createElement("div");
    const delay = Math.random() * 10;
    const initial_opacity = Math.random();
    const duration = Math.random() * 20 + MIN_DURATION;

    snowflake.classList.add("snowflake");
    snowflake.style.left = `${Math.random() * window.screen.width}px`;
    snowflake.style.animationDelay = `${delay}s`;
    snowflake.style.opacity = initial_opacity;
    body.appendChild(snowflake);
    snowflake.style.animation = `fall ${duration}s linear`;
}
//make_snowflake();
for (let index = 0; index < 500; index++){
    setTimeout(make_snowflake, 500* index);
}