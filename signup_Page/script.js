function createAccount() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var username = document.getElementById('username').value;

    var errorMessage = document.getElementById('error-message');
    var successMessage = document.getElementById('success-message');

    if (!email || !password || !username) {
        errorMessage.innerHTML = 'Please fill in all the fields.';
        successMessage.innerHTML = '';
    } else {
        errorMessage.innerHTML = '';
        successMessage.innerHTML = 'Account created for ' + username + ' with email: ' + email;
    }
}
