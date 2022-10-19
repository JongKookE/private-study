<h3>섭씨 -> 화씨 온도 변환 </h3>
<table border = "1" width = "300">
<tr align = "center"><td width = "100">섭씨</td><td width = "200">화씨</td></tr>

<?php
	for($C = -15; $C<=35; $C = $C+5){
		$to_f = ($C * 9/5) + 32;
		echo "<tr align = 'center'><td>$C</td><td>$to_f</td></tr>";	
	}
?>
</table>