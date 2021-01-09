<?php
$item = "Zak's Laptop";
$escaped_item = mysqli_escape_string($item);
printf("Escaped string: %s\n", $escaped_item);
?>