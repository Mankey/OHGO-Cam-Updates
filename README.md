# Webcam Snapshot Discord Bot

This project allows you to fetch webcam images from a specified camera and send them to a Discord channel using a webhook. It includes location and timestamp details for each image sent.

## Requirements

Before running the script, make sure you have the following installed:

- Python 3.x
- `requests` library (can be installed via `pip install requests`)

## How It Works

The bot fetches an image from a webcam URL at regular intervals (every 10 seconds by default), then sends the image to a specified Discord webhook. The bot also includes the webcam location and timestamp of the image in the message sent to Discord.

---

## How to Get Your Own Webcam Link

To use this script with your own webcam feed, follow these steps:

### 1. Find Your Webcam URL

You need the direct URL to the camera feed. For example, the camera feed URL from the OHGO website is:

`https://itscameras.dot.state.oh.us/images/CMH/CMH71-35.jpg?date=1736196824000`


In this example:
- `https://itscameras.dot.state.oh.us/images/CMH/CMH71-35.jpg` is the base URL.
- The `date` parameter (`?date=1736196824000`) is a dynamic value that you don’t need to worry about; the script will update it automatically.

### 2. Modify the Script with Your Webcam URL

Once you have the direct URL to the webcam feed, replace the `BASE_CAMERA_URL` in the script with your camera URL. For example:
wwwww
BASE_CAMERA_URL = "https://itscameras.dot.state.oh.us/images/CMH/CMH71-35.jpg"
Make sure the URL is a direct link to the image (ending in `.jpg`, `.png`, or another image format).
