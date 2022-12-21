import pytest 
import pandas as pd
import pickle

df = pd.read_csv("C:/Users/edenl/Desktop/file_rouge/notebook/original_data/clean_heart_failure_data.csv")
df

def test_data():

    if len(df.columns)==12:

        assert True
    else : 
        assert False

def test_prediction_range():
    
    model = pickle.load(open('C:/Users/edenl/Desktop/file_rouge/pickle_model/heart.pickle', 'rb'))
    predictions = model.predict(df.drop('HeartDisease', axis=1))
    range_values_checked = ((predictions >= 0) & (predictions <= 1)).all()
    assert range_values_checked == True

    
def test_number_of_prediction():
    model = pickle.load(open('C:/Users/edenl/Desktop/file_rouge/pickle_model/heart.pickle', 'rb'))
    predictions = model.predict(df.drop('HeartDisease', axis=1))
    assert len(predictions) == len(df)





if __name__ == "__main__":
    test_data()
    test_prediction_range()
    test_number_of_prediction()

