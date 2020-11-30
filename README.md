Name | Mr. Soontorn Janphuk
E-mail | freedom44357@gmail.com 
Tel.| 087-505-4494
Birtday | 24 April

Education ==> | Bachelor’s Degree in Computer Engineering, King Mongkut’s Institute of Technology Ladkrabang,Thailand
<img src ="picture.jpg" width = "50%" hight = "50%">
AKA
var AsciiBanner = require('ascii-banner');	

// simple banner
AsciiBanner
.write('freedom1')
.out();

// add color
AsciiBanner
.write('freedom2')
.color('red')
.out();

// change font
AsciiBanner
.write('freedom3')
.color('red')
.font('Thin')
.out();

// add app version number (aligned right)
AsciiBanner
.write('freedom4')
.color('red')
.font('Thin')
.after('>v{{version}}', 'yellow')
.out();

// add app name before (centered)
AsciiBanner
.write('freedom5')
.color('red')
.font('Thin')
.after('>v{{version}}', 'yellow')
.before('>[{{name}}<')
.out();

















