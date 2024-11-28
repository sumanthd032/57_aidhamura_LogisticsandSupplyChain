// JavaScript to handle real-time updates, form validation, and interaction on the dashboard

// Example function for form validation
function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input, textarea');

    inputs.forEach(input => {
        if (input.required && !input.value.trim()) {
            isValid = false;
            input.style.borderColor = 'red';
            alert(`${input.name} is required!`);
        } else {
            input.style.borderColor = '';
        }
    });

    return isValid;
}

// Example function for handling form submission
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if (validateForm(form)) {
            form.submit();
        }
    });
});

// Example for dynamically updating the dashboard data (mock data)
function updateDashboard() {
    fetch('/api/dashboard-data')
        .then(response => response.json())
        .then(data => {
            document.querySelector('.dashboard-item1').innerHTML = `
                <h3>New Orders</h3>
                <p>${data.newOrders}</p>
            `;
            document.querySelector('.dashboard-item2').innerHTML = `
                <h3>Total Revenue</h3>
                <p>$${data.totalRevenue}</p>
            `;
            document.querySelector('.dashboard-item3').innerHTML = `
                <h3>Food Wasted</h3>
                <p>${data.foodWasted} kg</p>
            `;
        })
        .catch(error => console.error('Error fetching dashboard data:', error));
}

// Refresh dashboard data every 5 minutes
setInterval(updateDashboard, 300000);

// Function for toggling modals
function toggleModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        modal.style.display = 'block';
    }
}

// Add event listeners for modals
document.querySelectorAll('.open-modal').forEach(button => {
    button.addEventListener('click', function() {
        const modalId = button.getAttribute('data-modal');
        toggleModal(modalId);
    });
});

document.querySelectorAll('.close-modal').forEach(button => {
    button.addEventListener('click', function() {
        const modal = button.closest('.modal');
        if (modal) modal.style.display = 'none';
    });
});

// Example function to display a notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Example usage of the notification function
showNotification('Welcome to the Zero Plate Dashboard!', 'success');

// Function to toggle the visibility of modals
function toggleModal(modalId, action) {
    const modal = document.getElementById(modalId);
    if (action === 'show') {
        modal.style.display = 'block';
    } else {
        modal.style.display = 'none';
    }
}

// Event listener for closing modals
document.querySelectorAll('.modal .close').forEach((btn) => {
    btn.addEventListener('click', function() {
        const modal = this.closest('.modal');
        toggleModal(modal.id, 'hide');
    });
});

// Function to show notifications
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;

    // Append notification to the body
    document.body.appendChild(notification);

    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Example usage: Show a notification
// showNotification('Form submitted successfully!', 'success');

// Form submission logic (example: async form submission)
document.querySelectorAll('form').forEach((form) => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);

        // Example async request (use fetch for real requests)
        fetch('/submit-form-url', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification('Form submitted successfully!', 'success');
            } else {
                showNotification('Error submitting form. Please try again.', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showNotification('An unexpected error occurred.', 'error');
        });
    });
});

// Toggle the visibility of the dashboard modal
document.querySelectorAll('.dashboard-item').forEach((item) => {
    item.addEventListener('click', function() {
        const modalId = this.dataset.modalId;
        toggleModal(modalId, 'show');
    });
});
