# in_array


HTTP Response Splitting
vulnerability concept:
source		sink		vulnerability
$_GET
+
header()	
=
HTTP Response Splitting
vulnerability description:
An attacker can inject arbitrary headers to the HTTP response header. This can be abused for a redirect when injecting a "Location:" header or help within a session fixation attack when the "Set-Cookie:" header is added. Additionally, the HTTP response can be overwritten and JavaScript can be injected leading to Cross-Site Scripting attacks. In PHP version below 4.4.2 or 5.1.2 the characters \n\r (LF CR) can be used for header line termination (cross-browser). In PHP below 5.4 the character \r (CR) can still be used for header line termination (Chrome, IE).

More information about HTTP Response Splitting can be found here.

vulnerable example code:
1: header("Location: " . $_GET["url"]);  
proof of concept:
/index.php?url=a%0a%0dContent-Type:%20text/html%0a%0d%0a%0d<script>alert(1)</script>

patch:
Update PHP to prevent header injection or implement a whitelist.

1: if(!in_array($_GET["url"],  $whitelist)) exit ;  
related securing functions:
None.