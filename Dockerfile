# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV FACEBOOK_ACCESS_TOKEN=<your-facebook-access-token>
ENV FACEBOOK_APP_SECRET = <your-facebook-app-secert>
ENV FACEBOOK_APP_ID = <your-facebook-app-id>
ENV GEMINI_API_KEY = <your-google-gemini-api-key>
ENV NOTION_DATABASE_ID = <your-notion-database-id>
ENV SLACK_APP_TOKEN = <your-slack-app-token>
ENV SLACK_OAUTH_TOKEN = <your-slack-oauth-token>
ENV TOKEN_CREATED_TIME = <your-token-created-time-facebook>
ENV NOTION_API_KEY=<your-notion-api-key>


# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
