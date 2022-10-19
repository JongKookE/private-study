<?php 
	$inch = 10;
	$inches = 255*0.1;
	echo "<table border = '1'>";
	echo "<tr>";
	echo "<th width = '100'>인치</th><th width = '100'>센티미터</th><th width = '100'>joke</th>>";
	echo "<tr>";
	while($inch <= 100){
		$cm = $inch * 2.54;
		#echo "<tr align = 'center'><td>$inch</td><td>$cm</td><tr>";
		echo "<tr align = 'center'><td>$inch</td><td> $cm </td><td>$inches</td><tr>";
		$inch = $inch + 10;
	}
	echo "</table>";
?>