# personal_vaccine_tracker
Python code to track vaccine slot availability 

**Purpose**
- Uses Public APIs provided at Co-Win website to fetch results using pincode and date
- Uses asyncio to run URL queries in parallel for a span of current date to current date+3months
- When Json data is received back with 200OK, script pushes the required details using Telegram Bot API
- The update is received as a notification message to end user(That is Me!!!!)


