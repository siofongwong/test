function logIn() {
    var usr = document.getElementById("your_name").value;

    if (usr == "") {
        alert("Please enter valid information");
        return false;
    } else {
      return true;
    }
}