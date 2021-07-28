from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    dataset = Dataset()

    def new_model(self, payload: str) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)




def create_train(this):
    return this

def create_label(this):
    return this

def drop_feature(this, *feature):
    return this

def embarked_nominal(this):
    return this

def fare_oridnal(this):
    return this

def title_nominal(this):
    return this

def gender_norminal(this):
    return this

def age_ordinal(this):
    return this

def create_k_fold():
    return None

def accuracy_by_classfier(this):
    return ""



