from tensorflow.keras.preprocessing.image import img_to_array

class ToArray:

    def __init__(self, data_format=None):
        self.data_format = data_format

    def preprocess(self, image):
        return img_to_array(image, data_format=self.data_format)
