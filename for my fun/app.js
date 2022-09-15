
const login_form = document.querySelector("#login-form");
const login_input = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";

function on_login_submit(event){
    event.preventDefault();
    login_form.classList.add(HIDDEN_CLASSNAME);
    const username = login_input.value;
    greeting.innerText = `HELLO ${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME);
    
}

login_form.addEventListener("submit", on_login_submit)
