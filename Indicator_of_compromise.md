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

เหตุการที่เราจะต้องการ IOC มาช่วยในการวิเคราะห์ในการตัดสินใจว่า เมื่อเราโดนโจมตี จากภัยคุกคามใด และต้องการที่จะทราบ สาเหตุ ของเหตุการณ์ ที่เกิดขึ้น โดย สืบมองย้อนกลับไป (Forensic) มาช่วย วิเคราะห์หาสาเหตุ และแนวทางในการป้องกัน ไม่ให้เกิดขึ้นอีก และ คำถาม IOC นี้ เอามาจากไหน
ในมุมมองของผู้เขียน
1. ซื้อมา
2. เขียนเอง

ผมจะขออธิบายข้อ2.แล้วกัน 
เราจะเขียน IOC แล้วมีเครื่องมือที่ใช้เขียน 
ในการเขียน IOC อาจจะมีเครื่องมือที่หลากหลาย ผมจะมาอธิบาย ตัวที่ ผู้เขียน ใช้ แล้วกันครับ
[IOC Editor](https://www.fireeye.com/content/dam/fireeye-www/services/freeware/ug-ioc-editor.pdf)
ผมจะขอเขียนในขอบเขตที่ กว้าง ไม่ลงลึกถึงว่า หาเคส อย่างไงเขียนแบบไหน จะพูดในภาพกว้างๆ
1. ก่อนอื่น เมื่อเราทราบว่า เครื่องเราติดไวรัส ชื่ออะไร จาก antivirus หรือ เครื่ีองมือที่ตรวจสอบว่าเราบอกว่าเราติดอะไร ทำให้เครื่องคอมเราใช้งานผิดปกติ
2. คำถามต่อมา เราอยากทราบว่า มันเกิดขึ้นมาได้อย่างไร
เราจะทำการ สืบสวน สอบสวน โดยใช้เครื่องมือในการ นำการทำงานต่างๆใน หน่วยความจำออกมา ในที่นี้ใช้ [redline](https://www.fireeye.com/services/freeware/redline.html) ไปลองเอามาใช้ดู

3. หา VDO หรือคู่มือการใช้งาน ของ Tool มาศึกษาดู
4. เราจะใช้ redline ในการ dump memory ออกมาวิเคราะห์ เพื่อหา ช่วงเวลาที่เกิดเหตุการณ์ ที่เราสนใจ  
5. ตอนนี้เราต้องการที่จะใช้งาน IOC แล้ว เพื่อมาช่วยให้เรา หาเหตุการณ์ ที่เราสนใจ
6. ไล่ลำดับเหตุการณ์ ที่เกิดขึ้น และทำการวิเคราะห์ เพื่อตรวจสอบ หรือ หยุดการโจมตี และหาทางออกเพื่อให้ตรวจพบได้เร็วยิ่งขึ้น

## อ้างอิง
+ [secureinfo](https://www.secureinfo.co.th/index.php?page=article-detail&topic_id=13)
+ [wikipedia](en.wikipedia.org/wiki/Indicator_of_compromise)