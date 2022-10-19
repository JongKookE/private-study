<?php
	$score = array(array(88,98,96,77,63),
				   array(86,77,66,86,93),
		    	   array(74,83,95,86,97));

	for ($i =0; $i<3; $i++){
		for($j=0; $j<5; $j++){
			echo "\$score[{$i}][{$j}] = {$score[$i][$j]} <br>" ;
		}
		echo "<br>";
	}
	for ($i =0; $i<3; $i++){
		$sum = 0;
		for($j=0; $j<5; $j++){
			$sum = $sum +  $score[$i][$j];
		}
	
		$avg = $sum/count($score[0]);
		$student_num = $i+1;
		echo "{$student_num}번 학생의 점수 => 합계 : {$sum}, 평균 : {$avg} <br>";
	}
	echo count($score[0]);
?>