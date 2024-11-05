# Phishing Website Detection System - End-to-End Machine Learning Solution

## Overview

The **Phishing Website Detection System** is a comprehensive end-to-end machine learning solution designed to identify and mitigate phishing attacks by detecting malicious websites. Phishing attacks remain one of the most prevalent threats on the internet, posing significant risks to individuals and organizations alike. This project aims to provide a robust mechanism for real-time detection of phishing websites, utilizing advanced machine learning techniques within a scalable infrastructure.

## Table of Contents

1. [Project Goals](#project-goals)
2. [Architecture](#architecture)
3. [Key Features](#key-features)
4. [Technologies Used](#technologies-used)
5. [Data Ingestion](#data-ingestion)
6. [Data Validation](#data-validation)
7. [Model Training](#model-training)
8. [Model Deployment](#model-deployment)
9. [Usage](#usage)
10. [Contributing](#contributing)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)

## Project Goals

The primary objectives of this project include:

- **Automated Phishing Detection**: Develop a reliable system to automatically detect phishing websites using machine learning algorithms.
- **Scalability**: Ensure the solution is scalable, allowing for the handling of large datasets effectively.
- **Real-time Deployment**: Implement a robust deployment strategy to facilitate real-time phishing detection.
- **Maintain Data Quality**: Incorporate data validation checks to ensure high-quality data input into the machine learning models.

## Architecture

The architecture of the Phishing Website Detection System consists of several components, which work together to provide a seamless machine learning pipeline. The main components include:

- **Data Ingestion**: Ingesting data from various sources into a MongoDB Atlas database.
- **Data Validation**: Performing checks to ensure data quality and consistency.
- **Data Transformation**: Preparing data for model training through feature engineering and data preprocessing.
- **Model Training**: Training multiple machine learning models to identify the most effective approach.
- **Model Deployment**: Deploying the final model to an AWS EC2 instance for real-time predictions.

![Architecture Diagram](./images/architecture_diagram.png)

## Key Features

- **ETL Pipeline**: The project includes an ETL (Extract, Transform, Load) pipeline that ingests phishing data into MongoDB Atlas, facilitating efficient data processing.
- **Data Validation**: Implemented checks for schema consistency, datatype verification, and data drift detection, ensuring data integrity.
- **Multiple Model Training**: Trained various machine learning models, including Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, and AdaBoost Classifier, with hyperparameter tuning to optimize performance.
- **Experiment Tracking**: Used MLflow for tracking classification metrics and performance, enabling a structured approach to model evaluation.
- **Real-time Deployment**: Deployed the optimized model on AWS EC2, enabling real-time detection of phishing websites.

## Technologies Used

The following technologies and tools were utilized in the development of this project:

- **Programming Languages**: Python
- **Data Management**: MongoDB Atlas Cloud
- **Cloud Services**: AWS EC2, AWS S3, AWS ECR
- **Machine Learning Libraries**: Scikit-learn, MLflow
- **Containerization**: Docker
- **CI/CD Tools**: GitHub Actions
- **Version Control**: Git, DagsHub

## Data Ingestion

The ingestion process is handled by a well-structured ETL pipeline that extracts phishing data from various sources and loads it into MongoDB Atlas. This modular coding approach ensures:

- **Seamless Data Processing**: The code is modular, allowing for easy maintenance and scalability.
- **Flexible Data Retrieval**: Data can be accessed and manipulated as needed for analysis and training.

### Sample Code Snippet for ETL Pipeline

```python
import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/phishing_db")
db = client.phishing_db
collection = db.phishing_data

# Ingest data function
def ingest_data(data):
    collection.insert_many(data)
