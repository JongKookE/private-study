<?php
$cday=date("d");
$cmonth=date("m");
$cyear=date("Y");
echo("<form action=nal_display.php method=post>");		// 날짜표시.php 파일에 값을 전달
echo "<TD align=left><select name=day>";		// 일을 선택
$i=1;
while($i<32) {
    if ($cday == $i) {
      echo "<option selected> $i";
      }
    else  {
      echo "<option> $i";
      }
    $i=$i+1;
    }
echo "</select>";
echo "/<select name=month>";				// 달을 선택
$i=1;
while($i<13) {
    if ($cmonth == $i) {
      echo "<option selected> $i";
      }
    else  {
      echo "<option> $i";
      }
    $i=$i+1;
    }
echo "</select>";
echo "/<select name=year>";				// 년도를 선택
echo "<option selected> $cyear";
echo "</select></TD>";
echo "<P><input type=submit value=선택하기><P>";
echo "</form>";
?>
