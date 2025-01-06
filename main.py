import requests
import time
from datetime import datetime

# Discord webhook URL
WEBHOOK_URL = "WEBHOOK"

# Base Camera URL
BASE_CAMERA_URL = "LINK_HERE"

# Function to format the location from the file name
def extract_location(camera_url):
    # Extract the file name from the URL
    file_name = camera_url.split("/")[-1].split("?")[0]  
    location = file_name.replace(".jpg", "").replace("_", " ").replace("-", " ")
    return location

# Function to get the current timestamp
def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS

# Function to send the image to Discord
def post_to_discord():
    try:
        # Add a timestamp to the URL
        timestamp = int(time.time() * 1000)  # Current time in milliseconds
        camera_url = f"{BASE_CAMERA_URL}?date={timestamp}"
        
        # Extract the location and get the current timestamp
        location = extract_location(BASE_CAMERA_URL)
        current_time = get_current_time()
        
        # Fetch the image
        response = requests.get(camera_url, stream=True)
        response.raise_for_status()
        
        # Prepare the file payload and content
        file = {"file": ("camera_snapshot.jpg", response.content, "image/jpeg")}
        data = {
            "content": f"📍 Location: {location}\n🕒 Timestamp: {current_time}"
        }
        
        # Send the image to Discord
        discord_response = requests.post(WEBHOOK_URL, files=file, data=data)
        discord_response.raise_for_status()
        
        print(f"Image posted successfully: {location} at {current_time}")
    except Exception as e:
        print(f"Error posting image: {e}")

# Run the script every 10 seconds
if __name__ == "__main__":
    while True:
        post_to_discord()
        time.sleep(10)
