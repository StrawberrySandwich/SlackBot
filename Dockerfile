# Use Python base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install flask
RUN pip install slack_sdk
RUN pip install slack_bolt
RUN pip install dotenv

# Expose port 5000
EXPOSE 5000

# Run Flask app
CMD ["python", "SlackBot.py"]