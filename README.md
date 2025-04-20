# ConciseAI
This project implements a text summerization app.

## Prerequisites
- Python 3.10
- Anaconda or Miniconda
- Git (optional, if you plan to clone via Git)

## Setup Instructions

Follow these steps to set up the project locally on your machine.

### Step 1: Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/aviralsoni22/ConciseAI.git
cd ConciseAI
```

### Step 2: Create a Virtual Environment
For Windows PowerShell, use the following command to create a virtual environment
```bash
conda create -p venv python==3.10 -y
```

### Step 3: Activate the virtual environment
```bash
conda activate <Path of venv>
```

### Step 4: Install the required dependencies
```bash
pip install -r requirements.txt
```
### Step 5: Run the application
Navigate to the directory where app.py is located and run the application:

```bash
python app.py
```
### Step 6: Train the model
Go to a web browser and paste: http://localhost:8080/train
Training will take 20-30 minutes.

### Step 6: Predict
Go to: http://localhost:8080/predict
Click on "Try it out" under Predict option.
Paste the text and click on "execute" button.

Suggestion: Take a story of 50-60 words and paste it in the prediction box. 




