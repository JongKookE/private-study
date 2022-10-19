<html>
<head>
<meta charset = "utf-8">
<link href="css" rel="stylesheet">
</head>
<body>
	<?php
		$file_dir = "C:/xampp/htdocs/07/data/";
		$file_path =$file_dir.$_FILES["upload_file"]["name"];
		if(move_uploaded_file($_FILES["upload_file"]["tmp_name"], $file_path)){
			$img_poath = "data/".$_FILES["upload_file"]["name"];
		
	?>
	<ul>
		<li><img src ="<?= $img_path?>"></li>
		<li><?=$_POST["commit"]?></li>
	</ul>
<?php
	}
	else{
		echo "파일 업로드 실패"
	}
?>


</body>

</html>