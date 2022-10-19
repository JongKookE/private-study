<table border = "1" width = "300">
<tr align = "center"><td>a</td><td>b</td><td>c</td></tr>
<?php
	$a = array(array(1,2,3),
				   array(4,5,6),
				   array(7,8,9));
	$b = array(array(9,8,7),
				   array(6,5,4),
				   array(3,2,1));
	$c = array(array(0,0,0),
				   array(0,0,0),
				   array(0,0,0));
	$cnt = 0;
	for ($i = 0; $i < 3; $i++){
		for ($j = 0; $j < 3; $j++){
			echo "<tr><td>\$a[$i][$j]= {$a[$i][$j]}</td><td></td><td></td></tr> ";
		} 	
	} 

	$sum = 0;
	for($i = 0; $i < count($a); $i++){
		for($j = 0; $j < count($b[0]); $j++){
			$sum =  $a[$i][$j] + $b[$i][$j] + $c[$i][$j];	
		}
		echo "<tr align = 'center'><td>{$sum}</td><td>{$sum}</td><td>{$sum}</td></tr>";
		
	}
?>