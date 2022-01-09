FROM continuumio/anaconda3:4.4.0
COPY . /Users/abhinav/Desktop/machinelearning/BankNote
EXPOSE 5000
WORKDIR /Users/abhinav/Desktop/machinelearning/BankNote
CMD python app2.py
RUN pip install -r requirements.txt
