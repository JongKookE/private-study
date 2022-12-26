const todoForm = document.querySelector("#todo-form");
const todoList = document.querySelector("#todo-list");
const todo_input = document.querySelector("#todo-form input");
let todos = [];

const todo_key = "todos";

function save_todos(){
    localStorage.setItem(todo_key, JSON.stringify(todos));
}
function delete_todo(event){
    const li = event.target.parentElement;
    li.remove();
    todos = todos.filter(todo => todo.id !== parseInt(li.id));
    save_todos();
    //alert(`${new_todo}를 삭제하셨습니다.`);
}

function paint_todo(new_todo){
    const li = document.createElement("li");
    li.id = new_todo.id;
    const span = document.createElement("span");
    const button = document.createElement("button");
    button.innerText = "X";

    button.addEventListener("click", delete_todo);
    li.appendChild(span);
    li.appendChild(button);
    span.innerText = new_todo.text;
    todoList.appendChild(li);
}

function handle_ToDo_submit(event){
    event.preventDefault();
    const new_todo = todo_input.value;
    todo_input.value = "";
    const todo_object = {
        text : new_todo,
        id : Date.now()
    }
    todos.push(todo_object);
    paint_todo(todo_object);
    // delete_todo(new_todo);
    save_todos();
}

todoForm.addEventListener("submit", handle_ToDo_submit);

function sayHello(item){
    console.log(`this is your turn ${item}`);
}
const saved_todos = localStorage.getItem(todo_key);
console.log(saved_todos);
if (saved_todos !== null){
    const parsed_todos = JSON.parse(saved_todos);
    todos = parsed_todos;
    parsed_todos.forEach(paint_todo);
}

function sexy_filter(){

}

[1,2,3,4].filter(sexy_filter);