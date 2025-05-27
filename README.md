# Eudaimonia: Automated Content Creation and Facebook Posting

This project automates the process of creating content from prompts, generating images, posting to Facebook, and updating a Notion database with post performance metrics.  It uses a Large Language Model (LLM) for content generation and interacts with the Notion and Facebook APIs.

## 1. Project Overview

Eudaimonia streamlines content creation and social media management.  It retrieves prompts and image specifications from a Notion database, uses an LLM to generate content, creates an image (presumably using a separate service not detailed in the provided code), posts the content and image to a Facebook page, and then updates the Notion database with the post's ID, view count, and like count. This allows for efficient content creation and tracking of social media performance.

## 2. Table of Contents

* [Project Overview](#1-project-overview)
* [Prerequisites](#4-prerequisites)
* [Installation Guide](#5-installation-guide)
* [Configuration](#6-configuration)
* [Usage Examples](#7-usage-examples)
* [Project Architecture](#8-project-architecture)
* [License](#17-license)


## 4. Prerequisites

* **Python 3.x:** The project is written in Python.
* **Notion API Key:**  You need a Notion API key and database ID configured in `Notion/Config/notion_config.py`.
* **Facebook App ID, App Secret, and Access Token:**  These are required and should be stored securely in a `.env` file.  The script `refresh_facebook_token.py` handles token refresh.  The script needs appropriate permissions to post to Facebook and access post insights.
* **LLM API Key:**  An API key for your chosen Large Language Model (not specified in the code).  Configuration is likely in `LLM/Config/llm_config.py`.
* **Required Python Libraries:** `requests`, `dotenv`, and potentially others depending on the LLM and image generation libraries used.


## 5. Installation Guide

1. **Clone the repository:** `git clone https://github.com/harshkasat/Eudaimonia.git`
2. **Create a `.env` file:**  Place your Facebook App ID, App Secret, and initial Access Token in a `.env` file in the root directory.  The format should be:
   ```
   FACEBOOK_APP_ID=your_app_id
   FACEBOOK_APP_SECRET=your_app_secret
   FACEBOOK_ACCESS_TOKEN=your_access_token
   TOKEN_CREATED_TIME=0  (Initial value)
   ```
3. **Install dependencies:**  Use pip to install the required libraries.  The exact list is not explicitly provided but includes `requests` and `python-dotenv` at minimum.  For example:  `pip install -r requirements.txt` (assuming a `requirements.txt` file exists).
4. **Configure Notion and LLM:** Update the configuration files (`Notion/Config/notion_config.py` and `LLM/Config/llm_config.py`) with your respective API keys and database IDs.
5. **Run `main.py`:** Execute the `main.py` script to start the process.


## 6. Configuration

The project relies heavily on environment variables and configuration files.

* **`.env`:** Contains Facebook credentials.
* **`Notion/Config/notion_config.py`:**  Contains Notion API key and database ID.
* **`LLM/Config/llm_config.py`:** Contains LLM API key and potentially other settings.

Ensure these files are correctly configured before running the script.


## 7. Usage Examples

The main functionality is triggered by running `main.py`.  This script:

1. Retrieves a page from the Notion database using `GetPage().get_page()`.
2. Sends the prompt to the LLM to generate content using `RetrieveEndpoint().retrieve_content()`.
3. Posts the generated content and image to Facebook using `CreatePost().post_image_and_message()`.
4. Updates the Facebook post's view and like counts using `UpdateFacebook().view_count()` and `UpdateFacebook().like_count()`.
5. Updates the Notion database with the post details and metrics using `UpdateDetail().update_content_generation()`.

Example from `main.py`:

```python
get_image_n_prompt_response = GetPage().get_page()
retrieve_content = RetrieveEndpoint().retrieve_content(get_image_n_prompt_response)
post_id = CreatePost().post_image_and_message(message=retrieve_content)
# ... rest of the update process ...
```


## 8. Project Architecture

The project is structured into several modules:

* **Notion:** Handles interaction with the Notion API (fetching data and updating it).
* **LLM:**  Interacts with the Large Language Model API for content generation.
* **Facebook:**  Manages Facebook API interactions (posting and retrieving metrics).
* **Config:** Holds configuration files for different services.


## 17. License

[Specify the license here.  The provided code does not include a license.]


This README provides a starting point.  Further details on error handling, specific LLM and image generation libraries, and more comprehensive documentation are needed for a complete description.  The code snippets provided offer a glimpse into the core functionality.
