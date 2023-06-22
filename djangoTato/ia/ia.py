
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.utils import shuffle
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import tensorflow as tf
import pickle

data = pd.read_csv('dataset.csv')
oraciones = data['oracion'].values
respuestas = data['respuesta'].values

label_encoder = LabelEncoder()
respuestas_codificadas = label_encoder.fit_transform(respuestas)

# Guardar el LabelEncoder en un archivo
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(oraciones)
tokenizer_json = tokenizer.to_json()
with open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(tokenizer_json)
oraciones_secuencia = tokenizer.texts_to_sequences(oraciones)

max_length = max([len(seq) for seq in oraciones_secuencia])

oraciones_secuencia = pad_sequences(oraciones_secuencia, maxlen=max_length)

model = Sequential()
model.add(Dense(128, input_shape=(max_length,), activation='relu'))
model.add(Dense(len(label_encoder.classes_), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(oraciones_secuencia, tf.keras.utils.to_categorical(respuestas_codificadas), epochs=200)

bert_model = SentenceTransformer('bert-base-nli-mean-tokens')

def similar(a, b):
    embeddings = bert_model.encode([a, b])
    similarity = 1 - cosine(embeddings[0], embeddings[1])
    return similarity

def responder_oracion(oracion):
    oracion_codificada = tokenizer.texts_to_sequences([oracion])
    oracion_codificada = pad_sequences(oracion_codificada, maxlen=max_length)
    prediccion = model.predict(oracion_codificada)
    prediccion_clase = np.argmax(prediccion, axis=1)
    respuesta_codificada = label_encoder.inverse_transform(prediccion_clase)
    respuesta = respuesta_codificada[0]
    if similar(oracion, respuesta) < 0.7:
        respuesta = "No entiendo tu pregunta"
    return respuesta

model.save('model.h5')

while True:
    oracion = input("Escribi: ")
    if oracion.lower() == 'salir':
        break
    respuesta = responder_oracion(oracion)
    print(respuesta)
