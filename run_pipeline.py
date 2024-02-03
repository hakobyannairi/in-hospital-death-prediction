from model import Model
from preprocessor import Preprocessor

class Pipeline:
    def __init__(self,):
        self.model = Model()
        self.preprocessor = Preprocessor()

    def run(self, X, test=False):
        if test:
            print('we are in the testing mode')
        # load preprocessor and model for testing
        # save results to predictions.json file
        else:
            print('training mode')
        # call preprocessor and model for training
        # save preprocessor and model for future testing