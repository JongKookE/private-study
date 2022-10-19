<?php
	/*
	고혈압 OR
	정상 AND
	저혈압 OR
	*/

	$iwan = 50;
	$suchuck =120; 
	echo "이완기 혈압: $iwan mmHg<br>";
	echo "수축기 혈압: $suchuck mmHg<br>";
	if ($iwan > 90 or $suchuck > 140){
		echo "<h1>고혈압";
	}
	elseif (60 <= $iwan and $iwan < 90 and 100 <= $suchuck and $suchuck  < 140){
		echo "<h1>정상";
	}
	else{
		echo "<h1>저혈압";
	}
?>