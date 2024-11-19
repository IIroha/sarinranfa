  
<script>
        document.getElementById('cardRequestForm').addEventListener('submit', function(event) {
            event.preventDefault();

            // Clear previous errors
            document.getElementById('customerNameError').innerText = '';
            document.getElementById('cifNumberError').innerText = '';
            document.getElementById('contactNumberError').innerText = '';
            document.getElementById('successMessage').innerText = '';

            // Retrieve form values
            let customerName = document.getElementById('customerName').value.trim();
            let cifNumber = document.getElementById('cifNumber').value.trim();
            let contactNumber = document.getElementById('contactNumber').value.trim();
            let requestTypes = document.querySelectorAll('input[name="requestType"]:checked');
            let cardTypes = document.querySelectorAll('input[name="cardType"]:checked');

            // Form validation
            let isValid = true;

            if (customerName === '') {
                document.getElementById('customerNameError').innerText = 'Customer name is required.';
                isValid = false;
            }

            if (cifNumber === '') {
                document.getElementById('cifNumberError').innerText = 'CIF number is required.';
                isValid = false;
            }

            if (contactNumber === '') {
                document.getElementById('contactNumberError').innerText = 'Contact number is required.';
                isValid = false;
            }

            if (requestTypes.length === 0) {
                alert('Please select at least one request type.');
                isValid = false;
            }

            if (cardTypes.length === 0) {
                alert('Please select at least one card type.');
                isValid = false;
            }

            // If valid, show success message
            if (isValid) {
                document.getElementById('successMessage').innerText = 'Form submitted successfully!';
                // Reset form if needed
                // document.getElementById('cardRequestForm').reset();
            }
        });
    </script>
</body>
</html>
