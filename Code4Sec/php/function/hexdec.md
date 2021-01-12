# Hexdec

<img src ="hexdec.jpg" width ="100%" hight = "100%">


***Hexdec()***
คือฟังก์ชัน ที่ใช้แปลงเลขฐาน 16 เป็นเลขฐาน 10 

**การใช้งาน**

    hexdec ( string $hex_string ) : int|float

ค่าที่ใส่ไป $hex_string ฟังก์ชันนี้ จะแปลงค่าที่อยู่ในตัวแปรที่ใส่ไปมันจะ แปลงค่าเป็นเลขฐานสิบถ้

**ตัวอย่างการใช้งาน**

        <?php
    var_dump(hexdec("Seeurity"));
    var_dump(hexdec("ee"));
    // both print "int(238)"

    var_dump(hexdec("that")); // print "int(10)"
    var_dump(hexdec("a0")); // print "int(160)"
    ?>

จะเป็นได้ว่า ค่าจะถูกแปลงเป็น ค่า ​int(238) เหมือนกันทั้งคู่ ในฟังก์ชันนี้จะสนใจ เฉพาะ ตัวเลขฐานสิบหก 

**ผลลัพธ์**

        Deprecated: Invalid characters passed for attempted conversion, these have been ignored in /tmp/preview on line 2
    int(238)
    int(238)

    Deprecated: Invalid characters passed for attempted conversion, these have been ignored in /tmp/preview on line 6
    int(10)
    int(160)

 ผลลัพธ์ที่ได้มันจะสนใจแค่ตัวเลขที่จะสามารถถูกแปลงเป็นเลขฐานสิบหกมาเป็นเลขฐานสิบ เท่านั้น นอกนั้นมันจะแจ้งเตือนว่าบรรทัดไหนมีปัญหา แต่ก็ยังสามารถให้ค่าแปลงออกมาได้ แต่จะแจ้ง ค่า Deprecated หมายถึงมันไม่รับค่าที่ไม่ใช่เลขฐานสิบหก แต่มันจะปล่อยผ่านไปแล้วแสดงค่าออกมา


 **ในการประยุกต์ใช้งาน**

 ในทางด้านความปลอดภัยจะใช้ ฟังก์ชัน ***hexdec()***เป็นส่วนประกอบในการแปลงเลขฐาน และจะใช้ เพื่อประกอบการตั้งค่าการควบคุมการเข้าถึงทรัพยากรในระบบ เช่นการใช้งาน Share Files หรือ ทรัพยากรอื่น ๆ ในระบบ

        // Returns the textual SID
    function bin_sid_to_text($binsid)
    {
        
        $hex_sid = bin2hex($binsid);
        $rev = hexdec(substr($hex_sid, 0, 2));// Gets the revision-part of the SID
        $subcount = hexdec(substr($hex_sid, 2, 2));// Gets count of sub-auth entries
        $auth = hexdec(substr($hex_sid, 4, 12));// SECURITY_NT_AUTHORITY
        $result = "$rev-$auth";
        
        // Retrieves the full SID
        /*
        for($x=0; $x<$subcount; $x++)
        {

            $subauth[$x] = hexdec(little_endian(substr($hex_sid, 16+($x*8), 8)));  // Gets all SECURITY_NT_AUTHORITY
            $result.= "-" . $subauth[$x];

        }
        */ 
        
        // Retrieves only the last part of the SID = '$subcount-1'
        $result = hexdec(little_endian(substr($hex_sid, 16+(($subcount-1)*8), 8)));
            
        return $result;


**อ้างอิง**

+ https://3v4l.org/#live
+ https://www.php.net/manual/en/function.hexdec
+ http://www.mvpskill.com/kb/%E0%B8%95%E0%B8%B2%E0%B8%A3%E0%B8%B2%E0%B8%87%E0%B8%84%E0%B9%88%E0%B8%B2-sid-%E0%B8%82%E0%B8%AD%E0%B8%87-user-account-%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99.html#:~:text=Security%20Identifier%20(SID)%20%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B8%84%E0%B9%88%E0%B8%B2,%E0%B8%97%E0%B8%A3%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%B7%E0%B9%88%E0%B8%99%20%E0%B9%86%20%E0%B9%83%E0%B8%99%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A)