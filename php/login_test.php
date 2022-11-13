<?php
    $id = $_POST["login_id"];
    $password = $_POST["login_password"];
    $id_list = array("ID");
    $password_list = array("PASSWORD");
    array_push($password_list, $password);
    array_push($id_list, $id);
    echo "저장 될 아이디 : {$id}<br>";
    echo "저장된 아이디 : ";
    foreach ($id_list as $id_list){
        
        echo " {$id_list} " . "\n";
    }
    echo "<br>저장 될 비밀번호 : {$password} <br>";
    foreach ($password_list as $password_list){
        
        echo " {$password_list} " . "\n";
    }


?>