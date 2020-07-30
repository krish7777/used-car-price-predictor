FROM continuumio/anaconda3:4.4.0
COPY requirements.txt ./usr/app/requirements.txt
WORKDIR /usr/app/
RUN pip install -r requirements.txt
COPY . /usr/app/
# EXPOSE 5000

CMD python app.py
