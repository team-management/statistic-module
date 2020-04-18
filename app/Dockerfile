FROM python:3.7.3


WORKDIR /usr/src/app

COPY . /usr/src/app
#COPY commit /usr/src/app/commit

RUN pip install .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#RUN pip3 install requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run run.py when the container launches
ENTRYPOINT ["python"]
CMD ["run.py"]
