# strpos function
<img src ="Strpos.jpg" width ="100%" hight = "100%">


strpos () เป็นฟังก์ชันที่ตรวจสอบว่ามีคำที่ต้องการอยู่ใน Sting หรือ ไม่

***การใช้งาน***

    strpos ( string $haystack , string $needle , int $offset = 0 ) : int|false

การใช้งาน ฟังก์ชัน แบบง่ายๆ **strpos(ข้อีความ,สตริงที่ต้องการหา)** ถ้าต้องการหาสตริงในที่ต้องการ ที่อยู่ในข้อความนั้น จะ return ค่ามาเป็นตำแหน่งและ ture,false
***ตัวอย่างการใช้งาน***

    <?php
    $mystring = '../../';
    $findme   = '/';
    $pos = strpos($mystring, $findme);

    // Note our use of ===.  Simply == would not work as expected
    // because the position of 'a' was the 0th (first) character.
    if ($pos === false) {
        echo "The string '$findme' was not found in the string '$mystring'";
    } else {
        echo "The string '$findme' was found in the string '$mystring'";
        echo " and exists at position $pos";
    }
    ?>

ตัวอย่างการใช้งานนั้น โจทย์ต้องการหา ตัวอักษร '/' จากที่เราทำความเข้าใจกับการใช้งานเบื้องต้นแล้ว strpos() จะ return ค่า ว่าได้ตรวจสอบ เจอ หรือไม่ ถ้าเจอจะ return true และ ตำแหน่งของ ตัวอักษร มา เช่นในตัวอย่างนี้ จะ ได้ $pos จะเท่ากับ true และตำแหน่งที่ตรวจสอบพบ คือ 2 

***ผลลัพธ์***

    The string '/' was found in the string '../../' and exists at position 2

***ในการประยุกต์ใช้งาน***
จะนำเอาไปตรวจสอบการ ใช้เทคนิค ในการทำ [**directory traversal**](http://blog.itselectlab.com/?p=5582) ซึ่งหลักๆ ถ้าเราตรวจเช็ค ได้ว่ามีการ '../' อยู่ใน ข้อความที่ผู้ใช้งานใส่มาหรือไม่ นั้นก็ทำให้เราป้องกันการโจมตี ของ directory traversal ได้ระดับหนึ่ง
<img src ="Directory Traversal.png" width ="100%" hight = "50%">

    <? function directory_traversal_check_1($data)
    <? {
    <?
    <? // Not bulletproof
    <?
    <? $directory_traversal_error = "";
    <?
    <? // Searches for special characters in the GET parameter
    <? if(strpos($data, "../") !== false ||
    <? strpos($data, "..\\") !== false ||
    <? strpos($data, "/..") !== false ||
    <? strpos($data, "\..") !== false)
    <?
    <? {
    <?
    <? $directory_traversal_error = "Directory Traversal detected!";
    <?
    <? }
    <?
    <? /*
    <? else
    <? {
    <?
    <? echo "Good path!";
    <?
    <? }
    <? */
    <?
    <? return $directory_traversal_error;

***อ้างอิง***
+ http://blog.itselectlab.com/?p=5582
+ https://www.php.net/manual/en/function.strpos.php