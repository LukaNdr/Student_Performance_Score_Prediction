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
    ```bash
    python -m venv venv
    
Activate the virtual environment:

Windows:

    .\\venv\\Scripts\\activate

Mac/Linux:

    source venv/bin/activate

3. Install Python dependencies:
   ```bash
    cd api
   
    pip install -r requirements.txt

5. Run the backend:
   ```bash
    python app.py

6. Open index.html in your browser to access the UI.

7. Enter the data and get your prediction!

