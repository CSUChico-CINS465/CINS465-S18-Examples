FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD /code/ /code/
RUN pip install -r requirements.txt
#Create a new group
RUN groupadd -r djangouser
#Create a new user for the group
RUN useradd -r -g djangouser djangouser
#switch to the new user account
USER djangouser
