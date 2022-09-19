
const login_form = document.querySelector("#login-form");
const login_input = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";

function on_login_submit(event){
    event.preventDefault();
    login_form.classList.add(HIDDEN_CLASSNAME);
    const username = login_input.value;
    localStorage.setItem(USERNAME_KEY, username);
    paint_greeting(username);
}

login_form.addEventListener("submit", on_login_submit)

const save_username = localStorage.getItem(USERNAME_KEY);

function paint_greeting(username){
    greeting.innerText = `HELLO ${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME);
}

if(save_username === null){
    login_form.classList.remove(HIDDEN_CLASSNAME);
    login_form.addEventListener("submit", on_login_submit);
}
else{
    paint_greeting(save_username);
    
}