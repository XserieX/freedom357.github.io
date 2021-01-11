# urldecode
<img src ="Cross-site-scripting-XSS-guide.png" width ="80%" hight = "80%">



***urldecode*** 
เป็นการถอดรหัสของ URL กับ เข้ารหัสสตริง

**การใช้งานของฟังก์ชัน**

    urldecode ( string $string ) : string

การทำงานจะเป็นรูปแบบที่ง่ายมาก ใส่สตริงเข้าไปที่ อาร์กิวเมนต์ ที่รับค่าเป็น สตริง

**ลองใช้งาน**

    <?php
    $test = urlencode("http://192.168.43.129/bWAPP/xss_get.php?firstname=Soontorn&lastname=Janphuk&form=submit");
    echo urldecode($test);
    ?>

**ผลลัพธ์**

+ ***encode***

        http%3A%2F%2F192.168.43.129%2FbWAPP%2Fxss_get.php%3Ffirstname%3DSoontorn%26lastname%3DJanphuk%26form%3Dsubmit

+ ***decode***


        http://192.168.43.129/bWAPP/xss_get.php?firstname=Soontorn&lastname=Janphuk&form=submit


**การประยุกต์การใช้งาน**

+ Input Validation security level low 

        function no_check($data) {    
        return $data;
        }

**ในมุมของความปลอดภัย**

ในช่องทางของความปลอดภัยเว็บไซด์นั้น วิธีการในการ โจมตี ได้หลากหลายรูปแบบ เช่น injection, XSS เป็นต้น 
ใน ฟังก์ชัน urlencode(),urldecode() จะช่วยในการตรวจสอบในกรณีที่ ผู้ใช้งานกรอกข้อมูลเข้ามาในระบบ การตรวจสอบนี้เรียกว่า ***Input Validation*** เทคนิคในการโจมตี [XSS](https://blog.tamacorp.co/xss/)

+ Input Validation security level medium

        // Input Validation
    function xss_check_1($data) {
        // Converts only "<" and ">" to HTLM entities    
        $input = str_replace("<", "&lt;", $data);
        $input = str_replace(">", "&gt;", $input);
        
        // Failure is an option
        // Bypasses double encoding attacks   
        // <script>alert(0)</script>
        // %3Cscript%3Ealert%280%29%3C%2Fscript%3E
        // %253Cscript%253Ealert%25280%2529%253C%252Fscript%253E
        $input = urldecode($input);
        
        return $input;
    }

**อ้างอิง**
+ https://blog.tamacorp.co/xss/
+ https://www.php.net/manual/en/function.urldecode.php
+ https://sites.google.com/view/oxdeca/security-pentesting/bwapp/bwapp-injection#h.p_hQjwKigho_W2
+ https://3v4l.org/#live