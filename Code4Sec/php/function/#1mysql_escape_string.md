mysql_escape_string
===================


 **mysql_escape_string** คือ ฟังก์ชันที่ใช้ในการหลบเลี่ยง สตริืงที่ใช้กับ mysql query จะมีฟังก์ชันนี้ต้องแต่ (PHP 4 >= 4.0.3, PHP 5)

 **การใช้งาน**

    mysql_escape_string ( string $unescaped_string ) : string



ฟังก์่ชันนี้ จะทำการหลบเลี่ยง

This function will escape the unescaped_string, so that it is safe to place it in a mysql_query(). This function is deprecated.

This function is identical to mysql_real_escape_string() except that mysql_real_escape_string() takes a connection handler and escapes the string according to the current character set. mysql_escape_string() does not take a connection argument and does not respect the current charset setting.