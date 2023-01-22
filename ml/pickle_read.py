import pickle
import keras
import json
import tensorflow as tf
from keras.models import model_from_json
with open("ml\model.json","r") as file:
    model_json=file.read()
loaded_model=model_from_json(model_json)
print(loaded_model.predict([1]*32)) 