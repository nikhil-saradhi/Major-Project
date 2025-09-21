# Real-Time Audio Event Detection for Threat Identification using 1D-CNN

This repository contains the implementation of our **Major Project Report** submitted to **Jawaharlal Nehru Technological University, Hyderabad** in partial fulfillment of the requirements for the award of the **Bachelor of Technology in Computer Science and Engineering (2024-2025)**.  

---

## 📖 Abstract
Ensuring personal safety in remote or isolated areas is becoming increasingly important. Threats such as robbery or assault are often preceded by audio cues (e.g., footsteps, shouting, breaking glass) that are overlooked by traditional security systems.  

This project proposes a **Real-Time Audio Event Detection System** using a **1D Convolutional Neural Network (1D-CNN)** to classify environmental sounds with high accuracy. By training on labeled datasets of real-world audio, the model learns to recognize patterns and detect potential threats in real-time, thereby enhancing situational awareness and safety.

---

## 🎯 Objectives
- Detect and classify **environmental and threat-related sounds** in real time.  
- Differentiate between **normal background noises** and **critical audio events**.  
- Provide a **scalable and adaptable system** for diverse environments (urban, workplace, healthcare, remote areas).  
- Improve **situational awareness** for timely responses in critical situations.  

---

## 🏗️ Methodology
The system is designed and developed in the following phases:
1. **Data Collection** – Datasets from Kaggle and UrbanSound.  
2. **Preprocessing** – Feature extraction using **MFCCs (Mel-Frequency Cepstral Coefficients)**.  
3. **Model Design** – A 1D CNN architecture for sequential audio data.  
4. **Model Training & Evaluation** – Accuracy achieved: **Training 99.87%, Testing 91%**.  
5. **Deployment** – Web-based user interface to upload or capture live audio for classification.  

---

## ⚙️ System Requirements

### Hardware
- Intel Core i5 Processor  
- 16 GB RAM  
- 512 GB Hard Disk  

### Software
- **Operating System**: Windows 10/11  
- **Programming Language**: Python  
- **Platform**: Spyder3 / Jupyter Notebook  
- **Libraries**: TensorFlow, Keras, librosa, numpy, pandas, matplotlib  
- **Frontend**: Flask/Django (Web UI)  

---

## 🚀 Features
- Real-time **audio classification** using 1D-CNN.  
- Detection of threat-related sounds like **screams, gunshots, footsteps**.  
- **Live audio input** support using microphone.  
- User-friendly **web interface** for uploading and analyzing audio.  
- Performance analysis with accuracy/loss charts.  

---

## 📊 Results
- Achieved high accuracy on test datasets with robust classification.  
- Successfully distinguished between normal and threat-related sounds.  
- Real-time implementation validated with live microphone input.  

---

## 🔮 Future Enhancements
- **Data augmentation** (noise addition, pitch shift, time-stretching).  
- **Transfer learning** with pre-trained audio models.  
- **Multimodal inputs** (audio + video for better context).  
- **Edge deployment** (Raspberry Pi, microcontrollers for IoT applications).  

---

## 👨‍💻 Project Team
- **Kandula Nikhil Saradhi** (21831A0587)  
- **Kokkirala Sravan Kumar** (21831A0590)  
- **Marisetty Tejesh** (21831A05B0)  

Under the guidance of:  
**Mrs. P. Anusha**  
Assistant Professor, Department of CSE  
Guru Nanak Institute of Technology, Hyderabad  

---

## 📜 Acknowledgement
We express our gratitude to our guide **Mrs. P. Anusha**, our HOD **Dr. B. Santhosh Kumar**, and all faculty members of the **Department of CSE, GNIT** for their constant support and encouragement.  

---

## 📚 References
The project is based on research and datasets referenced in our official report. Key datasets:  
- [UrbanSound8K Dataset](https://urbansounddataset.weebly.com/download-urbansound8k.html)  
- [Environmental Sound Classification 50 – Kaggle](https://www.kaggle.com/datasets/mmoreaux/environmental-sound-classification-50)  
- [Audio Dataset of Scream and Non-Scream – Kaggle](https://www.kaggle.com/datasets/aananehsansiam/audio-dataset-of-scream-and-non-scream)  

---

## 🏫 Institution
**Department of Computer Science & Engineering**  
Guru Nanak Institute of Technology (Affiliated to JNTUH, Hyderabad)  
Ranga Reddy District – 501506  
