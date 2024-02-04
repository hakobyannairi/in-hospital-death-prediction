from model import Model
from preprocessor import Preprocessor

class Pipeline:
    def __init__(self,):
        self.model = Model()
        self.preprocessor = Preprocessor()
        print('change from local')

    def run(self, X, test=False):
        if test:
            print('testing')
        # load preprocessor and model for testing
        # save results to predictions.json file
        else:
            print('training')
        # call preprocessor and model for training
        # save preprocessor and model for future testing
