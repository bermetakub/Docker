<?php
$username = $_POST['username'];
$password = $_POST['password'];

$data = array('username' => $username, 'password' => $password);
$options = array(
    'http' => array(
        'header'  => "Content-type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);
$context  = stream_context_create($options);
$result = file_get_contents('http://backend:5000/api/users', false, $context);

if ($result === FALSE) {
    die('Error');
}

header('Location: index.php');
?>
