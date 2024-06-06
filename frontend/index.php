<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="post" action="add_user.php">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Register">
    </form>
    <h2>Registered Users</h2>
    <?php
    $response = @file_get_contents('http://backend:5000/api/users');
    if ($response === FALSE) {
        echo '<p>Error retrieving users. Please try again later.</p>';
    } else {
        $users = json_decode($response, true);
        if (is_array($users)) {
            echo '<ul>';
            foreach ($users as $user) {
                echo '<li>' . htmlspecialchars($user[1]) . '</li>';
            }
            echo '</ul>';
        } else {
            echo '<p>No users found.</p>';
        }
    }
    ?>
</body>
</html>
