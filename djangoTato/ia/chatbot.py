from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
from sklearn.preprocessing import LabelEncoder

import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

class tatoBot:
    def __init__(self, model_path, tokenizer_path, max_length):
        # Carga el modelo y el tokenizer
        self.model = load_model(model_path)
        self.tokenizer = self.load_tokenizer(tokenizer_path)
        self.max_length = max_length
        # Inicializa el LabelEncoder
        self.label_encoder = LabelEncoder()
        # Ajusta el LabelEncoder con las etiquetas conocidas
        etiquetas = ['¡Hola! me llamo Tatobot', '¡Hola! Estoy muy bien ¿y tu?', 'La escuela se llama Almirante Guillermo Brown mejor conocida como ET36', 'El colegio queda en el Polo educativo Saavedra en la calle Galvan 3700', 'El colegio se llama Almirante Guillermo Brown', 'El nombre abreviado del colegio es ET36', 'El colegio se encuentra en el barrio de Saavedra']
        self.label_encoder.fit(etiquetas)  # Reemplaza con las etiquetas adecuadas
    
    def load_tokenizer(self, tokenizer_path):
        # Carga el tokenizer desde el archivo JSON
        with open(tokenizer_path, 'r') as file:
            tokenizer_json = file.read()
        tokenizer = tokenizer_from_json(tokenizer_json)
        return tokenizer
    
    def preprocess_text(self, text):
        # Preprocesa el texto utilizando el tokenizer
        text = text.lower()
        text = self.tokenizer.texts_to_sequences([text])
        text = pad_sequences(text, maxlen=self.max_length)
        return text
    
    def responder_oracion(self, text):
        preprocessed_text = self.preprocess_text(text)
        prediction = self.model.predict(preprocessed_text)
        predicted_class_index = tf.argmax(prediction, axis=1).numpy()[0]
        response = self.tokenizer.index_word[predicted_class_index+1]
        return response

