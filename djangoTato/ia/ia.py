import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import tensorflow as tf
# Cargar el dataset
data = pd.read_csv('dataset.csv')
oraciones = data['oracion'].values
respuestas = data['respuesta'].values

# Codificar las respuestas
label_encoder = LabelEncoder()
respuestas_codificadas = label_encoder.fit_transform(respuestas)

# Guardar el LabelEncoder en un archivo
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# Tokenizar las oraciones
tokenizer = Tokenizer()
tokenizer.fit_on_texts(oraciones)
tokenizer_json = tokenizer.to_json()
with open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(tokenizer_json)

# Convertir las oraciones a secuencias numéricas y hacer padding
oraciones_secuencia = tokenizer.texts_to_sequences(oraciones)
max_length = max([len(seq) for seq in oraciones_secuencia])
oraciones_secuencia = pad_sequences(oraciones_secuencia, maxlen=max_length)

# Crear el modelo
model = Sequential()
model.add(Dense(128, input_shape=(max_length,), activation='relu'))
model.add(Dense(len(label_encoder.classes_), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(oraciones_secuencia, tf.keras.utils.to_categorical(respuestas_codificadas), epochs=500)

# Cargar el modelo de embeddings BERT
bert_model = SentenceTransformer('bert-base-nli-mean-tokens')

# Función para calcular la similitud coseno entre dos oraciones
def similarity(a, b):
    embeddings = bert_model.encode([a, b])
    similarity = 1 - cosine(embeddings[0], embeddings[1])
    return similarity

# Función para responder a una oración
def responder_oracion(oracion):
    oracion_codificada = tokenizer.texts_to_sequences([oracion])
    oracion_codificada = pad_sequences(oracion_codificada, maxlen=max_length)
    prediccion = model.predict(oracion_codificada)
    prediccion_clase = np.argmax(prediccion, axis=1)
    respuesta_codificada = label_encoder.inverse_transform(prediccion_clase)
    respuesta = respuesta_codificada[0]
    if similarity(oracion, respuesta) < 0.7:
        respuesta = "No entiendo tu pregunta"
    return respuesta

# Guardar el modelo
model.save('model.h5')

# Loop principal para interactuar con la IA
while True:
    oracion = input("Escribe: ")
    if oracion.lower() == 'salir':
        break
    respuesta = responder_oracion(oracion)
    print(respuesta)
