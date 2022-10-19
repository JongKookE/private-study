<?php
	$height = $_POST["height"];
	$weight = $_POST["weight"];
	$age = $_POST["age"];
	echo "키: {$height}<br>몸무게: {$weight}<br>나이: {$age}<br> ";
	$bimando = 0;
	if ($age < 20){
		$bimando = ($height - 110)/($weight * 0.8);
	}
	else{
		$bimando = ($height - 110)/($weight * 0.9);
	}
	echo "<br>";
	if ($bimando > 1.05){
		$bimando = number_format($bimando, 2);
		echo "당신의 비만도는 {$bimando}이므로 저체중입니다.";
	}
	else if ($bimando < 0.84){
		echo "당신의 비만도는 {$bimando}이므로 과체중입니다.";
	}
	else{
		echo "당신의 비만도는 {$bimando}이므로 정상입니다.";
	}
?>