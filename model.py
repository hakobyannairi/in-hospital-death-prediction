class Model:
    def __init__(self, new_param):
        self.my_param = new_param
        print('change from local')
        pass

    def fit(self, X, y):
        print('function for testing')
        pass

    def predict(self, X):
        print('change from local')
        print('remote changes refused')
        pass
