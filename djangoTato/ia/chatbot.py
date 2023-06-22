from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
from sklearn.preprocessing import LabelEncoder
import pickle

import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

import pickle

class tatoBot:
    def __init__(self, model_path, tokenizer_path, label_encoder_path, max_length):
        
        self.model = load_model(model_path)
        self.tokenizer = self.load_tokenizer(tokenizer_path)
        self.max_length = max_length
        self.label_encoder = self.load_label_encoder(label_encoder_path)
    
    def load_tokenizer(self, tokenizer_path):
        with open(tokenizer_path, 'r') as file:
            tokenizer_json = file.read()
        tokenizer = tokenizer_from_json(tokenizer_json)
        return tokenizer
    
    def load_label_encoder(self, label_encoder_path):
        with open(label_encoder_path, 'rb') as file:
            label_encoder = pickle.load(file)
        return label_encoder
    
    def preprocess_text(self, text):
        text = text.lower()
        text = self.tokenizer.texts_to_sequences([text])
        text = pad_sequences(text, maxlen=self.max_length)
        return text
    
    def responder_oracion(self, text):
        preprocessed_text = self.preprocess_text(text)
        prediction = self.model.predict(preprocessed_text)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        predicted_class_label = self.label_encoder.inverse_transform([predicted_class_index])[0]
        return predicted_class_label
