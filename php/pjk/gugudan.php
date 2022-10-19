<?php
	for ($b =1; $b<=9; $b++){
		echo "<tr>";
		for ($a=2; $a <= 9; $a++){
			$c = $b * $a;

			echo "<td>{$a} x {$b} = {$c}</td>";
		}
		echo "</tr>";
	}

?>