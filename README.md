# 🔒Phishing URL Detection

## Overview

This project demonstrates a phishing detection system using a trained machine learning model served via a Flask web application. Users can input a URL and get real-time predictions of whether it's legitimate or phishing, along with confidence percentages.

## Live Demo

Access the live app here:  
[Phishing URL Detector](https://phishing-url-detector-kn1b.onrender.com)  
( **Note**: It may take upto a minute to load for the first time)

## Key Features

- Trained scikit-learn pipeline with TF-IDF (word and character level) and LinearSVC
- Calibrated model outputs for accurate probability estimates
- Flask web app to interact with the model via a browser
- Dynamic visual feedback using progress bars for prediction confidence
- Render or GitHub-compatible for deployment

## Dataset and Model

- Based on the following dataset of URLs labeled as legitimate or phishing:
   - `https://huggingface.co/datasets/pirocheto/phishing-url`
- Pipeline includes:
  - TF-IDF feature extraction (word and character)
  - Linear Support Vector Machine with calibration for probabilities
- Model is saved as a pickle file and loaded at runtime

## Project Structure
```
phishing-url-detector/
├── app.py             # Main Flask server
├── templates/
│ └── index.html       # Frontend HTML
├── model/
│ └── model.pkl        # Trained machine learning model
├── helpers.py         # Model training and utilities
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```
## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip for dependency installation

### Installation and Running

Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
pip install -r requirements.txt
```
Run the web app:
```bash
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.
## License

This project is licensed under the MIT License. 

## Contact

Contributions and feedback are welcome. Feel free to reach out or open an issue on GitHub.
