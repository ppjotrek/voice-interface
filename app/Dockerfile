# Use the official Python image as a base image
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

RUN apt-get update && apt-get install -y \
    libasound-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    espeak-ng

RUN pip install -r requirements.txt

CMD ["python", "calc.py"]