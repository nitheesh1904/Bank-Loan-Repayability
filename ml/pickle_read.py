import pickle
import keras
import json
import tensorflow as tf
from keras.models import model_from_json   
json_file = open('ml\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
