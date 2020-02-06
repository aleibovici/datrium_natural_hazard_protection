FROM python:3
COPY . /
RUN pip install pystrich six requests botocore pyowm
RUN ln -sf /dev/stdout /main.log
CMD [ "python", "./main.py" ]