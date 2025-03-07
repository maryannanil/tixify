document.getElementById("ticketForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const ticketId = document.getElementById("ticketId").value;
    
    if(ticketId === "ZAYN001") {
      document.getElementById("result").innerText = "✅ Valid ticket for Zayn Malik Live!";
    } else {
      document.getElementById("result").innerText = "❌ Fake or invalid ticket!";
    }
  });
  