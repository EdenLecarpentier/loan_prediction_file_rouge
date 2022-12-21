# %%
import pandas as pd
import pickle

import seaborn as sns

import matplotlib.pyplot as plt
from scikitplot.estimators import plot_learning_curve
import numpy as np

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as imbpipeline
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
import scikitplot as skplt
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate , learning_curve
from sklearn.metrics import confusion_matrix , roc_curve , recall_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
  
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline , make_pipeline
from sklearn.model_selection import GridSearchCV , cross_val_score
from sklearn.preprocessing import MinMaxScaler , StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn import linear_model
from sklearn.ensemble import BaggingClassifier , AdaBoostClassifier , StackingClassifier , GradientBoostingClassifier
from sklearn.dummy import DummyClassifier
from yellowbrick.classifier import ConfusionMatrix
from imblearn.over_sampling import SMOTE 
import mysql.connector
import pymysql
import sqlite3
from sqlalchemy import create_engine

import mlflow
import mlflow.sklearn 

# %%
if __name__ == "__main__":
    
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment(experiment_name='mlflow_loan_pred')
    with mlflow.start_run(run_name='mlflow_loan_prediction') as run : 
        
        data_base = mysql.connector.connect(host='localhost' , user='root' , password='Yugioh11.' , database='loan_prediction_file_rouge')
        cur = data_base.cursor(buffered=True)
        query = "select * from loan_prediction"
        cur.execute(query)
        tables = cur.fetchone()
        #connect sql database to be used has dataframe 



# %%    
        df = pd.read_sql(query , data_base)
        df
        #sql dataframe

        # %%

        df = df.drop('MyUnknownColumn' , axis=1)


        # %%
        df = df.drop('Id' , axis=1)

        # %%


        # %%
        categ = ["Gender" , "Dependents",  "Married" , "Education" , "Self_Employed" , "Property_Area" , "Loan_Status"]
        le = LabelEncoder()
        df[categ] = df[categ].apply(le.fit_transform)


        # %%

        X = df.drop(["Loan_Status" ], axis=1)
        # X is the dataframe without the target 

        y = df.Loan_Status
        #y is the target 

        # %%

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
        #we are splitting the dataset with train test split a test size of 20 percent of test and 80 percent of train 


        # %%

        from sklearn.decomposition import PCA
        preprocessing_ss = Pipeline(steps=[
            ('standard scaler', StandardScaler())])

        model = linear_model.LogisticRegression()
        #the dataset is really umbalanced so i ill need the smote to compare once i found a decent model 
        #standard scaler and min max scaler will be for the other models

        # %%


        # %%
        pipeline_log = Pipeline(steps = [['preprocessing_Standard_scaler'  , preprocessing_ss],
                                        ['LogisticRegression', model]
                                             ])

        # %%


        # %%


        # %%
        pipeline_log.fit(X_train , y_train.values)

        # %%
        pipeline_log.get_params().keys()

        # %%
        print("accuracy train : %.3f"%pipeline_log.score(X_train , y_train))
        print("accuracy test : %.3f"%pipeline_log.score(X_test , y_test))


        # %%
        



        # %%
        y_pred_log = pipeline_log.predict(X_test)
        y_pred_log
        
        recall = recall_score(y_test, y_pred_log)
         

        # %%
        print(classification_report(y_test, y_pred_log))
        #we are going to base or result on the recall we will need the 0 to be really low and the 1 to be really hight
        #this is because in a bank you don't wan't to predict people like that : they can get a loan but actually they shouldn't be able to get it
        #0 is the number of people that or not getting it but if the score is high this means a lot of people that shouldn't get the loan will get it 
        #1 needs to be high because they are the good prediction of people who can correctly get the loan

        # %%
        plot_learning_curve(pipeline_log, X , y)

        # %%
        pipeline_log.fit(X_train, y_train)
        y_probas = pipeline_log.predict_proba(X_test)
        skplt.metrics.plot_roc(y_test, y_probas)

        # %%
        cm = confusion_matrix(y_test, y_pred_log)
        sns.heatmap(cm, annot=True, fmt=".0f")
        plt.xlabel('y_pred')
        plt.ylabel('y_test') 
        plt.show()
        #what we need to reduce is the false positive on the top right overwhise it's decent but not great

        # %%
        pred = pipeline_log.predict(X_test)
        mlflow.log_metric("accuracy train" , pipeline_log.score(X_train , y_train))
        mlflow.log_metric("accuracy test" , pipeline_log.score(X_test , y_test))
        mlflow.log_metric("Recall" , recall)
        
        mlflow.sklearn.log_model(pipeline_log , "model")
        
        # %%
        pred

        # %%
        X_test['proba_ml'] =pipeline_log.score(X_train , y_train)
        X_test

        # %%

        X_test['predict'] = pred
        X_test


        # %%
        X_test

        # %%
        #data_base = mysql.connector.connect(host="localhost" , user="root" , password="Yugioh11." , database="loan_prediction_file_rouge")
        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(
            host="localhost" , user="root" , pw="Yugioh11." , db="loan_prediction_file_rouge"))
        conn = engine.connect()
        X_test.to_sql('ml_pred', conn, if_exists='replace', index = False)

        # %%
        mlflow.end_run()
  


 