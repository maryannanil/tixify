# Tixify API Endpoints

### 1. Health Check
- **Route:** `/`
- **Method:** GET
- **Description:** Confirms that the backend is running.
- **Response:** 
```json
{ "message": "Tixify backend is live!" }

### 2. Verify Ticket
Route: /verify-ticket
Method: POST
Description: Checks if a ticket is legitimate.

{
  "ticket_id": "123ABC",
  "source": "official"
}

{
  "status": "Valid",
  "message": "Ticket is from an authorized source."
}

### 3. Push this new doc to GitHub:
```bash
git add docs/api_endpoints.md
git commit -m "Added API endpoints documentation"
git push