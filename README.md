# Mashroom DataAnalysis With Streamlit
This project focuses on building interactive web applications for machine learning classification using **Streamlit** and **Python**. The app provides an intuitive interface that allows users to select a classification algorithm, adjust hyperparameters, and visualize evaluation metrics through a web-based interface.

## Project Overview

This project provides an easy-to-use platform for users to:
1. **Train Machine Learning Models**: Implement Logistic Regression, Random Forest, and Support Vector Classifiers (SVC) using **scikit-learn**.
2. **Evaluate Model Performance**: Visualize evaluation metrics for binary classification problems.
3. **Interactive Web Interface**: Build a web application with **Streamlit** that allows users to:
   - Select a classification algorithm.
   - Adjust hyperparameters interactively.
   - View performance metrics and visualizations dynamically.

## Objectives

- **Data Manipulation and Visualization**:
  - Load datasets dynamically using **Pandas**.
  - Explore and visualize data with insightful charts and graphs.

- **Machine Learning Models**:
  - Train and evaluate Logistic Regression, Support Vector Machines (SVM), and Random Forest Classifiers.
  - Use hyperparameter tuning to improve model performance.

- **Web Application with Streamlit**:
  - An intuitive and interactive interface for non-coders to experiment with machine learning models.
  - Real-time updates of metrics and visualizations based on user input.

## Project Structure

| File/Directory              | Description                                         |
|-----------------------------|-----------------------------------------------------|
| `app.py`                    | Main Streamlit application script.                  |
| `mushrooms.csv`             | Dataset containing the mushrooms information.       |
| `requirements.txt`          | Python dependencies for the project.                |

## Prerequisites

- **Python** 3.8 or higher
- **Libraries**: Streamlit, scikit-learn, pandas, matplotlib, numpy

## Features
1. **Dataset Loading and Exploration**:
    - Load `mushrooms.csv` datasets.
    - Display data summary statistics and visualizations.
2. **Model Selection and Training**:
    - Choose between Logistic Regression, Random Forest, or Support Vector Machines.
    - Adjust hyperparameters interactively, such as:
        - Support Vector Machine (SVM): Regularization strength (C), Kernal and Gamma.
        - Logistic Regression: Regularization strength (C) and Maximum iteration (max_iter).
        - Random Forest: Number of estimators (n_estimators), maximum depth (max_depth), bootstrap, n_jobs.
3. **Model Evaluation**:
    - Visualize evaluation metrics for trained models:
        - Confusion matrix
        - ROC curve
        - Precision-recall curve
- Compare the performance of different models interactively.

## Future Enhancements
- Add support for additional classification algorithms like K-Nearest Neighbors and Gradient Boosting.
- Include more advanced evaluation metrics, such as ROC curves and AUC scores.
- Allow users to upload custom datasets for experimentation.

## Acknowledgements

- This project was inspired and developed based on the concepts learned in the [Build a Machine Learning Web App with Streamlit and Python](https://www.coursera.org/projects/machine-learning-streamlit-python) on Coursera. Special thanks to the course creators for their comprehensive content.
- Resources and references for this project include:
    - **Streamlit** for building interactive web applications.
    - **scikit-learn** for machine learning model implementation.
    - **pandas** for data manipulation.
    - **matplotlib** for data visualization.
