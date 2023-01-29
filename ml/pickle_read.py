

# def predictor(input):
import pickle
import numpy as np
import keras
import json
import tensorflow as tf
import pandas as pd
from keras.models import model_from_json   
json_file = open('ml\model_final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
array=np.array([[1, 0.00044665645737621234, 1, 0.25333333333333335, 1, 0.05555555555555555, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0]])
check=pd.DataFrame(data=array)
answer=np.round(loaded_model.predict(check))
answer=answer.flatten()
print(int(answer))


