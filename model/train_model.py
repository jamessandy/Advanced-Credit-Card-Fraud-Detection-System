import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import numpy as np

# Load data
data = pd.read_csv("fraud_data.csv")
X = data.drop(columns=["is_fraud"])
y = data["is_fraud"]

# Define model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=10, batch_size=32)

# Save model
model.save("model/model.h5")
