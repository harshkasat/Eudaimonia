# AI-Powered Blog Creation

## Overview
Effortlessly generate, publish, and organize engaging blogs using AI. This project integrates FastAPI, Notion, and the Facebook Graph API to streamline your content creation process.

## Features
- **AI-Driven Blog Generation:** Automatically generate high-quality blog content with advanced AI.
- **Seamless Publishing:** Publish your content directly to Facebook pages or groups using the Facebook Graph API.
- **Effortless Content Management:** Organize and manage your blog posts in Notion.

## Tech Stack
- **FastAPI:** A high-performance, easy-to-use web framework for the backend API.
- **Facebook Graph API:** Publish and manage content on Facebook.
- **Notion API:** Organize and manage blog content within Notion.

## Demo Video
* Check out the demo of how the project works:

https://github.com/user-attachments/assets/d3f8a2b8-20fc-40f2-baea-3da72d5d0138

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshkasat/Eudaimonia
   cd Eudaimonia

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Set up environment variables:
   * Create a .env file and add your API keys and other credentials:
     ```bash
     FACEBOOK_ACCESS_TOKEN=<your-facebook-access-token>
     FACEBOOK_APP_SECRET = <your-facebook-app-secert>
     FACEBOOK_APP_ID = <your-facebook-app-id>
     GEMINI_API_KEY = <your-google-gemini-api-key>
     NOTION_DATABASE_ID = <your-notion-database-id>
     SLACK_APP_TOKEN = <your-slack-app-token>
     SLACK_OAUTH_TOKEN = <your-slack-oauth-token>
     TOKEN_CREATED_TIME = <your-token-created-time-facebook>
     NOTION_API_KEY=<your-notion-api-key>
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload

## Running with Docker

You can also run the application using Docker.

### Building the Docker Image

To build the Docker image, use the following command:

```bash
docker build -t ai-blog-creation .
```

### Running the Docker Container

To run the Docker container, use the following command:

```bash
docker run -p 8000:8000 ai-blog-creation
```

- If you encounter a conflict with an existing container name, you can remove the existing container with:

```bash
docker rm ai-blog-creation
```
