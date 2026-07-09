# SmartHire: Resume-to-Job Matching & Career Guidance Engine

SmartHire is an end-to-end Machine Learning recruitment pipeline that uses Natural Language Processing (NLP) to match candidates with their ideal job roles. 

It predicts a candidate's job category (Supervised Learning), recommends top job matches using Cosine Similarity (Unsupervised Learning), and extracts dynamic skill gaps using K-Means clustering and target role feature engineering.

##  Setup & Installation

1. **Clone the repository:**
   ```
   git clone [https://github.com/YourUsername/SmartHire.git](https://github.com/YourUsername/SmartHire.git)
   cd SmartHire
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Add the Datasets:**
   Ensure your cleaned datasets are placed in the correct directories:
   * Place `resumes_clean.csv` in `data/raw/`
   * Place `jobs_reduced.csv` in `data/interim/`

##  Training the Models

Before launching the app, you must train the machine learning models and generate the required `.pkl` files. Run these commands from the root directory:

1. **Train the Classifier (Supervised):**
   ```
   python -m src.models.classifier
   ```
2. **Train the Recommender & Clustering Models (Unsupervised):**
   ```
   python -m src.models.recommender
   ```

## Running the Web App

Once the models are trained, launch the Streamlit portal:
```
streamlit run app/streamlit_app.py
```

## Generating Evaluation Metrics & Visualizations

To view model performance (Accuracy, F1-Score, Silhouette Score) and generate PCA/t-SNE plots for your report:
1. Run the evaluation script for terminal metrics:
   ```
   python -m src.evaluate
   ```
2. Run the Jupyter Notebooks inside the `notebooks/` folder to save visual figures directly to the `reports/figures/` directory.

## Project Architecture
```text
smarthire/
├── data/               # Raw and interim datasets
├── notebooks/          # EDA, evaluation, and visualizations
├── src/                # Reusable Python modules (models, features, parsing)
├── models/             # Serialized .pkl model files
├── app/                # Streamlit web interface
├── reports/            # Generated figures and final written report
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```