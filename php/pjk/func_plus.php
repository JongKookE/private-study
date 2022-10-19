<?php
	function plus($a, $b){
		$c = $a + $b;
		echo "$c <br>";
		return $c;
	}
	function sub($a, $b){
		$c = $a - $b;
		echo "$c <br>";
		return $c;
	}
	function mul($a, $b){
		$c = $a * $b;
		echo "$c <br>";
		return $c;
	}
	function div($a, $b){
		$c = $a / $b;
		echo "$c <br>";
		return $c;
	}
	plus(15,20);
	sub(55,20);
	mul(7,5);
	div(245, 7);
?>