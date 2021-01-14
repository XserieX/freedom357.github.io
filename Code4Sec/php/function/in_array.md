# in_array

<img src ="CRFL.png" width ="100%" hight = "100%">


***in_array***

คือฟังก์ชันที่ใช้ตรวจสอบค่าว่ามีอยู่ในอาร์เรย์หรือไม่โดยจะ return คือเป็น true กับ false

***ตัวอย่าง***

    in_array ( mixed $needle , array $haystack , bool $strict = false ) : bool


***ตัวอย่าง***
+ code

        <?php
        $os = array("CRLF", "sec", "Inj", "ection");
        if (in_array("CRLF", $os)) {
        echo "Got CRLF";
        }
        if (in_array("Injection", $os)) {
        echo "Got Injed";
        }
        ?>

+ output
    
        Got CRLF

***การประยุกต์ใช้งาน***

[CRLF Injection](https://snownekoblog.wordpress.com/2017/06/30/crlf-injection/#:~:text=CRLF%20%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B9%87%E0%B8%84%E0%B8%B7%E0%B8%AD%20%E2%80%9CCarriage,%E0%B8%AA%E0%B8%B4%E0%B9%89%E0%B8%99%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%9A%E0%B8%A3%E0%B8%A3%E0%B8%97%E0%B8%B1%E0%B8%94%E0%B8%95%E0%B8%A3%E0%B8%87%E0%B9%84%E0%B8%AB%E0%B8%99%E0%B8%99%E0%B8%B1%E0%B9%88%E0%B8%99%E0%B9%80%E0%B8%AD%E0%B8%87)
CRLF หรือก็คือ “Carriage Return”+”Line Feed” เป็นOperatorsที่ทำให้เราสามารถควบคุมการแสดงผลแบบStringโดยใช้Escape Sequenceช่วยเหลือได้ โดยเป็นตัวที่ทำหน้าที่บอกให้คอมพิวเตอร์รู้ว่าตรงไหนคือ End of Line หรือสิ้นสุดบรรทัดตรงไหนนั่นเอง


[HTTP Response Splitting](http://libdoc.dpu.ac.th/thesis/Piya.Art.pdf)
Web application แบบไดนามิกจะกำหนดค่าในส่วนของ header fields เพื่อตอบสนอง
HP บนพื้นฐานของคำผ่านพารามิเตอร์ภายนอก ยกตัวอย่างเช่นการเปลี่ยนเส้นทาง HTIP จะ
ดำเนินการโดยการตั้งค่าการเปลี่ยนเส้นทางไปยัง URL ที่ระบุในพารามิเตอร์ไปยังตำแหน่งของ
Header fields หรือ web application อาจจะตั้งชื่อที่ป้อนในกระดานข่าวไปยัง Cookie header filed
หากกระบวนการของการสร้างส่วนหัวของให้ตอบสนองต่อ HTTP ในการใช้งานเว็บดังกล่าวมี
ช่องโหว่ที่ผู้โจมตีสามารถเพิ่ม header field เพื่อจัดการเนื้อหาการตอบสนองและมี web application
เพื่อสร้างการตอบสนองในหลายรูปแบบ ปัญหานี้จะเรียกว่า "HTTP Header Injection vulnerability"
และวิธีการในการโจมตีจากการใช้ประ โยชน์จากช่องโหว่นี้ถูกเรียกว่า "HTTP Header Injection
Attack" โดยฉพาะอย่างยิ่งการโจมตีที่นำไปสู่การสร้างการตอบสนองต่อ web application ได้หลาย


***ตัวอย่างที่มีช่องโหว่***

    1: header("Location: " . $_GET["url"]);  

***ทดสอบเจาะ***

    /index.php?url=a%0a%0dContent-Type:%20text/html%0a%0d%0a%0d<script>alert(1)</script>

***การใช้งานประยุกต์***

อัฟเดรต PHP ถึงการป้องกันในส่วน header injection หรือ ทำ whitelist


    1: if(!in_array($_GET["url"],  $whitelist)) exit ;  
    related securing functions:
    None.

***อ้างอิง***
+ https://snownekoblog.wordpress.com/2017/06/30/crlf-injection/
+ http://libdoc.dpu.ac.th/thesis/Piya.Art.pdf
+ https://3v4l.org/#preview
+ https://www.php.net/manual/en/function.in-array.php

