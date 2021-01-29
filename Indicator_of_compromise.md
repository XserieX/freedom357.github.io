# Indicator of compromise


<img src ="IOC.jpg" width ="100%" hight = "100%">

Indicator of compromise (IoC) ในทาง computer forensics คือการเฝ้าดูสิ่งที่สร้างขึ้นในเครือข่ายและระบบปฎิบัติการนั้นๆ แล้วสรุปได้ว่าเป็นการถูกโจมตี

## Types of indication

1. รูปแบบของไวรัส [(virus signatures)](https://en.wikipedia.org/wiki/Computer_virus)
2.  IP addresses, MD5 hashes ของ มัลแวร์
3.  URLs or domain names ของ บอทเน็ต C2  

## ตัวอย่าง

1. การปริมาณข้อมูลเครือข่ายขาออกผิดปกติ(Unusual Outbound Network Traffic)
2. บัญชีผู้ใช้ที่มีสิทธิ์สูงที่มีลักษณะกิจกรรมที่ผิดปกติ

การวิเคราะห์สัญญาณบ่งชี้การบุกรุก (Indicator of Compromise ;IOCs) 

3. การเข้าใช้ระบบจากสถานที่ที่แตกต่างหรือผิดปกติ(Geographical Irregularities)

4. การล็อคอินผิดพลาดจนระบบเตือน(Other Log-In Red Flags)

5. ปริมาณการอ่านฐานข้อมูลเพิ่มสูงขึ้น(Swells in Database Read Volume)

6. ขนาดของการตอบกลับหน้าเว็บ(HTML Response Sizes)

7. ข้อมูลไฟล์เดียวกัน มีการเรียกดูจำนวนมาก(Large Numbers of Requests for The Same File)

8. โปรแกรมมีการเชื่อมต่อพอร์ตที่ผิดปกติ(Mismatched Port Application Traffic)

9. การเปลี่ยนแปลงรีจิสทรีหรือไฟล์ระบบที่น่าสงสัย(Suspicious Registry or System File Changes)

10. การเรียกข้อมูล DNS ที่ผิดปกติ(DNS Request Anomalies)

11. การแพตช์อย่างไม่มีเหตุผล (Unexpected Patching of Systems)

12. การโจมตีที่มีการย้ายฐานการโจมตี ขึ้นบนแพลตฟอร์มอุปกรณ์พกพา(Mobile Device Profile Changes)

13. ข้อมูลบางชุดถูกวางไว้ในที่ไม่ควรอยู่ (Bundles of Data in The Wrong Places)

14. การใช้งาน เว็บแบบผิดปกติที่ไม่น่ามีผู้ใช้งานทั่วไปใช้งานในลักษณะนั้น (Web Traffic with Unhuman Behavior)

15. DDoS อาจจะเป็นอีกหนึ่งสัญญาณที่บ่งบอกว่าระบบโดนโจมตี (Signs of DDoS Activity)


## ในการใช้งาน 


## อ้างอิง
+ [secureinfo](https://www.secureinfo.co.th/index.php?page=article-detail&topic_id=13)
+ [wikipedia](en.wikipedia.org/wiki/Indicator_of_compromise)