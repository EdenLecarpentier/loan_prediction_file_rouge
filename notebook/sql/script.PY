import pyodbc 
import mysql.connector

data_base = mysql.connector.connect(host="localhost" , user="root" , password="Yugioh11." , database="loan_prediction_file_rouge")

cursor = data_base.cursor()

cursor.execute('''
                INSERT INTO loan_prediction (Loan_ID , Gender , Married , Dependents , Education , Self_Employed , ApplicantIncome , CoapplicantIncome , LoanAmount , Loan_Amount_Term , Credit_History , Property_Area , Loan_Status)
                VALUES('LP000001',1 ,1 , 0, 1,0 ,2000 ,1900 ,700 , 360, 0, 0,1)
                
                
                ''')
data_base.commit()