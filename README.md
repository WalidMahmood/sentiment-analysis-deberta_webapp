---
title: Sentiment Analysis DeBerTa Webapp
emoji: 🎭
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

<div align="center">

# 🎭 Sentiment Analysis Web App

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![DeBERTa](https://img.shields.io/badge/Model-DeBERTa-yellow?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/docs/transformers/model_doc/deberta)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue?style=for-the-badge)](https://huggingface.co/spaces/WalidMahmood/sentiment-analysis-deberta_webapp)

**A high-performance, containerized web application for real-time sentiment analysis using state-of-the-art implementation of DeBERTa.**

[Features](#-key-features) • [Model & Training](#-model--training) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-documentation)

</div>

---

## 📖 Overview

This project is a sophisticated AI-powered web application that analyzes the sentiment of text inputs in real-time. Built with a **FastAPI** backend and a polished **frontend**, it leverages the **DeBERTa (Decoding-enhanced BERT with disentangled attention)** model to deliver highly accurate classifications (Negative, Neutral, Positive).

Whether you're analyzing customer feedback, social media posts, or product reviews, this tool provides instant insights with visual confidence metrics efficiently packaged in **Docker** for easy deployment.

## ✨ Key Features

- **🚀 State-of-the-Art NLP**: Powered by the custom-tuned `DeBERTa` architecture for superior accuracy.
- **⚡ Real-time Analysis**: Instant inference using an optimized backend pipeline.
- **📊 Visual Analytics**: Dynamic bar charts generated server-side with Matplotlib to visualize confidence scores for each class.
- **🐳 Dockerized**: Fully containerized environment ensuring consistency across development and production.
- **🎨 Modern UI**: Clean and responsive web interface for seamless user interaction.

## 🧠 Model & Training

The core of this application is a fine-tuned **DeBERTa** model, chosen for its superior performance on natural language understanding tasks.

### Dataset & Preprocessing
- **Source**: Trained on a large dataset of tweets (approx. 31k training samples) sourced from Hugging Face / Kaggle.
- **Class Distribution**: Balanced dataset with 3 classes:
  - Negative: ~9,100 samples
  - Neutral: ~11,600 samples
  - Positive: ~10,400 samples
- **Preprocessing Pipeline**: 
  - Custom text cleaning to handle social media noise (hashtags, mentions).
  - Emoji preservation/translation to capture emotional context.
  - Light text normalization for Transformer capability.

### Architecture
- **Base Model**: `DeBERTa` (Decoding-enhanced BERT with disentangled attention). 
  - This architecture improves on BERT by disentangling potential content and position, using a disentangled attention mechanism.
- **Fine-tuning**: The model was fine-tuned specifically for 3-way sentiment classification, optimizing for robust handling of informal text and slang.

## 🛠 Tech Stack

- **Backend**: Python, FastAPI, Uvicorn, PyTorch, Transformers
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data Visualization**: Matplotlib
- **DevOps**: Docker, Docker Compose

## 🚀 Installation

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.

### Quick Start with Docker (Recommended)

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Launch the application**:
    ```bash
    docker-compose up --build
    ```
    *Note: The first build may take a few minutes as it packages the model files.*

3.  **Access the App**:
    Open your browser and verify the status:
    - **Web Interface**: [http://localhost:8000](http://localhost:8000)
    - **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

### Local Development (Manual)

If you prefer running without Docker:

1.  Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

2.  Install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  Run the server:
    ```bash
    cd backend
    uvicorn main:app --reload
    ```

## 🔌 API Documentation

The API follows RESTful principles. Interactive documentation is available at `/docs`.

### Endpoints

#### `POST /analyze`
Analyzes the sentiment of the provided text.

- **Request Body**:
  ```json
  {
    "text": "This product exceeded my expectations!"
  }
  ```

- **Response**:
  ```json
  {
    "text": "...",
    "predicted_class": 2,
    "class_label": "Positive",
    "probabilities": [0.01, 0.04, 0.95],
    "chart": "base64_encoded_image_string..."
  }
  ```

#### `GET /status`
Health check endpoint.

## 📂 Project Structure

```bash
├── backend/
│   ├── main.py              # Application entry point & API routes
│   ├── model_loader.py      # Model inference logic
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── index.html           # User interface
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── models/
│   └── deberta_base_config3 # DeBERTa model artifacts
├── notebooks/               # Research & training notebooks
├── Dockerfile               # Container definition
└── docker-compose.yml       # Production service orchestration
```

---

<div align="center">

Made with ❤️ by [Walid Mahmood](https://github.com/WalidMahmood)    

</div>
