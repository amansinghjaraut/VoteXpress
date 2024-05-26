import requests
import random

def send_otp(mobile_number):
    # Generate a random 6-digit OTP
    otp = ''.join(random.choices('0123456789', k=6))

    # Your Fast2SMS API key
    api_key = 'O1c4ev7nJZ6MIu05NYWQ3dpoyHwURChlqgr2GFDPAxiBzKLkfVQF7JXwWaKRoSHYzj3hpg0CvkdnlDyu'

    # Construct the request payload
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = {
        "authorization": api_key,
        "sender_id": "FSTSMS",
        "message": f"Your OTP is: {otp}",
        "language": "english",
        "route": "p",
        "numbers": mobile_number
    }

    # Send the POST request to Fast2SMS API
    response = requests.post(url, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        print("OTP sent successfully!")
    else:
        print("Failed to send OTP")
        print(response.text)  # Print the error response for debugging
        # Example usage:
        mobile_number = input("Enter your mobile number (including country code): +918956688305")
        send_otp(mobile_number)
        

