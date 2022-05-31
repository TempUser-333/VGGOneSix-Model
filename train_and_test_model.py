from pytesseract import pytesseract
from tensorflow.keras.applications import vgg16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from glob import glob
import numpy as np
from logger_files.custom_logger import logger


pytesseract.pytesseract_cmd = glob('C:\\Pro**\\Tes**OCR\\te**t.exe')[0]

class TrainAndTestVGGOneSixModel(object):
    def train_model(self):
        model = vgg16.VGG16(include_top=True,
                            weights='imagenet')
        model.summary()
        logger.info('model got trained')
        
        return model
        
    def test_model(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_arr = image.img_to_array(img)
        logger.info('image loaded from the path and got converted into an array') 
        logger.debug(img_arr)
        
        expnd_arr = np.expand_dims(img_arr, 
                                   axis=0)
        logger.info('array got expanded with axis set to zero')
        logger.debug(expnd_arr)
        
        predictions = self.train_model().predict(expnd_arr)
        decoded_predictions = decode_predictions(predictions)
        
        logger.info('The predicted outputs are as follows')
        logger.debug(decoded_predictions)
        logger.info('The image might be %s which is of %.2f percent correct' % (decoded_predictions[0][0][1], decoded_predictions[0][0][2]*100))
        
        return 'The image might be %s which is of %.2f correct' % (decoded_predictions[0][0][1], decoded_predictions[0][0][2]*100)
            