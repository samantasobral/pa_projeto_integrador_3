import pickle
import json

class CustomerClusteringModel:
    def __init__(self):
        with open('model/gmm_model.pkl', 'rb') as file:
            self.gmm = pickle.load(file)
    
    def predict_cluster(self, data):
        clusters = self.gmm.predict(data)
        return json.dumps(clusters.tolist())