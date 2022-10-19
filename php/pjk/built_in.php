<?php
	$ju = "000220-2446916";
	$sex = substr($ju, 7,1);
	if ($sex == "1" or $sex == "3"){
		echo "남자";
	}
	else{
		echo "여자";
	}
?>