# app/Dockerfile

FROM python:3.9-slim



#RUN apt-get update && apt-get install -y \
#    build-essential \
#    software-properties-common \
#    git \
#    && rm -rf /var/lib/apt/lists/*
#
#RUN git clone https://github.com/streamlit/streamlit-example.git .
#RUN pip install -r requirements.txt
COPY requirements.txt requirements.txt

COPY app.py app.py
CMD mlflow experiments create --experiment-name file_rouge_loan_pred

#ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]