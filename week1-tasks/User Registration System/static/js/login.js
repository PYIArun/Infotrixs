document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("registration-form");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
  
    form.addEventListener("submit", function(event) {
      const emailValue = emailInput.value.trim();
      const passwordValue = passwordInput.value;
  
      // Validate Email Format
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailValue)) {
        event.preventDefault();
        alert("Invalid email format.");
      }
  
      if (passwordValue.length < 8) {
        event.preventDefault();
        alert("Password should be at least 8 characters long.");
      }
  
    });
  });
  