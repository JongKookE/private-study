<?php 
	$age = 1;
	$time = 12;
	$for_country = False;
	$walfare = False;

	echo "당신의 나이는 $age";
	echo "입니다.<br>";
	echo "당신의 입장시간은 $time";
	echo "입니다.<br>";

	if ($for_country ==True){
		echo "당신은 국가유공자입니다.<br>";
	}
	else {
		echo "당신은 국가유공자가 아닙니다.<br>";
	}
	if ($walfare == True){
		echo "당신은 복지카드를 소유하고 있습니다.<br>";
	}
	else{
		echo "당신은 복지카드를 소유하고 있지않습니다.<br>";
	}


	if ($age < 3){
		echo "입장료 무료입니다!";
	}
	else if($age>3 and $age <13 or $time > 17){
		echo "특별 할인입니다!";
	}
	else if($age > 14 and $age < 18 or $age > 70 or $for_country == True or $walfare == True){
		echo "할인입니다!";
	}
	else{
		echo "일반고객입니다!";
	}
	
?>