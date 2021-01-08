mysql_escape_string
===================


 **mysql_escape_string** คือ ฟังก์ชันที่ใช้ในการหลบเลี่ยง สตริืงที่ใช้กับ mysql query จะมีฟังก์ชันนี้ต้องแต่ (PHP 4 >= 4.0.3, PHP 5)

 **การใช้งาน**

    mysql_escape_string ( string $unescaped_string ) : string



ฟังก์ชันนี้ จะทำการหลบเลี่ยงของสตริง ที่ส่งผลให้กับการทำงานในการ query mysql  ซึ่งอาจจะเป็นผลในทางที่ไม่ดีได้

***ตัวอย่าง*** 

    <?php
    $item = "My name 's freedom357";
    $escaped_item = mysql_escape_string($item);
    printf("Escaped string: %s\n", $escaped_item);
    ?>
