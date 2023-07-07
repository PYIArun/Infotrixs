document.addEventListener('DOMContentLoaded', function() {
    const cancelBtn = document.getElementById('cancelBtn');
  
    cancelBtn.addEventListener('click', function() {
      window.location.href = '/profile';
    });
  
    const profileForm = document.getElementById('profileForm');
  
    profileForm.addEventListener('submit', function(event) {
  
      const firstName = document.getElementById('firstName').value.trim();
      const lastName = document.getElementById('lastName').value.trim();
      // const email = document.getElementById('emailInput').value.trim();
      const phone = document.getElementById('phoneInput').value.trim();
      const passwordValue = document.getElementById('passwordInput').value;
      const confirmPasswordValue = document.getElementById('confirmPasswordInput').value;

      if (firstName.length < 3 || lastName.length < 3) {
        event.preventDefault();
        alert('First name and last name must be at least 3 characters long.');
      }
      
      if (phone.length !== 10 || isNaN(phone)) {
        event.preventDefault();
        alert('Please enter a valid 10-digit phone number.');

      }
      if (passwordValue.length < 8) {
        event.preventDefault();
        alert("Password should be at least 8 characters long.");
      }

      if (passwordValue !== confirmPasswordValue) {
        event.preventDefault();
        alert("Passwords do not match.");
      }
  
      // document.getElementById('name').textContent = `${firstName} ${lastName}`;
      // document.getElementById('email').textContent = email;
      // document.getElementById('phone').textContent = phone;
  
      // alert('Profile updated successfully!');
    });
  });
  
  // Function to validate email format
  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }
  