document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Simple validation
    if (username === "admin" && password === "admin123") {
        alert("Login successful!");
        window.location.href = "admin.html"; // Redirect to admin dashboard
    } else {
        alert("Invalid credentials!");
    }
});
