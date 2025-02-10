# ExamScore Predictor

This project predicts an exam score based on user input. It uses a trained machine learning model served via Flask and a responsive front-end for data collection and results display.

## Structure

project/
├── index.html          # Main HTML file for the frontend
├── styles.css          # CSS for styling the frontend
├── script.js           # JavaScript for frontend logic and API communication
├── api/                # Backend API directory
│   ├── app.py          # Flask application (backend server)
│   ├── requirements.txt # List of Python dependencies
├── model/              # Directory for the trained model
│   └── trained_model.pkl # Saved machine learning model
├── static/             # Static assets (e.g., fonts, images)
│   └── fonts/          # Fonts used in the project
├── README.md           # Documentation for the project
└── .gitignore          # File to specify untracked files to ignore

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

