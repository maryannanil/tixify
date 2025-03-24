document.getElementById('verification-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const ticketId = document.getElementById('ticket-id').value;
    const fileInput = document.getElementById('ticket-file');
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append('ticket_id', ticketId);
    if (file) {
        formData.append('file', file);
    }

    // ✅ FETCH call to Flask backend
    const response = await fetch('http://127.0.0.1:8000/validate_ticket', {  // ✅ Only the endpoint
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('result').innerHTML = data.message;
});
