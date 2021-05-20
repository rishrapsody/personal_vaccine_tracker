# personal_vaccine_tracker
Python code to track vaccine slot availability In India


Purpose
- Uses Public APIs provided at Co-Win website to fetch results using pincode and date
- Uses asyncio to run URL coroutine queries function for periof of current date to current date+3months
- Parses JSON data and pushes the required details using Telegram Bot API
- The update is received as a notification message to end user(That is Me!!!!)
