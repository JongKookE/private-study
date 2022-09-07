const login_form = document.querySelector("#login-form");
const login_input = document.querySelector("#login-form input");
const link = document.querySelector("a")

function press_submit(event){
    event.preventDefault();
    console.log(login_input.value);
}

function link_click(event){
    event.preventDefault();
    console.log(event);
    alert("clicked");

}

login_form.addEventListener("submit", press_submit);
link.addEventListener("click",link_click)