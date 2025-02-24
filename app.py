from flask import Flask, render_template, request, send_file, url_for
import cv2 
import os
import time
from filters import apply_filter
from generate_qr import generate_qr
from ai_effects import apply_face_effects

app = Flask(__name__)
UPLOAD_FOLDER = "static/images/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
cam = cv2.VideoCapture(0)

def generate_frames(filter_type="none"):
    while True:
        success, frame = cam.read()
        if not success:
            break

        if filter_type != "none":
            frame = apply_filter(frame, filter_type)

        frame = apply_face_effects(frame)

        _, buffer = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=["POST"])
def capture():
    ret, frame = cam.read()
    if not ret:
        return "Failed to capture image", 500

    filename = f"{UPLOAD_FOLDER}captured_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)
    return filename

@app.route('/apply_filter', methods=["POST"])
def apply_filter_route():
    image_path = request.form["image_path"]
    filter_type = request.form["filter"]
    filtered_image = apply_filter(image_path, filter_type)
    
    return filtered_image

@app.route('/generate_qr', methods=["POST"])
def generate_qr_route():
    image_path = request.form["image_path"]
    image_url = url_for("static", filename=f"images/{os.path.basename(image_path)}", _external=True)
    qr_code_path = generate_qr(image_url)
    
    return qr_code_path

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)