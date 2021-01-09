mysql_escape_string
===================



<img src ="phpSecurityBanner1.png" width ="100%" hight = "100%">


 **mysql_escape_string** คือ ฟังก์ชันที่ใช้ในการหลบเลี่ยง สตริงที่ใช้กับ mysql query จะมีฟังก์ชันนี้ต้องแต่ (PHP 4 >= 4.0.3, PHP 5)

 **การใช้งาน**

    mysql_escape_string ( string $unescaped_string ) : string



ฟังก์ชันนี้ จะทำการหลบเลี่ยงของสตริง ที่ส่งผลให้กับการทำงานในการ query mysql  ซึ่งอาจจะเป็นผลในทางที่ไม่ดีได้

***ตัวอย่าง*** 

    <?php
    $item = "or'='1'='1";
    $escaped_item = mysql_escape_string($item);
    printf("Escaped string: %s\n", $escaped_item);
    ?>

***ผลลัพธ์***


    Escaped string: or\'=\'1\'=\'1

***ประยุกต์ใช้งาน***

จากที่ได้เห็น เราสามารถเอามาประยุกต์ใช้งาน เกี่ยวกับ การหลบเลี่ยงของสตริง ที่ผู้ไม่ประสงค์ดี (hacker) ที่ใช้เทคนิคในการเจาะระบบ ทำให้ข้อมูลเกิดความเสียหาย 


***ตัวอย่าง ที่มีช่องโหว่***

$title = $_REQUEST["title"];

    $sql = "SELECT * FROM movies WHERE title = '" . sqli($title) . "'";

    $recordset = mysql_query($sql, $link);

จะเห็นได้ว่า มีการส่ง ข้อมูลจากผู้ไม่ประสงค์ดี เข้ามา เช่น 'or'1'='1 จะทำให้เห็นข้อมูลใน mysql ทั้งหมด ซึ่ง ผู้ไม่ประสงต์ดีนั้นสามารถทำอะไรกับข้อมูลในระบบ ได้หมด


***ในทางแก้ไข***

$title = $_REQUEST["title"];


     
    $sql = "SELECT * FROM movies WHERE title = '" . sqli($title) . "'";
    
    $recordset = mysql_escape_string($sql, $link);


จะเห็นว่าใช้ฟังก์ชัน mysql_escape_string()แก้ปัญหา นี้ได้ แต่จะใช้ได้กับ PHP 4 >= 4.0.3, PHP 5

ถ้าเป็น PHP5,PHP7 จะใช้ฟังก์ชันmysqli_escape_string แทน
 
***อ้างอิง***
- <https://3v4l.org/RZmjH#v500>
- <https://www.php.net/manual/en/function.mysql-escape-string>

