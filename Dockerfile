FROM python

WORKDIR /opt/program
ADD . /opt/program

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000