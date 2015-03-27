function createProject() {
    var title = document.getElementById("title").value;
    var git_link = document.getElementById("git_link").value;

    if (title == "" || git_link == "") {
        alert("Please enter valid information");
        return false;
    } else {
        return true;
    }
}