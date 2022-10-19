<?php
	$curr_year = 2022;
	$curr_month = 9;
	$curr_day = 21;

	$birth_year = 2000;
	$birth_month = 2;
	$birth_day = 20;

	if ($birth_month < $curr_month){
		$age = $curr_year - $birth_year;
	}
	else if($birth_month == $curr_month){
		if($birth_day <= $curr_day){
			$age = $curr_year - $birth_year;
		}
		else{
			$age = $curr_year - $birth_year -1;
		}
	}
	else{
		$age = $curr_year - $birth_year -1;
	}
	echo "오늘 날짜 $curr_year";
	echo "년 ";
	echo $curr_month;
	echo "월 ";
	echo $curr_day;
	echo "일 <br>";

	echo "태어난 날짜 $birth_year";
	echo "년 ";
	echo $birth_month;
	echo "월 ";
	echo $birth_day;
	echo "일 <br>";
	echo "만 나이: $age";
	echo "세";

?>