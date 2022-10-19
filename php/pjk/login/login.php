<html>
<head>
<meta charset = "utf-8">
<link href="css" rel = "stylesheet">
</head>
<body>
	<?php
		$name = $_POST["name"];
		$age = $_POST["age"];
		$id = $_POST["id"];
		$password = $_POST["password"];
		$combo_box = $_POST["grade"];
		$hobby = $_POST["hobby"];
		$content = $_POST["content"];

		$num = count($_POST["hobby"]);
		
		

		echo "이름: $name<br>";
		echo "나이: $age<br>";
		echo "아이디: $id<br>";
		echo "비밀번호: $password<br>";
		echo "학력 $combo_box<br>";
		echo "취미 ";
		for ($i =0; $i < $num; $i++){
			echo $_POST["hobby"][$i];
			if ($i != $num-1){
				echo ", ";
			}
		}
		echo "<br>";
		echo "기타 소개: $content<br>";
	?>

</body>
</html>