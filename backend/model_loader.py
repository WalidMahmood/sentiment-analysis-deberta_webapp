import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

def load_model(model_path=None):
    """Load model and tokenizer from path"""
    if model_path is None:
        # Check environment variable first
        model_path = os.environ.get("MODEL_PATH")
        if model_path is None:
            # Fallback to relative path assuming script is in backend/ and models is in ../models
            current_dir = os.path.dirname(os.path.abspath(__file__))
            model_path = os.path.join(current_dir, "..", "models", "deberta_base_config3")
    
    print(f"Loading from: {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    device = "cpu"
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.to(device)
    model.eval()
    print(f"Model loaded on {device}")
    return model, tokenizer, device

def predict(text, model, tokenizer, device):
    """Predict sentiment for text"""
    inputs = tokenizer(
    text, 
    return_tensors="pt", 
    padding=True, 
    truncation=True,
    max_length=128
).to(device)

    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=-1)
        predicted_class = torch.argmax(probs, dim=-1).item()
    
    return predicted_class, probs[0].cpu().numpy().tolist()

if __name__ == "__main__":
    # Load model once
    model, tokenizer, device = load_model()

    # Test
    test_text = "This product is amazing!"
    predicted_class, probs = predict(test_text, model, tokenizer, device)

    print(f"Text: {test_text}")
    print(f"Predicted class: {predicted_class}")
    print(f"Probabilities: {probs}")
