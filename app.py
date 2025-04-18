from flask import Flask, render_template, request, redirect, url_for, jsonify
import librosa
import os
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import joblib

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load model
try:
    model = load_model('Model.h5')
    print(" Model loaded successfully!")
except Exception as e:
    print(f" Error loading model: {e}")
    model = None

# Load LabelEncoder
try:
    le = joblib.load('label_encoder.pkl')
    print(" LabelEncoder loaded successfully!")
except Exception as e:
    print(f" Error loading LabelEncoder: {e}")
    le = None

# ✅ Feature extraction
def extract_features(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None, duration=2.5, offset=0.6)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfcc_scaled = np.mean(mfcc.T, axis=0)
        return mfcc_scaled
    except Exception as e:
        print(f" Error extracting features: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/live_detect', methods=['POST'])
def live_detect():
    print(" Received request at /live_detect")
    audio_file = request.files.get('audio_data')
    if not audio_file:
        return jsonify({'detected': False, 'error': 'No audio received'})

    save_path = os.path.join(app.config['UPLOAD_FOLDER'], 'live_audio.wav')
    audio_file.save(save_path)

    try:
        features = extract_features(save_path)
        if features is None:
            raise ValueError("Feature extraction failed")

        features = np.expand_dims(features, axis=0)
        prediction = model.predict(features)
        predicted_class = int(np.argmax(prediction) ) # Get the predicted class (0-9)
        print("hey tej:---->",predicted_class)

        # Check if the model returns any prediction between 0-9
        if (predicted_class ==2):
            # Alarm triggered
            return jsonify({'detected': True, 'predicted_class': predicted_class, 'message': "Alarm triggered!"})
        else:
            return jsonify({'detected': False, 'message': "No valid prediction detected"})

    except Exception as e:
        return jsonify({'detected': False, 'error': str(e)})

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        result = "Prediction result here"
        return render_template('prediction.html', result=result)
    return render_template('prediction.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            return render_template('result.html', prediction="No file selected.")

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename.replace("\\", "/"))
        try:
            file.save(file_path)
            print(f" Saved audio file at {file_path}")

            if model is None or le is None:
                raise ValueError("Model or LabelEncoder not loaded properly.")

            features = extract_features(file_path)
            if features is None:
                raise ValueError("Feature extraction failed.")
            features = np.expand_dims(features, axis=0)
            pred = model.predict(features)
            pred_label = le.inverse_transform([np.argmax(pred)])[0]

            os.remove(file_path)
            return render_template('result.html', prediction=pred_label)

        except Exception as e:
            print(f" Prediction error: {e}")
            if os.path.exists(file_path):
                os.remove(file_path)
            return render_template('result.html', prediction="Error during prediction.")
    return render_template('result.html', prediction="No file uploaded.")

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
