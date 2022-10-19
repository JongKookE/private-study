<?php 
		
		$hour_rate = 10000;
		$day_night = "주간";
		$work_time = 12;


		echo "시간당 급여 <br>";
		echo "- 주간 근무 : $hour_rate <br>";
		echo "- 야간 근무 : 주간 시급 * 1.5 <br><br>";

		
		if($day_night == "주간"){
			$pay = $hour_rate * $work_time;
		}
		else{
			$pay = $hour_rate * $work_time * 1.5;
		}

		echo "$work_time 시간 동안 일한 $day_night 급여는 $pay 원입니다.";
?>