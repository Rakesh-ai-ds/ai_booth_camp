# ai_booth_camp
# AI Photo Booth

## Overview
AI Photo Booth is a web-based application that captures a user's image via a webcam, transforms it into a cartoon or anime style using deep learning, and generates a QR code for downloading the processed image.

## Features
- **Webcam Capture**: Uses WebRTC to access the user's webcam and take a snapshot.
- **Image Processing**: Applies AI-based transformations to convert the image into a cartoon/anime style.
- **QR Code Generation**: Generates a QR code with a download link for the processed image.
- **Cloud Storage**: Stores processed images securely in the cloud.

## Tech Stack
### Frontend:
- **HTML/CSS/JavaScript**: User interface and interactions.
- **WebRTC**: Webcam access and image capture.
- **AJAX**: Communication with the backend.

### Backend:
- **Python (Flask)**: Handles image processing and API requests.
- **OpenCV & PIL**: Processes images.
- **Deep Learning (GANs or pre-trained models)**: Converts images to cartoon/anime style.
- **qrcode (Python Library)**: Generates QR codes.
- **Cloud Storage (AWS/GCP/Azure)**: Stores processed images.

## Installation & Setup
### Prerequisites:
- Python 3.x
- Node.js (Optional, if extending frontend with frameworks)
- Flask & required Python libraries

### Steps:
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/ai-photo-booth.git
   cd ai-photo-booth
   ```
2. **Install dependencies**
   ```bash
   pip install flask opencv-python pillow qrcode numpy
   ```
3. **Run the Flask server**
   ```bash
   python app.py
   ```
4. **Open the frontend**
   - Open `index.html` in a browser.
   - Ensure webcam permissions are granted.

## API Endpoints
### 1. **Process Image**
   - **Endpoint:** `/process`
   - **Method:** `POST`
   - **Payload:** Image file (base64 or multipart form-data)
   - **Response:** JSON with QR code URL

## Usage
1. Open the webpage and allow webcam access.
2. Capture an image using the provided button.
3. Wait for AI processing to convert it into a cartoon/anime style.
4. Scan the generated QR code to download the processed image.

## Potential Issues & Solutions
- **Webcam Not Working?** Ensure browser permissions are granted.
- **Image Processing Too Slow?** Optimize model or use GPU acceleration.
- **QR Code Not Displaying?** Check backend response and ensure image URL is correct.

## Future Enhancements
- Add multiple AI transformation styles.
- Improve processing speed with cloud-based inference.
- Implement user authentication for image history tracking.

## License
This project is licensed under the MIT License.

## Contributors
- Your Name (@yourusername)
- Additional Contributors

## Contact
For inquiries or collaborations, email: your-email@example.com

