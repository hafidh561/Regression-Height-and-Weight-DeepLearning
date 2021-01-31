import tensorflow as tf
import pandas as pd
import pickle


def predict_weight(height):
    # Load Model
    scaler_height = pickle.load(
        open('./saved_model/scaler_height.pickle', 'rb'))
    scaler_weight = pickle.load(
        open('./saved_model/scaler_weight.pickle', 'rb'))
    model = tf.keras.models.load_model('./saved_model/model_predict_weight.h5')
    data_height = {
        'height': [height]
    }
    df_predict = pd.DataFrame(data_height)
    scaler_predict_weight = scaler_height.transform(df_predict)
    data_predict_weight = model.predict(scaler_predict_weight)
    data_predict_weight = round(
        scaler_weight.inverse_transform(data_predict_weight)[0][0], 1)

    return abs(data_predict_weight)


def predict_height(weight):
    # Load Model
    scaler_height = pickle.load(
        open('./saved_model/scaler_height.pickle', 'rb'))
    scaler_weight = pickle.load(
        open('./saved_model/scaler_weight.pickle', 'rb'))
    model = tf.keras.models.load_model('./saved_model/model_predict_height.h5')

    data_weight = {
        'weight': [weight]
    }
    df_predict = pd.DataFrame(data_weight)
    scaler_predict_height = scaler_weight.transform(df_predict)
    predict_height = model.predict(scaler_predict_height)
    predict_height = round(
        scaler_height.inverse_transform(predict_height)[0][0], 1)

    return abs(predict_height)
