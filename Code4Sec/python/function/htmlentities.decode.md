# htmlentities encode

<img src ="HTMLEntities.jpg" width ="100%" hight = "100%">

***htmlentities***

ฟังก์ชันสำหรับใช้แปลงเครื่องหมายพิเศษต่าง ๆ ที่ตรงกับ tag ของภาษาHTML ให้เป็นรหัสอักษรที่ใช้ในภาษา HTML เช่น "<" เป็น "&lt;"

ในการใช้งาน ใน ***python*** นั้นจะต้องทำการติดตั้งก่อน

**ติดตั้ง**

    $ [sudo] pip install htmlentities


**การใช้งาน**
   + ***encoding***
        
        สามารถที่จะเข้ารหัสด้วย ***htmlentitie.encode()*** ด้วยวิธิการ เข้ารหัส

                    import htmlentities

                    htmlentities.encode('<') # returns "&lt"
   + ***decoding***
        สามารถถอดรหัสด้วย ***htmlentitie.decode()*** ด้วยวิธีการ ถอดรหัส

                import htmlentities

                htmlentities.decode('&lt') # returns "<"
    

***การนำประยุกต์ใช้งาน***

Cross-site Scripting ชื่อย่อว่า XSS เป็นชนิดของการช่องโหว่ที่ถูกจัดให้อยู่ในลำดับที่ 3 ของ OWASP TOP 10 2017 โดยเว็บแอปพลิเคชันที่มีช่องโหว่ประเภทนี้ อนุญาตให้ผู้ไม่หวังดีสามารถใส่ JavaScript ให้ทำงานภายใต้ domain ของเป้าหมาย ดังนั้น ผู้ไม่หวังดีสามารถใช้ XSS เพื่อขโมยข้อมูลของผู้ใช้งานคนอื่นได้ 
การป้องกัน
[XSS prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)


***อ้างอิง***

+ https://pypi.org/project/htmlentities/
+ https://blog.tamacorp.co/xss/#:~:text=Cross%2Dsite%20Scripting%20%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B9%88%E0%B8%B2,%E0%B8%9A%E0%B8%97%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%99%E0%B8%B5%E0%B9%89%E0%B8%88%E0%B8%B0%E0%B8%AD%E0%B8%98%E0%B8%B4%E0%B8%9A%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%B2%E0%B8%A2
+ https://stackoverflow.com/questions/11378645/preventing-a-security-breach