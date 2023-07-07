document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("registration-form");
    const firstNameInput = document.getElementById("first-name");
    const lastNameInput = document.getElementById("last-name");
    const emailInput = document.getElementById("email");
    const phoneInput = document.getElementById("phone");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");
  
    form.addEventListener("submit", function(event) {
      const firstNameValue = firstNameInput.value.trim();
      const lastNameValue = lastNameInput.value.trim();
      const emailValue = emailInput.value.trim();
      const phoneValue = phoneInput.value.trim();
      const passwordValue = passwordInput.value;
      const confirmPasswordValue = confirmPasswordInput.value;
  
      if (firstNameValue === "" || firstNameValue.length < 3) {
        event.preventDefault();
        alert("First Name should be at least 3 characters long.");
      }
  
      if (lastNameValue === "" || lastNameValue.length < 3) {
        event.preventDefault();
        alert("Last Name should be at least 3 characters long.");
      }
  
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailValue)) {
        event.preventDefault();
        alert("Invalid email format.");
      }
  
      const phoneRegex = /^\d{10}$/;
      if (!phoneRegex.test(phoneValue)) {
        event.preventDefault();
        alert("Phone Number should be 10 digits.");
      }
  
      if (passwordValue.length < 8) {
        event.preventDefault();
        alert("Password should be at least 8 characters long.");
      }
      
      if (passwordValue !== confirmPasswordValue) {
        event.preventDefault();
        alert("Passwords do not match.");
      }
    });
  });
  