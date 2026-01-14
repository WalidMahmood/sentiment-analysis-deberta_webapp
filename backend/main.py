from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import load_model, predict
import matplotlib.pyplot as plt
import io
import base64
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load model at startup
model, tokenizer, device = load_model()

class TextInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    predicted_class: int
    class_label: str
    probabilities: list
    chart: str  # base64 encoded image

@app.get("/status")
def read_root():
    return {"message": "Sentiment Analysis API is running"}

@app.post("/analyze")
def analyze_sentiment(input_data: TextInput):
    predicted_class, probs = predict(input_data.text, model, tokenizer, device)
    
    # Class labels
    class_labels = ['Negative', 'Neutral', 'Positive']
    class_label = class_labels[predicted_class]
    
    # Generate bar chart
    fig, ax = plt.subplots()
    ax.bar(class_labels, probs, color=['red', 'yellow', 'green'])
    ax.set_ylabel('Confidence Score')
    ax.set_title('Sentiment Analysis Confidence Scores')
    ax.set_ylim(0, 1)
    
    # Save to base64
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    chart_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close(fig)
    
    return SentimentResponse(
        text=input_data.text,
        predicted_class=predicted_class,
        class_label=class_label,
        probabilities=probs,
        chart=chart_base64
    )

# Mount static files for frontend
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
frontend_path = os.path.join(current_dir, "../frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
