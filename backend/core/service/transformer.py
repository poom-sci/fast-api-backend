# Use a pipeline as a high-level helper
from transformers import pipeline


model = 'ProsusAI/finbert'
pipe = pipeline("text-classification", model=model)

def predicts(text : [str]):
    result = pipe(text)
    return result

def predict(text : str):
    result = pipe(text)
    return result

