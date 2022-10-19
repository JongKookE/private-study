<?php
	$ju = "000220-7446916";
	$sex = substr($ju, 7,1);
	if ($sex == "1" or $sex == "3"){
		echo "남자";
	}
	else if ($sex == "2" or $sex == "4"){
		echo "여자";
	}
	else{
		echo "?";
	}
?>