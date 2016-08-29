<?php

if (isset($_GET['fahrenheit'])) {
    $fahrenheit = $_GET['fahrenheit'];
} else {
    die('No degrees in Fahrenheit provided.');
}
$celsius = ($fahrenheit - 32) * 5 / 9;
echo floor($celsius);
