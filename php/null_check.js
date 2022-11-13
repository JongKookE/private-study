const id_and_password = document.querySelector("#sign");
const login_button = document.querySelector(".login_btn");
const check = "";

id_and_password.addEventListener("click", function(){
    if (!id_and_password){
        alert("아이디 및 패스워드를 입력하세요");
    }
})