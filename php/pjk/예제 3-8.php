<?php
	$age = 65;
	$time = 5;
	$walfare = "no";
	$forCountry = "no";
	echo "나이 $age";
	echo "세<br>";
	echo "시간 $time";
	echo "시<br>";
	echo "복지카드유무 $walfare <br>";
	echo "국가유공자 $forCountry <br>";

	if ($age < 3) {
		echo "무료";
	}
	else if( $age > 3 && $age <= 13 || $time >= 17) {
		echo "특별할인! 4000원!";
	}
	else if ($age >= 14 and $age <= 18  or $age >= 70 or $walfare =="yes" or $forCountry == "yes"){ echo "할인! 8000원!";
	}
	else{
		echo "일반고객 10000원!";
	}

	

?>