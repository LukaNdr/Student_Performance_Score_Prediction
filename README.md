# ExamScore Predictor

This project predicts an exam score based on user input. It uses a trained machine learning model served via Flask and a responsive front-end for data collection and results display.

## Structure

project/ ├── index.html # Main HTML file ├── styles.css # Styling file ├── script.js # Frontend script ├── api/ # Backend API │ ├── app.py # Flask server │ ├── requirements.txt # Python dependencies ├── model/ # Trained model directory │ └── trained_model.pkl ├── static/ # Static assets │ └── fonts/ ├── README.md # Project documentation └── .gitignore # Ignore unnecessary files


## Setup and Run

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project

2. Set Up a Virtual Environment (Recommended)
    python -m venv venv
Activate the virtual environment:

Windows:
    .\\venv\\Scripts\\activate

Mac/Linux:
    source venv/bin/activate

3. Install Python dependencies:

    cd api
    pip install -r requirements.txt

4. Run the backend:

    python app.py

5. Open index.html in your browser to access the UI.

6. Enter the data and get your prediction!

