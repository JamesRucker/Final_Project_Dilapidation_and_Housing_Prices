# Import Dependencies
import pandas as pd
import tensorflow as tf
from tensorflow import keras


def run_model(price, bath, bed, sqft, zip):
    
    # Import necessary files
    census_df = pd.read_csv("../Resources/acs5_2018.csv")
    model = tf.keras.models.load_model("housing_model.h5")

    input_df = pd.
