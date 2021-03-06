import tensorflow as tf
from tensorflow import keras

def init():
    reconstructed_model = keras.models.load_model("C:/Users/alvia/My_Projects/uyoga-git/UYOGA_MODEL")

    test_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale= 1/255.)
    test_data = test_gen.flow_from_directory("C:/Users/alvia/Downloads/archive (10)/DATASET/TEST",
                                            target_size = (224,224),
                                            color_mode = "rgb",
                                            class_mode = "categorical",
                                            batch_size = 32
                                            )

    labels = list(test_data.class_indices.keys())

    return reconstructed_model, labels