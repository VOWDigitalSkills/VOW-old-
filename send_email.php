<!-- filepath: c:\Users\Ashwa\Downloads\AWS\AWS\send_email.php -->
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $mobile = $_POST['mobile'];
    $it_member = $_POST['it_member'];
    $date = $_POST['date'];
    $time = $_POST['time'];
    $problem = $_POST['problem'];

    $to = "VOWsupport@gmail.com";
    $subject = "New Appointment Request";
    $message = "Name: $name\nEmail: $email\nMobile: $mobile\nIT Member: $it_member\nDate: $date\nTime: $time\nProblem: $problem";
    $headers = "From: $email";

    if (mail($to, $subject, $message, $headers)) {
        echo "Email sent successfully!";
    } else {
        echo "Failed to send email.";
    }
}
?>